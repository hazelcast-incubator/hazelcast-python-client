__author__ = 'Jonathan Brodie'
import asyncore, socket,asynchat,time,threading,struct,util.util,util.encode
from clientmessage import AuthenticationMessage
from clientmessage import ClientMessage
from hzclient.codec import clientcodec

class ConnectionManager(object):
    def __init__(self,smart=False):
        self.messages={}
        self.messagelist=[]
        self.proxies=[]
        self.__correlationid__=0
        self.connections=[]
        self.events=[]
        self.eventregistry={}
        self.connected=False
        self.lock=threading.Lock()

        firstConnection=HazelConnection('127.0.0.1',5701,self)
        self.connections.append(firstConnection)
        self.step_thread=threading.Thread(target = self.step)
        self.step_thread.start()

        #get the first response from the server
        initialresponse=self.getPackageWithCorrelationId(self.__correlationid__-1,True)
        msg=ClientMessage.decodeMessage(initialresponse)
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
            self.sendPackage(msg.encodeMessage())
            response=self.getPackageWithCorrelationId(correlationid,retryable)
            msg2=ClientMessage.decodeMessage(response)

            response=clientcodec.ClientGetPartitionsCodec.decodeResponse(msg2)
            i=1

            for member in response.members:
                i=i+1
                memberhost=member.host
                memberport=member.port
                if memberhost != "127.0.0.1" and memberport != 5701:
                    newConnection=HazelConnection(memberhost,memberport,self,first=False)
                    response=self.getPackageWithCorrelationId(self.__correlationid__-1,True)
                    self.connections.append(newConnection)
                    if response is not None:
                        print "Successfully added new connection"
        #else:
            #raise Timeout Exception

    def sendPackage(self, binarypackage):
        #do logic in determining which connection to use to send the package, for now use a dumb for loop
        for i in self.connections:
            i.send(binarypackage)

    def adjustCorrelationId(self,clientmsg):
        clientmsg.correlation=self.__correlationid__
        self.__correlationid__ += 1

    def adjustPartitionId(self,clientmsg,opkey):
        msg=clientcodec.ClientGetPartitionsCodec.encodeRequest()
        self.adjustCorrelationId(msg)
        retryable=msg.retryable
        correlationid=msg.correlation
        self.sendPackage(msg.encodeMessage())
        response=self.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        response=clientcodec.ClientGetPartitionsCodec.decodeResponse(msg2)
        newpartition=util.util.computepartitionid(response.index,opkey)
        clientmsg.partition=newpartition

    def step(self):
        """
        Step function.  This thread is initialized at the beginning
        :return:
        """
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

            #release the lock
            self.lock.release()

    def getPackageWithCorrelationId(self,id,retry=False):
        """
        Gets the package with the specified id
        :param id:
        :param retry:
        :return:
        """

        #first acquire the lock for the manager
        self.lock.acquire()
        self.waitForPackageWithCorrelationId(id,iterations=10)
        returnvalue=None
        if id in self.messages.keys():
            returnvalue=self.messages[id]
        elif retry:

            mythread=threading.Thread(target=self.waitForPackageWithCorrelationId,args=(id,))
            mythread.start()
            mythread.join()
            self.waitForPackageWithCorrelationId(id,iterations=-1)
            returnvalue=self.messages[id]
        else:
            #ping the server to keep the connection alive
            mythread=threading.Thread(target=self.ping)
            mythread.start()

            returnvalue=None

        #now that we're done, we can release the lock
        self.lock.release()
        return returnvalue


    def ping(self):
        self.lock.acquire()
        msg=clientcodec.ClientPingCodec.encodeRequest()
        self.adjustCorrelationId(msg)
        corrid=msg.correlation
        self.sendPackage(msg.encodeMessage())
        response=self.getPackageWithCorrelationId(corrid,False)
        if response is not None:
            print "Server responded to ping"
        else:
            print "no response"
        self.lock.release()


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
        :return:
        """
        i=0
        while id not in self.messages.keys():
            i=i+1
            self.lock.release()
            time.sleep(1.0)
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
