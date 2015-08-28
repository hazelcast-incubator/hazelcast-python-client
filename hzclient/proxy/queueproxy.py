__author__ = 'jonathanbrodie'
from hzclient.codec import proxycodec
from hzclient.codec import queuecodec
from hzclient.clientmessage import ClientMessage
from util import encode

class QueueProxy(object):
    def __init__(self,title,connfamily):
        self.title=title
        self.connection=connfamily
        firstpack=proxycodec.createProxy(encode.encodestring(self.title), "hz:impl:queueService")
        self.connection.sendPackage(firstpack.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(firstpack.correlation)
    def AddAll(self,   dataList):
        msg=queuecodec.QueueAddAllCodec.encodeRequest( encode.encodestring(self.title), dataList)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueAddAllCodec.decodeResponse(msg2).response
    def AddListener(self,   includeValue, eventhandler):
        msg=queuecodec.QueueAddListenerCodec.encodeRequest( encode.encodestring(self.title), encode.encodeboolean(includeValue))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        self.connection.eventregistry[correlationid]=queuecodec.QueueAddListenerCodec.EventHandler(eventhandler)
        return queuecodec.QueueAddListenerCodec.decodeResponse(msg2).response
    def Clear(self,  ):
        msg=queuecodec.QueueClearCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return None
    def CompareAndRemoveAll(self,   dataList):
        msg=queuecodec.QueueCompareAndRemoveAllCodec.encodeRequest( encode.encodestring(self.title), dataList)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueCompareAndRemoveAllCodec.decodeResponse(msg2).response
    def CompareAndRetainAll(self,   dataList):
        msg=queuecodec.QueueCompareAndRetainAllCodec.encodeRequest( encode.encodestring(self.title), dataList)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueCompareAndRetainAllCodec.decodeResponse(msg2).response
    def ContainsAll(self,   dataList):
        msg=queuecodec.QueueContainsAllCodec.encodeRequest( encode.encodestring(self.title), dataList)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueContainsAllCodec.decodeResponse(msg2).response
    def Contains(self,   value):
        msg=queuecodec.QueueContainsCodec.encodeRequest( encode.encodestring(self.title), value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueContainsCodec.decodeResponse(msg2).response
    def DrainTo(self,  ):
        msg=queuecodec.QueueDrainToCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueDrainToCodec.decodeResponse(msg2)
    def DrainToMaxSize(self,   maxSize):
        msg=queuecodec.QueueDrainToMaxSizeCodec.encodeRequest( encode.encodestring(self.title), encode.encodeint32(maxSize))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueDrainToMaxSizeCodec.decodeResponse(msg2)
    def IsEmpty(self,  ):
        msg=queuecodec.QueueIsEmptyCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueIsEmptyCodec.decodeResponse(msg2).response
    def Iterator(self,  ):
        msg=queuecodec.QueueIteratorCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueIteratorCodec.decodeResponse(msg2)

    def Offer(self,   value, timeoutMillis):
        msg=queuecodec.QueueOfferCodec.encodeRequest( encode.encodestring(self.title), value, encode.encodeint64(timeoutMillis))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueOfferCodec.decodeResponse(msg2).response
    def Peek(self,  ):
        msg=queuecodec.QueuePeekCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueuePeekCodec.decodeResponse(msg2).response
    def Poll(self,   timeoutMillis):
        msg=queuecodec.QueuePollCodec.encodeRequest( encode.encodestring(self.title),encode.encodeint64(timeoutMillis))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueuePollCodec.decodeResponse(msg2).response
    def Put(self,   value):
        msg=queuecodec.QueuePutCodec.encodeRequest( encode.encodestring(self.title), value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return None
    def RemainingCapacity(self,  ):
        msg=queuecodec.QueueRemainingCapacityCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueRemainingCapacityCodec.decodeResponse(msg2).response
    def Remove(self,   value):
        msg=queuecodec.QueueRemoveCodec.encodeRequest( encode.encodestring(self.title), value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueRemoveCodec.decodeResponse(msg2).response
    def RemoveListener(self,   registrationId):
        msg=queuecodec.QueueRemoveListenerCodec.encodeRequest( encode.encodestring(self.title), encode.encodestring(registrationId))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueRemoveListenerCodec.decodeResponse(msg2).response
    def Size(self,  ):
        msg=queuecodec.QueueSizeCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueSizeCodec.decodeResponse(msg2).response
    def Take(self,  ):
        msg=queuecodec.QueueTakeCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return queuecodec.QueueTakeCodec.decodeResponse(msg2).response
