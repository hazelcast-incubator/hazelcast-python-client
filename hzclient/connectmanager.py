__author__ = 'Jonathan Brodie'
import asyncore, socket,asynchat,time,threading,struct,util.util,util.encode

from clientmessage import AuthenticationMessage
from clientmessage import ClientMessage
from hzclient.codec import clientcodec

class ConnectionManager(object):
    def __init__(self,smart=False):
        self.smart=smart
        self.messages={}
        self.corr_conn={}
        self.messagelist=[]
        self.deadconnections=[]
        self.proxies=[]
        self.__correlationid__=0
        self.connections=[]



        self.events=[]
        self.eventregistry={}


        self.lock=threading.Lock()
        self.partitiontable=None

        firstConnection=HazelConnection('127.0.0.1',5701,self)
        self.connections.append(firstConnection)
        self.step_thread=threading.Thread(target = self.step)
        self.step_thread.start()

        #get the first response from the server

        initialresponse=self.getPackageWithCorrelationId(self.__correlationid__-1,True)
        initialresponse=clientcodec.ClientAuthenticationCodec.decodeResponse(ClientMessage.decodeMessage(initialresponse))
        self.uuid=initialresponse.uuid
        self.owneruuid=initialresponse.ownerUuid

        #if the client is smart, initialize other connections
        if initialresponse is not None:
            print "Connection has been initalized"
        else:
            print "There was an error connecting to the server!"

        if smart:
            msg=clientcodec.ClientGetPartitionsCodec.encodeRequest()
            self.adjustCorrelationId(msg)
            retryable=msg.retryable
            correlationid=msg.correlation
            self.sendPackage(msg)
            response=self.getPackageWithCorrelationId(correlationid,retryable)
            msg2=ClientMessage.decodeMessage(response)

            response=clientcodec.ClientGetPartitionsCodec.decodeResponse(msg2)

            for member in response.members:
                memberhost=member.host
                memberport=member.port
                if memberhost != "127.0.0.1" and memberport != 5701:
                    newConnection=HazelConnection(memberhost,memberport,self,first=False)
                    self.connections.append(newConnection)
                    response=self.getPackageWithCorrelationId(self.__correlationid__-1,True)
                    if response is not None:
                        print "Successfully added new connection"
        #else:
            #raise Timeout Exception


    def sendPackage(self, clientmsg):
        """

        :param clientmsg: client message to send, unencoded
        :return: connection that was used to send the message.  This isn't needed unless we want to test a connection to a node.
        """
        sent=False
        corr=clientmsg.correlation
        conn=None
        if self.partitiontable is not None and clientmsg.partition >= 0 and self.smart:
            for i in range(len(self.connections)):
                if i == self.partitiontable[clientmsg.partition]:
                    self.connections[i].send(clientmsg.encodeMessage())
                    conn=self.connections[i]
                    sent=True
        else:
            for connection in self.connections:
                if not sent:
                    conn=connection
                    connection.send(clientmsg.encodeMessage())
                    sent=True
        if not sent:
            print "ERROR: Could not submit to appropriate member! redelegating..."
            for connection in self.connections:
                if not sent:
                    conn=connection
                    connection.send(clientmsg.encodeMessage())
                    sent=True
        self.corr_conn[corr]=conn
        self.timer=0
        return conn
    def sendPackageOnAllConnections(self,clientmsg):
        for connection in self.connections:
            connection.send(clientmsg.encodeMessage())

    def sendPackageOnConnection(self,clientmsg,connection):
        for conn in self.connections:
            if conn == connection:
                connection.send(clientmsg.encodeMessage())
                self.corr_conn[clientmsg.correlation]=conn

    def adjustCorrelationId(self,clientmsg):
        clientmsg.correlation=self.__correlationid__
        self.__correlationid__ += 1

    def adjustPartitionId(self,clientmsg,opkey):
        msg=clientcodec.ClientGetPartitionsCodec.encodeRequest()
        self.adjustCorrelationId(msg)
        retryable=msg.retryable
        correlationid=msg.correlation
        self.sendPackage(msg)
        response=self.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        response=clientcodec.ClientGetPartitionsCodec.decodeResponse(msg2)


        newpartition=util.util.computepartitionid(response.index,opkey)
        self.partitiontable=response.index
        clientmsg.partition=newpartition

    def ping_timer(self):
        while True:
            self.lock.acquire()
            self.timer=self.timer+1

            if self.timer >= 200:
                for connection in self.connections:
                    if not self.ping(connection):
                        self.removeconnection(connection)
            self.lock.release()
            time.sleep(1.0)

    def step(self):
        """
        Step function.  This thread is initialized at the beginning.
        Every 200 steps, ping the server.
        :return:
        """
        i=0
        while True:
            #acquire the lock for the thread
            self.lock.acquire()
            self.checkConnections()
            #do normal message processing
            if len(self.messagelist) > 0:
                while len(self.messagelist) > 0:
                    for message in self.messagelist:
                        id = ClientMessage.decodeMessage(message).correlation
                        self.messages[id]=message
                        self.messagelist.remove(message)


            #do event processing
            if len(self.events) > 0:
                while len(self.events) > 0:
                    for event in self.events:
                        id=event.correlation
                        for ids in self.eventregistry:
                            if id == ids:
                                self.eventregistry[id].handle(event)
                                self.events.remove(event)
                        if event in self.events:
                            print "ERROR: Could not find registered event handler"

            #if the client is smart, you should do more stuff here

            if self.deadconnections:
                for connection in self.deadconnections:
                    self.removeconnection(connection)


            if not self.connections:
                self.noconnections()

            #release the lock
            self.lock.release()

    def getPackageWithCorrelationId(self,id,retry=False):
        """
        Gets the package with the specified id
        :param id:
        :param retry:
        :return: the response package with the correlationid id
        """

        #first acquire the lock for the manager
        self.lock.acquire()
        self.waitForPackageWithCorrelationId(id,iterations=20)
        returnvalue=None
        if id in self.messages.keys():
            returnvalue=self.messages[id]
        elif retry:
            self.waitForPackageWithCorrelationId(id,iterations=50)
            if id in self.messages.keys():
                returnvalue=self.messages[id]



        #now that we're done, we can release the lock
        self.lock.release()
        if returnvalue is None:
            #ping the server to keep the connection alive
            alive=self.ping(self.corr_conn[id])

            #check if the ping wasn't successful
            if not alive:
                self.deadconnections.append(self.corr_conn[id])
                print "The connection seems to be dead..."

        return returnvalue


    def noconnections(self):
        """
        Raises an exception and quits
        :return: nothing
        """
        raise ValueError("ERROR: NO CONNECTIONS TO CLUSTER FOUND.  SHUTTING DOWN")

    def ping(self,connection):
        """

        :return: boolean - whether or not the server responded to ping
        """
        bool=None
        msg=clientcodec.ClientPingCodec.encodeRequest()
        self.adjustCorrelationId(msg)
        corrid=msg.correlation
        self.sendPackageOnConnection(msg,connection)

        self.lock.acquire()
        self.waitForPackageWithCorrelationId(corrid,iterations=50)
        returnvalue=None
        if corrid in self.messages.keys():
            returnvalue=self.messages[corrid]
        self.lock.release()
        if returnvalue is not None:
            bool=True
        else:
            bool=False


        return bool

    def removeconnection(self,conn):
        """
        removes the connection conn and any mappings from correlation id to the connection
        :param conn:
        :return:
        """

        self.connections.remove(conn)
        print "SUCCESS"
        for correlationid, connection in self.corr_conn.items():
            if connection == conn:
                self.corr_conn.pop(correlationid)



    def checkConnections(self,n=1):
        """
        Runs asyncore loop for n iterations
        :param n:
        :return:
        """
        asyncore.loop(count=n)


    def waitForPackageWithCorrelationId(self,id,iterations=-1):
        """
        checks if the id has been found, release the lock and sleep to give the step thread time to acquire it, then acquire the lock again
        :param id:
        :param iterations: number of time to try.  If this is -1, then it will loop until the id has been found
        :return: none
        """
        i=0
        while id not in self.messages.keys():
            i=i+1
            self.lock.release()
            time.sleep(0.1)
            self.lock.acquire()
            if iterations != -1 and i > iterations:
                break

