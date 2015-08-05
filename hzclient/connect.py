__author__ = 'Jonathan Brodie'

'''
Basic connection class that will connect to a Hazelcast Cluster

'''


import socket,asyncore
from hzclient.clientmessage import ClientMessage,AuthenticationMessage

class HazelcastConnection(object):
    def __init__(self):
        #initialize a default local connection, the user can change these using the below methods
        self.TCP_IP='127.0.0.1'
        self.TCP_PORT=5701
        self.connection=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.connection.setblocking(0)
        self.readFrom=[self.connection]
        self.initial=False
        self.connectConstant="CB2" #Binary Protocol constant
        self.clientType="PHY" #Python client authorization

    def setIPAddress(self, newIP):
        self.TCP_IP=newIP

    def setPort(self, newPort):
        self.TCP_PORT=newPort

    def connectToCluster(self):
        try:
            self.connection.connect((self.TCP_IP,self.TCP_PORT))
            self.initializeConnection()
        except Exception as e:
            print("There was an error connecting to the server!")
            print(e)

    def initializeConnection(self):
        #only run the six bytes at the beginning during the client-server dialog
        if self.initial:
            return

        string=(self.connectConstant+self.clientType).encode()
        self.sendPackage(string)

    def authenticateConnection(self):
        if self.initial:
            return
        authMsg=AuthenticationMessage()
        encoded=authMsg.encodeMessage()
        self.sendPackage(encoded)
        response=self.connection.recv(1024)

        if response is not None:
            self.initial=True


    def sendPackage(self, package):
        #do actual protocol stuff here
        totalsent=0
        self.connection.sendall(package)
        '''
        while totalsent < len(package):
            print("sending package...")
            sent=self.connection.send(package)
            if sent == 0:
                raise RuntimeError("Connection broken")
            totalsent=totalsent+sent
        '''

    def closeConnection(self):
        self.connection.close()

    def waitAndGetPackage(self):
        servermsg=self.connection.recv(32768)
        #if the connection is broken - break
        if servermsg is None:
            print "connection broken"
        return servermsg


