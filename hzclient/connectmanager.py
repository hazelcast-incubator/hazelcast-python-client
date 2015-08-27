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
        self.sentmessages={}
        self.corr_conn={}
        self.messagelist=[]
        self.deadconnections=[]
        self.proxies=[]
        self.__correlationid__=0
        self.connections=[]


        self.messagesignal={}

        self.events=[]
        self.eventregistry={}
        self.partitiontable=None
        firstConnection=HazelConnection(config.gethost(),config.getport(),self)
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
            self.updateMemberList(response.members)

        #else:
            #raise Timeout Exception
        self.eventthreadflag=threading.Event()
        self.event_thread=threading.Thread(target= self.eventloop)
        self.event_thread.start()

    def addConnection(self,host, port):
        newconnection=HazelConnection(host,port,self,first=False)
        correlationid=newconnection.initmessage.correlation
        response=self.getPackageWithCorrelationId(correlationid,True)
        if response is not None:
            print "Successfully added new connection"
            self.connections.append(newconnection)

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
        self.sentmessages[clientmsg.correlation]=clientmsg
        conn.sendmsg(clientmsg.encodeMessage())
        self.corr_conn[clientmsg.correlation]=conn

    def updateMemberList(self,memberlist):
        """
        This runs in O(n^2), which my algorithms professor would hate me for, but isn't that bad given that a cluster is
        unlikely to have more than like 100 members
        :param memberlist: memberlist to compare against
        :return:
        """
        #non-smart connections need not apply
        if not self.smart:
            return
        currentlist=self.connections

        #connections that we have but the cluster doesn't - aka dead connections
        deletelist=[]

        #given the member list, distinguish live and dead connections we have
        for connection in currentlist:
            connectionfound=False
            for member in memberlist:
                if member.port == connection.memberport and connection.memberaddress == member.host:
                    connectionfound=True
            if not connectionfound:
                deletelist.append(connection)


        #now iterate the other way to determine if the member has nodes we don't
        newmembers=[]
        for member in memberlist:
            memberfound=False
            for connection in currentlist:
                if member.port == connection.memberport and connection.memberaddress == member.host:
                    memberfound=True
            if not memberfound:
                newmembers.append(member)


        #now clear out the dead connections
        if deletelist:
            for connection in deletelist:
                self.removeconnection(connection)
        #add any new live connections
        if newmembers:
            for member in newmembers:
                self.addConnection(member.host,member.port)

        #Finally, sort our connection list so it's sorted the same way the member list is
        newlist=[]
        for member in memberlist:
            for connection in currentlist:
                if member.port == connection.memberport and connection.memberaddress == member.host:
                    newlist.append(connection)

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
        clientmsg.partition=newpartition
        self.updatePartitionTable(response.index)
        self.updateMemberList(response.members)

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

            self.messagesignal[id].wait(timeout=15)
            if id in self.messages.keys():
                returnvalue=self.messages[id]
            else:
                newmsg=self.sentmessages[id]
                self.adjustCorrelationId(newmsg)
                self.sendPackage(newmsg)
                return self.getPackageWithCorrelationId(newmsg.correlation,retry)

        if returnvalue is None:
            #ping the server to keep the connection alive
            alive=self.ping(self.corr_conn[id])

            #check if the ping wasn't successful
            if not alive:
                self.deadconnections.append(self.corr_conn[id])
                print "The connection seems to be dead..."
            else:
                print "ERROR: The connection is alive but the package could not be found!"

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
        self.messagesignal[corrid].wait(timeout=20)
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
        self.initmessage=msg
        self.initbuffer="CB2PHY"+msg.encodeMessage()
        self.connect((address,port))
    def handle_write(self):
        """
        Called whenever the client can write over the cluster
        :return:
        """
        #don't let the queue block the thread!
        if not self._writequeue.empty():
            msg=self._writequeue.get()
            self.send(msg)
    def sendmsg(self,msg):
        self._writequeue.put(msg)
    def handle_connect(self):
        """
        This function is called when the client connects
        """
        self.sendmsg(self.initbuffer)
    def handle_read(self):
        """
        This function is called when there is data available to be read
        """
        data=self.recv(2048)
        self.process_input(data)
    def process_input(self,input):
        """
        Process the input and put it in either received messages or events
        :param input: raw bytes received
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

                self.manager.messages[currentmsg.correlation]=currentinput
            input=input[msgsize:]