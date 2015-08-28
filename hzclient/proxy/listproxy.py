__author__ = 'jonathanbrodie'

from hzclient.codec import listcodec
from hzclient.codec import proxycodec
from hzclient.clientmessage import ClientMessage
from util import encode
class ListProxy(object):
    def __init__(self,title,connfamily):
        self.title=title
        self.connection=connfamily
        firstpack=proxycodec.createProxy(self.title, "hz:impl:listService")
        self.connection.adjustCorrelationId(firstpack)
        self.connection.sendPackage(firstpack)

        response=self.connection.getPackageWithCorrelationId(firstpack.correlation,firstpack.retryable)

        if response is not None:
            print "Proxy initialized"
        else:
            print "well uh oh"
    def AddAll(self,   valueList):
        msg=listcodec.ListAddAllCodec.encodeRequest( encode.encodestring(self.title), valueList)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListAddAllCodec.decodeResponse(msg2)
    def AddAllWithIndex(self,   index, valueList):
        msg=listcodec.ListAddAllWithIndexCodec.encodeRequest( encode.encodestring(self.title), encode.encodeint32(index), valueList)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListAddAllWithIndexCodec.decodeResponse(msg2)
    def Add(self,   value):
        msg=listcodec.ListAddCodec.encodeRequest( encode.encodestring(self.title), value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListAddCodec.decodeResponse(msg2)
    def AddListener(self,   includeValue, eventhandler):
        msg=listcodec.ListAddListenerCodec.encodeRequest( encode.encodestring(self.title), encode.encodeboolean(includeValue))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        self.connection.eventregistry[correlationid]=listcodec.ListAddListenerCodec.EventHandler(eventhandler)
        return listcodec.ListAddListenerCodec.decodeResponse(msg2)
    def AddWithIndex(self,   index, value):
        msg=listcodec.ListAddWithIndexCodec.encodeRequest( encode.encodestring(self.title), encode.encodeint32(index), value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListAddWithIndexCodec.decodeResponse(msg2)
    def Clear(self,  ):
        msg=listcodec.ListClearCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListClearCodec.decodeResponse(msg2)
    def CompareAndRemoveAll(self,   valueSet):
        msg=listcodec.ListCompareAndRemoveAllCodec.encodeRequest( encode.encodestring(self.title), valueSet)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListCompareAndRemoveAllCodec.decodeResponse(msg2)
    def CompareAndRetainAll(self,   valueSet):
        msg=listcodec.ListCompareAndRetainAllCodec.encodeRequest( encode.encodestring(self.title), valueSet)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListCompareAndRetainAllCodec.decodeResponse(msg2)
    def ContainsAll(self,   valueSet):
        msg=listcodec.ListContainsAllCodec.encodeRequest( encode.encodestring(self.title), valueSet)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListContainsAllCodec.decodeResponse(msg2).response
    def Contains(self,   value):
        msg=listcodec.ListContainsCodec.encodeRequest( encode.encodestring(self.title), value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListContainsCodec.decodeResponse(msg2).response
    def GetAll(self,  ):
        msg=listcodec.ListGetAllCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListGetAllCodec.decodeResponse(msg2).list


    def Get(self, index):
        msg=listcodec.ListGetCodec.encodeRequest( encode.encodestring(self.title), encode.encodeint32(index))
        retryable=msg.retryable
        self.connection.adjustPartitionId(msg, index)
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListGetCodec.decodeResponse(msg2).response
    def IndexOf(self,   value):
        msg=listcodec.ListIndexOfCodec.encodeRequest( encode.encodestring(self.title), value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListIndexOfCodec.decodeResponse(msg2).response
    def IsEmpty(self,  ):
        msg=listcodec.ListIsEmptyCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListIsEmptyCodec.decodeResponse(msg2).response
    def Iterator(self,  ):
        msg=listcodec.ListIteratorCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListIteratorCodec.decodeResponse(msg2).list
    def LastIndexOf(self,   value):
        msg=listcodec.ListLastIndexOfCodec.encodeRequest( encode.encodestring(self.title), value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListLastIndexOfCodec.decodeResponse(msg2).response
    def ListIterator(self,   index):
        msg=listcodec.ListListIteratorCodec.encodeRequest( encode.encodestring(self.title), encode.encodeint32(index))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListListIteratorCodec.decodeResponse(msg2).list
    def Remove(self,   value):
        msg=listcodec.ListRemoveCodec.encodeRequest( encode.encodestring(self.title), value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListRemoveCodec.decodeResponse(msg2).response
    def RemoveListener(self,   registrationId):
        msg=listcodec.ListRemoveListenerCodec.encodeRequest( encode.encodestring(self.title), encode.encodestring(registrationId))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListRemoveListenerCodec.decodeResponse(msg2).response
    def RemoveWithIndex(self,   index):
        msg=listcodec.ListRemoveWithIndexCodec.encodeRequest( encode.encodestring(self.title), encode.encodeint32(index))
        retryable=msg.retryable
        self.connection.adjustPartitionId(msg,index)
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListRemoveWithIndexCodec.decodeResponse(msg2).response

    def Set(self,   index, value):
        msg=listcodec.ListSetCodec.encodeRequest( encode.encodestring(self.title), encode.encodeint32(index), value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListSetCodec.decodeResponse(msg2).response
    def Size(self,  ):
        msg=listcodec.ListSizeCodec.encodeRequest(encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustPartitionId(msg,self.title)
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListSizeCodec.decodeResponse(msg2).response
    def Sub(self,   fromm, to):
        msg=listcodec.ListSubCodec.encodeRequest(encode.encodestring(self.title), fromm, to)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return listcodec.ListSubCodec.decodeResponse(msg2).list