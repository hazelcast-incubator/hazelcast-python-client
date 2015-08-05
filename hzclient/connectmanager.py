__author__ = 'Jonathan Brodie'
import asyncore, socket,asynchat,time,threading
from clientmessage import AuthenticationMessage
from clientmessage import ClientMessage

class ConnectionManager(object):
    def __init__(self,smart=False):
        self.messages={}
        self.connections=[]
        self.events=[]
        self.eventregistry={}
        self.connected=False
        firstConnection=HazelConnection('127.0.0.1',5701,self)
        self.connections.append(firstConnection)
        self.__correlationid__=0
        asyncore.loop(count=1)
        #else:
            #raise Timeout Exception

    def sendPackage(self, binarypackage):
        #do logic in determining which connection to use to send the package, for now use a dumb for loop
        for i in self.connections:
            i.send(binarypackage)

    def adjustCorrelationId(self,clientmsg):
        clientmsg.correlation=self.__correlationid__
        self.__correlationid__+=1

    def getPackageWithCorrelationId(self,id,retry=False):
        if id in self.messages.keys():
            return self.messages[id]
        elif retry:
            mythread=threading.Thread(target=self.waitForPackageWithCorrelationId,args=(id,))
            mythread.start()
            mythread.join()
            return self.messages[id]
        else:
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
        self.writebuffer="CB2PHY"+AuthenticationMessage().encodeMessage()
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
            self.manager.events.append(input)
        else:
            self.manager.messages[clientmsg.correlation]=input