class HazelConnection(asyncore.dispatcher):

    def __init__(self,address,port,manager,first=True):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.manager=manager
        self.setblocking(1)
        username=util.encode.encodestring("dev")
        password=util.encode.encodestring("dev-pass")
        if first:
            msg=clientcodec.ClientAuthenticationCodec.encodeRequest(username,password,None,None,util.encode.encodeboolean(True))
        else:
            msg=clientcodec.ClientAuthenticationCodec.encodeRequest(username,password,util.encode.encodestring(self.manager.uuid),util.encode.encodestring(self.manager.owneruuid),util.encode.encodeboolean(False))
        self.manager.adjustCorrelationId(msg)
        self.writebuffer="CB2PHY"+msg.encodeMessage()
        self.connect((address,port))
        self.initialized=False
    def handle_connect(self):
        self.send(self.writebuffer)
        print "Connected"
        self.writebuffer=""

    def handle_read(self):
        data=self.recv(2048)
        self.process_input(data)


    def process_input(self,input):
        while len(input) > 0:
            clientmsg=ClientMessage.decodeMessage(input)
            msgsize=clientmsg.FRAME_SIZE

            currentinput=input[:msgsize]
            currentmsg=ClientMessage.decodeMessage(currentinput)
            if currentmsg.isEvent():
                self.manager.events.append(clientmsg)
                    #self.manager.event_thread.start()
            else:
                self.manager.messagelist.append(currentinput)
            input=input[msgsize:]
