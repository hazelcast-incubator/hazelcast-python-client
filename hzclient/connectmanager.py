__author__ = 'Jonathan Brodie'
import asyncore, socket,asynchat,time,threading,struct
from clientmessage import AuthenticationMessage
from clientmessage import ClientMessage


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


        #if the client is smart, initialize other connections
        if initialresponse is not None:
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
            returnvalue=None

        #now that we're done, we can release the lock
        self.lock.release()
        return returnvalue



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
    '''
    method for manager to process events outside of the io thread
    '''


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
            if currentmsg.isEvent():
                self.manager.events.append(clientmsg)
                    #self.manager.event_thread.start()
            else:
                self.manager.messagelist.append(currentinput)
            input=input[msgsize:]
