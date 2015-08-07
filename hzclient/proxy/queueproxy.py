__author__ = 'jonathanbrodie'
from hzclient.codec import proxycodec
from hzclient.codec import queuecodec
from hzclient.clientmessage import ClientMessage

class QueueProxy(object):
    def __init__(self,title,connfamily):
        self.title=title
        self.connection=connfamily
        firstpack=proxycodec.createProxy(self.title, "hz:impl:queueService")
        self.connection.sendPackage(firstpack)
        response=self.connection.getPackageWithCorrelationId(firstpack.correlation)
    def AddAll(self,   dataList):
        msg=queuecodec.QueueAddAllCodec.encodeRequest( self.title, dataList)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueAddAllCodec.decodeResponse(msg2)
    def AddListener(self,   includeValue, eventhandler):
        msg=queuecodec.QueueAddListenerCodec.encodeRequest( self.title, includeValue)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        self.connection.eventregistry[correlationid]=queuecodec.QueueAddListenerCodec.EventHandler(eventhandler)
        return queuecodec.QueueAddListenerCodec.decodeResponse(msg2)
    def Clear(self,  ):
        msg=queuecodec.QueueClearCodec.encodeRequest( namself.titlee)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueClearCodec.decodeResponse(msg2)
    def CompareAndRemoveAll(self,   dataList):
        msg=queuecodec.QueueCompareAndRemoveAllCodec.encodeRequest( self.title, dataList)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueCompareAndRemoveAllCodec.decodeResponse(msg2)
    def CompareAndRetainAll(self,   dataList):
        msg=queuecodec.QueueCompareAndRetainAllCodec.encodeRequest( self.title, dataList)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueCompareAndRetainAllCodec.decodeResponse(msg2)
    def ContainsAll(self,   dataList):
        msg=queuecodec.QueueContainsAllCodec.encodeRequest( self.title, dataList)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueContainsAllCodec.decodeResponse(msg2)
    def Contains(self,   value):
        msg=queuecodec.QueueContainsCodec.encodeRequest( self.title, value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueContainsCodec.decodeResponse(msg2)
    def DrainTo(self,  ):
        msg=queuecodec.QueueDrainToCodec.encodeRequest( namself.titlee)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueDrainToCodec.decodeResponse(msg2)
    def DrainToMaxSize(self,   maxSize):
        msg=queuecodec.QueueDrainToMaxSizeCodec.encodeRequest( self.title, maxSize)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueDrainToMaxSizeCodec.decodeResponse(msg2)
    def IsEmpty(self,  ):
        msg=queuecodec.QueueIsEmptyCodec.encodeRequest( namself.titlee)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueIsEmptyCodec.decodeResponse(msg2)
    def Iterator(self,  ):
        msg=queuecodec.QueueIteratorCodec.encodeRequest( namself.titlee)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueIteratorCodec.decodeResponse(msg2)

    def Offer(self,   value, timeoutMillis):
        msg=queuecodec.QueueOfferCodec.encodeRequest( self.title, value, timeoutMillis)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueOfferCodec.decodeResponse(msg2)
    def Peek(self,  ):
        msg=queuecodec.QueuePeekCodec.encodeRequest( namself.titlee)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueuePeekCodec.decodeResponse(msg2)
    def Poll(self,   timeoutMillis):
        msg=queuecodec.QueuePollCodec.encodeRequest( self.title, timeoutMillis)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueuePollCodec.decodeResponse(msg2)
    def Put(self,   value):
        msg=queuecodec.QueuePutCodec.encodeRequest( self.title, value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueuePutCodec.decodeResponse(msg2)
    def RemainingCapacity(self,  ):
        msg=queuecodec.QueueRemainingCapacityCodec.encodeRequest( namself.titlee)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueRemainingCapacityCodec.decodeResponse(msg2)
    def Remove(self,   value):
        msg=queuecodec.QueueRemoveCodec.encodeRequest( self.title, value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueRemoveCodec.decodeResponse(msg2)
    def RemoveListener(self,   registrationId):
        msg=queuecodec.QueueRemoveListenerCodec.encodeRequest( self.title, registrationId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueRemoveListenerCodec.decodeResponse(msg2)
    def Size(self,  ):
        msg=queuecodec.QueueSizeCodec.encodeRequest( namself.titlee)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueSizeCodec.decodeResponse(msg2)
    def Take(self,  ):
        msg=queuecodec.QueueTakeCodec.encodeRequest( namself.titlee)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueTakeCodec.decodeResponse(msg2)
