__author__ = 'Jonathan Brodie'
import asyncore, socket,asynchat,time,threading
from clientmessage import AuthenticationMessage
from clientmessage import ClientMessage


class ConnectionManager(object):
    def __init__(self,smart=False):
        self.messages={}
        self.__correlationid__=0
        self.connections=[]
        self.events=[]
        self.eventregistry={}
        self.connected=False
        firstConnection=HazelConnection('127.0.0.1',5702,self)
        self.connections.append(firstConnection)
        asyncore.loop(count=1)
        #else:
            #raise Timeout Exception

    def sendPackage(self, binarypackage):
        #do logic in determining which connection to use to send the package, for now use a dumb for loop
        for i in self.connections:
            i.send(binarypackage)

    def adjustCorrelationId(self,clientmsg):
        clientmsg.correlation=self.__correlationid__
        self.__correlationid__ += 1

    def getPackageWithCorrelationId(self,id,retry=False):
        #do submission stuff up here
        mythread=threading.Thread(target=self.waitForPackageWithCorrelationId,args=(id,))
        mythread.start()
        mythread.join(timeout=5000)

        if id in self.messages.keys():
            return self.messages[id]
        elif retry:
            mythread=threading.Thread(target=self.waitForPackageWithCorrelationId,args=(id,))
            mythread.start()
            mythread.join()
            return self.messages[id]
        else:
            #ping the server to keep the connection alive
            return None

    def waitForPackageWithCorrelationId(self,id):
        while id not in self.messages.keys():
            asyncore.loop(count=1)


class HazelConnection(asyncore.dispatcher):

    def __init__(self,address,port,manager):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect((address,port))
        self.manager=manager
        msg=AuthenticationMessage
        self.writebuffer="CB2PER"+AuthenticationMessage().encodeMessage()
        self.manager.adjustCorrelationId(msg)
        self.readbuffer=[]
        self.receiving=False
        self.initialized=False
    def handle_connect(self):
        self.send(self.writebuffer)
        self.writebuffer=""
    def handle_read(self):
        data=self.recv(2048)
        self.process_input(data)
        print "endpoint!"
    def process_input(self,input):
        clientmsg=ClientMessage.decodeMessage(input)
        if clientmsg.isEvent():
            self.manager.eventregistry[clientmsg.correlation].handle(clientmsg)
        else:
            self.manager.messages[clientmsg.correlation]=input
