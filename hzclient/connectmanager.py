__author__ = 'Jonathan Brodie'
import asyncore, socket,asynchat,time,threading,struct,util.util,util.encode,Queue,sys,select

from clientmessage import AuthenticationMessage
from clientmessage import ClientMessage
from hzclient.codec import clientcodec

class ConnectionManager(object):
    def __init__(self,config,smart=False):
        self.config=config
        self.smart=smart
        self.messages={}
        self.corr_conn={}
        self.messagelist=[]
        self.deadconnections=[]
        self.proxies=[]
        self.__correlationid__=0
        self.connections=[]


        self.messagesignal={}

        self.events=[]
        self.eventregistry={}

        self.packageflag=threading.Lock()
        self.messageflag=threading.Event()


        self.partitiontable=None

        firstConnection=HazelConnection('192.168.1.186',5701,self)
        self.connections.append(firstConnection)

        self.iothread=threading.Thread(target=self.ioloop)
        self.iothread.start()

        #get the first response from the server

        initialresponse=self.getPackageWithCorrelationId(self.__correlationid__-1,True)
        print "did we get here?"
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

            self.updatePartitionTable(response.index)
            members=response.members

            for member in members:
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
        self.eventthreadflag=threading.Event()
        self.event_thread=threading.Thread(target= self.eventloop)
        self.event_thread.start()


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

                if i != self.partitiontable[clientmsg.partition]:
                    self.sendPackageOnConnection(clientmsg,self.connections[i])
                    sent=True
        else:
            for connection in self.connections:
                if not sent:
                    self.sendPackageOnConnection(clientmsg,connection)
                    sent=True

        if not sent:
            print "ERROR: Could not submit to appropriate member! redelegating..."
            for connection in self.connections:
                if not sent:
                    self.sendPackageOnConnection(clientmsg,connection)

    def sendPackageOnConnection(self,clientmsg,conn):
        self.messagesignal[clientmsg.correlation]=threading.Event()
        conn.sendmsg(clientmsg.encodeMessage())
        self.corr_conn[clientmsg.correlation]=conn

    def updateMemberList(self,memberlist):
        newlist=[]
        for member in memberlist:
            memberport=member.port
            memberaddress=member.host
            for connection in self.connections:
                if connection.memberport==member.port and connection.memberaddress==memberaddress:
                    newlist.append(connection)
                    break

        self.connections=newlist


    def updatePartitionTable(self,partitiontable):
        self.partitiontable=partitiontable

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
        for member in response.members:
            print member.host
            print member.port

        self.updatePartitionTable(response.index)
        self.updateMemberList(response.members)
        print self.partitiontable
        print self.connections
        clientmsg.partition=newpartition




    def check_connections(self,timeout=15.0,use_poll=False):
        """
        Similar to asyncore.loop(), but times out after the timeout and only loops once to check the connections if we can read or write from them
        :param timeout:
        :param use_poll:
        :return:
        """

        map=asyncore.socket_map

        if use_poll and hasattr(select, 'poll'):
            poll_fun = asyncore.poll2
        else:
            poll_fun = asyncore.poll
        poll_fun(timeout,map)

    def ioloop(self):
        while True:
            self.check_connections()
            if self.deadconnections:
                for connection in self.deadconnections:
                    self.removeconnection(connection)
            if not self.connections:
                self.noconnections()

    def eventloop(self):
        while True:
            self.eventthreadflag.wait(timeout=10)
            if self.eventthreadflag.is_set():
                while len(self.events) > 0:
                    for event in self.events:
                        id=event.correlation
                        for ids in self.eventregistry:
                            if id == ids:
                                self.eventregistry[id].handle(event)
                                self.events.remove(event)
                        if event in self.events:
                            print "ERROR: Could not find registered event handler"

                if len(self.events) == 0:
                    self.eventthreadflag.clear()
            time.sleep(0.1)


    def getPackageWithCorrelationId(self,id,retry=False):
        """
        Gets the package with the specified id
        :param id:
        :param retry:
        :return: the response package with the correlationid id
        """

        #first acquire the lock for the manager's received packages
        returnvalue=None
        self.messagesignal[id].wait(timeout=10)
        if id in self.messages.keys():
            returnvalue=self.messages[id]

        if retry and id not in self.messages.keys():
            print "retrying"
            time.sleep(5)

            self.messagesignal[id].wait(timeout=30)
            if id in self.messages.keys():
                returnvalue=self.messages[id]

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
        boolean=None
        msg=clientcodec.ClientPingCodec.encodeRequest()
        self.adjustCorrelationId(msg)
        corrid=msg.correlation
        self.sendPackageOnConnection(msg,connection)
        self.messageflag.wait(timeout=20)
        returnvalue=None
        if corrid in self.messages.keys():
            returnvalue=self.messages[corrid]
        if returnvalue is not None:
            boolean=True
        else:
            boolean=False
        return boolean

    def removeconnection(self,conn):
        """
        removes the connection conn and any mappings from correlation id to the connection
        :param conn:
        :return:
        """

        if conn in self.deadconnections:
            self.deadconnections.remove(conn)
        self.connections.remove(conn)
        for correlationid, connection in self.corr_conn.items():
            if connection == conn:
                self.corr_conn.pop(correlationid)

class HazelConnection(asyncore.dispatcher):

    def __init__(self,address,port,manager,first=True):
        """
        Init function for a connection to the server
        :param address: address to connect to
        :param port: port to connect to at address
        :param manager: parent manager connection
        :param first: first connection or not
        :return:
        """
        self._writequeue=Queue.Queue()
        self.memberaddress=address
        self.memberport=port
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.manager=manager
        self.setblocking(1)
        username=util.encode.encodestring(self.manager.config.get_username())
        password=util.encode.encodestring("dev-pass")
        if first:
            msg=clientcodec.ClientAuthenticationCodec.encodeRequest(username,password,None,None,util.encode.encodeboolean(True))
        else:
            msg=clientcodec.ClientAuthenticationCodec.encodeRequest(username,password,util.encode.encodestring(self.manager.uuid),util.encode.encodestring(self.manager.owneruuid),util.encode.encodeboolean(False))
        self.manager.adjustCorrelationId(msg)
        self.manager.messagesignal[msg.correlation]=threading.Event()
        self.initbuffer="CB2PHY"+msg.encodeMessage()
        self.connect((address,port))


    def handle_write(self):
        if not self._writequeue.empty():
            msg=self._writequeue.get()
            print "writing to cluster!"
            self.send(msg)


    def sendmsg(self,msg):
        self._writequeue.put(msg)
    def handle_connect(self):
        """
        This function is called when the client connects
        :return:
        """
        self.sendmsg(self.initbuffer)

    def handle_read(self):
        """
        This function is called when there is data available to be read
        :return:
        """
        data=self.recv(2048)
        self.process_input(data)


    def process_input(self,input):
        """
        Process the input and put it in either received messages or events
        :param input: raw bytes received
        :return:
        """
        while len(input) > 0:
            clientmsg=ClientMessage.decodeMessage(input)
            msgsize=clientmsg.FRAME_SIZE

            currentinput=input[:msgsize]
            currentmsg=ClientMessage.decodeMessage(currentinput)
            if currentmsg.isEvent():
                if not self.manager.eventthreadflag.is_set():
                    self.manager.eventthreadflag.set()
                self.manager.events.append(clientmsg)
            else:
                self.manager.messagesignal[currentmsg.correlation].set()
                if not self.manager.messageflag.is_set():
                    self.manager.messageflag.set()
                self.manager.messages[currentmsg.correlation]=currentinput
            input=input[msgsize:]