__author__ = 'jonathanbrodie'
from hzclient.codec import cachecodec
from hzclient.codec import proxycodec
from hzclient.clientmessage import ClientMessage
from util import encode
class CacheProxy(object):
    def __init__(self,title,connfamily):
        self.title=title
        self.connection=connfamily
        firstpack=proxycodec.createProxy(self.title, "hz:impl:cacheService")
        self.connection.sendPackage(firstpack)
        response=self.connection.getPackageWithCorrelationId(firstpack.correlation)




    def AddEntryListener(self,   eventhandler):
        msg=cachecodec.CacheAddEntryListenerCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        self.connection.eventregistry[correlationid]=cachecodec.CacheAddEntryListenerCodec.EventHandler(eventhandler)
        return cachecodec.CacheAddEntryListenerCodec.decodeResponse(msg2)
    def AddInvalidationListener(self,   eventhandler):
        msg=cachecodec.CacheAddInvalidationListenerCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        self.connection.eventregistry[correlationid]=cachecodec.CacheAddInvalidationListenerCodec.EventHandler(eventhandler)
        return cachecodec.CacheAddInvalidationListenerCodec.decodeResponse(msg2)
    def Clear(self,  ):
        msg=cachecodec.CacheClearCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheClearCodec.decodeResponse(msg2)
    def ContainsKey(self,   key):
        msg=cachecodec.CacheContainsKeyCodec.encodeRequest( encode.encodestring(self.title), key)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheContainsKeyCodec.decodeResponse(msg2).response
    def CreateConfig(self,  cacheConfig, createAlsoOnOthers):
        msg=cachecodec.CacheCreateConfigCodec.encodeRequest( cacheConfig, encode.encodeboolean(createAlsoOnOthers))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheCreateConfigCodec.decodeResponse(msg2)
    def Destroy(self,  ):
        msg=cachecodec.CacheDestroyCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheDestroyCodec.decodeResponse(msg2).response
    def EntryProcessor(self,   key, entryProcessor, arguments, completionId):
        msg=cachecodec.CacheEntryProcessorCodec.encodeRequest( encode.encodestring(self.title), key, entryProcessor, arguments, encode.encodeint32(completionId))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheEntryProcessorCodec.decodeResponse(msg2).response
    def GetAll(self,   keys, expiryPolicy):
        msg=cachecodec.CacheGetAllCodec.encodeRequest( encode.encodestring(self.title), keys, expiryPolicy)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheGetAllCodec.decodeResponse(msg2).entrySet
    def GetAndRemove(self,   key, completionId):
        msg=cachecodec.CacheGetAndRemoveCodec.encodeRequest( encode.encodestring(self.title), key, encode.encodeint32(completionId))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheGetAndRemoveCodec.decodeResponse(msg2).response
    def GetAndReplace(self,   key, value, expiryPolicy, completionId):
        msg=cachecodec.CacheGetAndReplaceCodec.encodeRequest( encode.encodestring(self.title), key, value, expiryPolicy, encode.encodeint32(completionId))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheGetAndReplaceCodec.decodeResponse(msg2).response
    def Get(self,   key, expiryPolicy):
        msg=cachecodec.CacheGetCodec.encodeRequest( encode.encodestring(self.title), key, expiryPolicy)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheGetCodec.decodeResponse(msg2).response
    def GetConfig(self,   simpleName):
        msg=cachecodec.CacheGetConfigCodec.encodeRequest( encode.encodestring(self.title), encode.encodestring(simpleName))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheGetConfigCodec.decodeResponse(msg2).response
    def Iterate(self,   partitionId, tableIndex, batch):
        msg=cachecodec.CacheIterateCodec.encodeRequest( encode.encodestring(self.title), encode.encodeint32(partitionId), encode.encodeint32(tableIndex), encode.encodeint32(batch))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheIterateCodec.decodeResponse(msg2).response
    def ListenerRegistration(self,   listenerConfig, register, hostname, port):
        msg=cachecodec.CacheListenerRegistrationCodec.encodeRequest( encode.encodestring(self.title), listenerConfig, encode.encodeboolean(register), encode.encodestring(hostname), encode.encodeint32(port))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheListenerRegistrationCodec.decodeResponse(msg2)
    def LoadAll(self,   keys, replaceExistingValues):
        msg=cachecodec.CacheLoadAllCodec.encodeRequest( encode.encodestring(self.title), keys, encode.encodeboolean(replaceExistingValues))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheLoadAllCodec.decodeResponse(msg2)
    def ManagementConfig(self,   isStat, enabled, hostname, port):
        msg=cachecodec.CacheManagementConfigCodec.encodeRequest( encode.encodestring(self.title), encode.encodeboolean(isStat), encode.encodeboolean(enabled), encode.encodestring(hostname), encode.encodeint32(port))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheManagementConfigCodec.decodeResponse(msg2).response
    def Put(self,   key, value, expiryPolicy, get, completionId):
        msg=cachecodec.CachePutCodec.encodeRequest( encode.encodestring(self.title), key, value, expiryPolicy, encode.encodeboolean(get), encode.encodeint32(completionId))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CachePutCodec.decodeResponse(msg2).response
    def PutIfAbsent(self,   key, value, expiryPolicy, completionId):
        msg=cachecodec.CachePutIfAbsentCodec.encodeRequest( encode.encodestring(self.title), key, value, expiryPolicy,  encode.encodeint32(completionId))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CachePutIfAbsentCodec.decodeResponse(msg2).response
    def RemoveAll(self,   completionId):
        msg=cachecodec.CacheRemoveAllCodec.encodeRequest( encode.encodestring(self.title), encode.encodeint32(completionId))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheRemoveAllCodec.decodeResponse(msg2)
    def RemoveAllKeys(self,   keys, completionId):
        msg=cachecodec.CacheRemoveAllKeysCodec.encodeRequest( encode.encodestring(self.title), keys,  encode.encodeint32(completionId))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheRemoveAllKeysCodec.decodeResponse(msg2)
    def Remove(self,   key, currentValue, completionId):
        msg=cachecodec.CacheRemoveCodec.encodeRequest( encode.encodestring(self.title), key, currentValue, encode.encodeint32(completionId))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheRemoveCodec.decodeResponse(msg2).response
    def RemoveEntryListener(self,   registrationId):
        msg=cachecodec.CacheRemoveEntryListenerCodec.encodeRequest( encode.encodestring(self.title), encode.encodestring(registrationId))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheRemoveEntryListenerCodec.decodeResponse(msg2).response
    def RemoveInvalidationListener(self,   registrationId):
        msg=cachecodec.CacheRemoveInvalidationListenerCodec.encodeRequest( encode.encodestring(self.title), encode.encodestring(registrationId))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheRemoveInvalidationListenerCodec.decodeResponse(msg2).response
    def Replace(self,   key, oldValue, newValue, expiryPolicy, completionId):
        msg=cachecodec.CacheReplaceCodec.encodeRequest( encode.encodestring(self.title), key, oldValue, newValue, expiryPolicy, encode.encodeint32(completionId))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheReplaceCodec.decodeResponse(msg2).response
    def Size(self,  ):
        msg=cachecodec.CacheSizeCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.receivePackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return cachecodec.CacheSizeCodec.decodeResponse(msg2).response