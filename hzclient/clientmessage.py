__author__ = 'Jonathan Brodie'

'''
Created on 6/24/15
ClientMessage Class, this is meant to duplicate the ClientMessage Java class as best
as I can to best ensure the protocol is followed
'''
import sys,struct,ctypes,uuid

class ClientMessage(object):
    def __init__(self):
        #initialize everything

        VERSION=1
        self.BEGIN_FLAG=0x80
        self.END_FLAG=0x40
        self.BEGIN_END_FLAG=self.BEGIN_FLAG | self.END_FLAG


        '''
        ***This could be constructed far more efficiently, but left in the form resembling that of ClientMessage.java
        -The first four bytes are the total size of the message
        -The next byte is the version
        -The next byte is the flag
        -The next two bytes are the message type
        -The next four bytes are the Correlation ID - unique to each message type
        -The next four bytes are the partition ID - -1 will put the ID into the default thread pool
        -The next two bytes define the offset from the start of the frame to the payload (Currently it is only 18 because
        the message header extension isn't used yet)
        -The rest of the message is the payload.
        '''

        FRAME_OFFSET=4
        VERSION_OFFSET=1 + FRAME_OFFSET
        FLAG_OFFSET=VERSION_OFFSET + 1
        TYPE_OFFSET=FLAG_OFFSET + 2
        CORRELATION_OFFSET=TYPE_OFFSET + 4
        PARTITION_OFFSET=CORRELATION_OFFSET+4
        self.DATA_OFFSET=PARTITION_OFFSET+2
        self.HEADER_SIZE=self.DATA_OFFSET

        self.FRAME_SIZE=self.HEADER_SIZE
        nativeOrder=sys.byteorder
        self.littleOrder='little'

        self.version=VERSION
        self.flag=self.BEGIN_END_FLAG
        self.optype=0
        self.correlation=213321
        self.partition=-1
        self.payload=None
        self.retryable=False
        self.extension=None

    def updateSize(self):
        newVersion=ctypes.c_uint8(self.version)
        newFlag=ctypes.c_uint8(self.flag)
        newType=ctypes.c_uint16(self.optype)
        newCorrelation=ctypes.c_uint32(self.correlation)
        newPartition=ctypes.c_int32(self.partition)
        newOffset=ctypes.c_uint16(self.DATA_OFFSET)

        byteArray=bytearray(newVersion)+bytearray(newFlag)+bytearray(newType)+bytearray(newCorrelation)+bytearray(newPartition)+bytearray(newOffset)

        if self.extension is not None:
            byteArray+=self.payload

        if self.payload is not None:
            byteArray+=self.payload
        self.FRAME_SIZE=len(byteArray)+4

    '''
    Getters and setters.  Typically not used in Python but used here so a user knows what variables they should and
    shouldn't be messing with
    '''
    def setVersion(self, vr):
        self.version=vr
    def getVersion(self):
        return self.version
    def setFlagBegin(self):
        self.flag=self.BEGIN_FLAG
    def setFlagEnd(self):
        self.flag=self.END_FLAG
    def setFlagBoth(self):
        self.flag=self.BEGIN_END_FLAG
    def isEvent(self):
        return self.flag == 0xc1
    def setEventFlag(self):
        self.flag=0xc1
    def setOperationType(self, newType):
        self.optype=newType
    def getOperationType(self):
        return self.optype
    def setPartition(self, newPartition):
        self.partition=newPartition
    def getPartition(self):
        return self.partition
    def setPayload(self,payload):
        self.payload=payload
    def set(self,item):
        if self.payload is None:
            self.payload=item
        else:
            self.payload+=item
    def setCorrelation(self,newCorrelation):
        self.correlation=newCorrelation
    def setRetryable(self,bool):
        self.retryable=bool
    def addExtension(self,extension):
        self.extension=extension
        self.DATA_OFFSET+=len(extension)

    def encodeMessage(self):
        #since Python only uses ints and longs and does weird memory stuff, we need to wrap them here using the C types
        newVersion=ctypes.c_uint8(self.version)
        newFlag=ctypes.c_uint8(self.flag)
        newType=ctypes.c_uint16(self.optype)
        newCorrelation=ctypes.c_uint32(self.correlation)
        newPartition=ctypes.c_int32(self.partition)

        byteArray=bytearray(newVersion)+bytearray(newFlag)+bytearray(newType)+bytearray(newCorrelation)+bytearray(newPartition)
        netSize=4+len(byteArray)+2
        self.HEADER_SIZE=netSize
        if self.extension is not None:
            netSize+=len(self.extension)
        self.DATA_OFFSET=netSize
        if self.payload is not None:
            netSize+=len(self.payload)

        self.FRAME_SIZE=netSize


        newSize=ctypes.c_int32(self.FRAME_SIZE)
        newOffset=ctypes.c_uint16(self.DATA_OFFSET)

        byteArray=bytearray(newSize)+byteArray+bytearray(newOffset)
        if self.extension is not None:
            byteArray+=self.extension
        if self.payload is not None:
            byteArray+=self.payload

        return byteArray

    @classmethod
    def decodeMessage(cls, bytesobject):
        headersize=struct.unpack_from("<i",bytes(bytesobject[:4]))[0]
        bytesobject=bytesobject[4:]
        version=struct.unpack_from("<b", bytes(bytesobject[:1]))[0]
        bytesobject=bytesobject[1:]
        flag=struct.unpack_from("<B", bytes(bytesobject[:1]))[0]
        bytesobject=bytesobject[1:]
        type=struct.unpack_from("<h", bytes(bytesobject[:2]))[0]
        bytesobject=bytesobject[2:]
        correlationID=struct.unpack_from("<i", bytes(bytesobject[:4]))[0]
        bytesobject=bytesobject[4:]
        partitionID=struct.unpack_from("<i", bytes(bytesobject[:4]))[0]
        bytesobject=bytesobject[4:]
        dataOffset=struct.unpack_from("<h", bytes(bytesobject[:2]))[0]
        bytesobject=bytesobject[2:]
        new=cls.constructMessageFrom(flag,version,type,correlationID,partitionID,dataOffset,bytesobject)
        return new

    @classmethod
    def constructMessageFrom(cls, flag,version,msgtype,corrID,pID,offset,payload):
        myMessage=cls()
        myMessage.flag=flag
        myMessage.version=version
        myMessage.optype=msgtype
        myMessage.correlation=corrID
        myMessage.partition=pID
        myMessage.DATA_OFFSET=offset
        myMessage.payload=payload
        myMessage.updateSize()
        return myMessage
    def extractIntFromPayload(self):
        int=self.payload[:4]
        self.payload=self.payload[4:]
        int2=struct.unpack_from("<i", int)[0]
        return int2
    def extractLongFromPayload(self):
        int=self.payload[:5]
        self.payload=self.payload[5:]
        int2=struct.unpack_from("<l", int)[0]
        return int2
    def extractBytesFromPayload(self):
        int=self.payload[:4]
        self.payload=self.payload[4:]
        int2=struct.unpack_from("<i", int)[0]
        bytesobject=self.payload[:int2]
        self.payload=self.payload[int2:]
        return bytesobject
    def extractStringFromPayload(self):
        int=self.payload[:4]
        self.payload=self.payload[4:]
        int2=struct.unpack_from("<i", int)[0]
        bytesobject=self.payload[:int2].decode("UTF8")
        self.payload=self.payload[int2:]
        return bytesobject
    def extractBooleanFromPayload(self):
        bool=self.payload[0]
        self.payload=self.payload[1:]
        bool2=struct.unpack_from("<b",bool)[0]
        if bool2==0:
            return False
        else:
            return True
class AuthenticationMessage(ClientMessage):
    def __init__(self):
        super(AuthenticationMessage, self).__init__()
        self.correlation=0
        self.initializeAuthentication()

    def initializeAuthentication(self):
        username="dev"
        password="dev-pass2"
        self.optype=0x2
        uuIDisNull=True
        OwneruuIDisNull=True
        isOwnerConnection=True

        newUser=username.encode("UTF8")
        userlength=len(newUser)
        newPass=password.encode("UTF8")
        passwordlength=len(newPass)

        newbool1=ctypes.c_uint8(uuIDisNull)
        newbool2=ctypes.c_uint8(OwneruuIDisNull)
        newbool3=ctypes.c_uint8(isOwnerConnection)

        authpayload=bytearray(ctypes.c_uint32(userlength))+newUser+bytearray(ctypes.c_uint32(passwordlength))+newPass+bytearray(newbool1)+bytearray(newbool2)+bytearray(newbool3)
        self.setPayload(authpayload)