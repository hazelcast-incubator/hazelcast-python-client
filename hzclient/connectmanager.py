__author__ = 'Jonathan Brodie'
import asyncore, socket,asynchat,time,threading,struct
from clientmessage import AuthenticationMessage
from clientmessage import ClientMessage


class ConnectionManager(object):
    def __init__(self,smart=False):
        self.messages={}
        self.proxies=[]
        self.__correlationid__=0
        self.connections=[]
        self.events=[]
        self.eventregistry={}
        self.connected=False
        firstConnection=HazelConnection('127.0.0.1',5701,self)
        self.connections.append(firstConnection)
        asyncore.loop(count=1)
        self.event_thread_flag=threading.Event()
        self.event_thread=threading.Thread(target= self.event_step)
        self.event_thread.daemon=True
        response=self.getPackageWithCorrelationId(self.__correlationid__-1,True)
        self.event_thread.start()
        if response is not None:
            print "Connection has been initalized"
        else:
            print "There was an error connecting to the server!"
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

        mythread=threading.Thread(target=self.waitForPackageWithCorrelationId,args=(id,))
        mythread.start()
        mythread.join(timeout=10)
        print "we didn't make it here did we..."
        if id in self.messages.keys():
            print "1"
            return self.messages[id]
        elif retry:
            print "2"
            print id
            mythread=threading.Thread(target=self.waitForPackageWithCorrelationId,args=(id,))
            mythread.start()
            mythread.join()
            return self.messages[id]
        else:
            #ping the server to keep the connection alive
            print "3"
            return None

    def waitForPackageWithCorrelationId(self,id):
        while id not in self.messages.keys():
            asyncore.loop(count=1)

    def msg_step(self):
        while True:
            self.msg_thread_flag.wait()
            for message in self.messagelist:
                print "message!"
                newmsg=ClientMessage.decodeMessage(message)
                self.messages[newmsg.correlation]=message
                self.messagelist.remove(message)
            self.msg_thread_flag.clear()

    '''
    method for manager to process events outside of the io thread
    '''
    def event_step(self):
        while True:
            #self.event_thread_flag.wait()
            for event in self.events:
                id=event.correlation
                for ids in self.eventregistry:
                    if id == ids:
                        self.eventregistry[id].handle(event)
                        self.events.remove(event)
            #self.event_thread_flag.clear()


class HazelConnection(asyncore.dispatcher):

    def __init__(self,address,port,manager):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.manager=manager
        self.connect((address,port))
        msg=AuthenticationMessage()
        self.manager.adjustCorrelationId(msg)
        self.setblocking(1)
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
            print currentmsg.correlation
            if currentmsg.isEvent():
                self.manager.events.append(clientmsg)
                    #self.manager.event_thread.start()
            else:
                self.manager.messages[currentmsg.correlation]=currentinput
                if len(self.manager.events) == 0:
                    self.manager.event_thread_flag.clear()
            input=input[msgsize:]
