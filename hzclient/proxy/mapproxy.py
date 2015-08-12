__author__ = 'jonathanbrodie'
from hzclient.codec import mapcodec
from hzclient.codec import proxycodec
from hzclient.clientmessage import ClientMessage
from util import encode
class MapProxy(object):
    def __init__(self,title,connfamily):
        self.title=title
        self.connection=connfamily
        firstpack=proxycodec.createProxy(self.title, "hz:impl:mapService")
        self.connection.sendPackage(firstpack.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(firstpack.correlation,True)
        newresponse=ClientMessage.decodeMessage(response)
        print newresponse.payload
        if response is not None:
            print "Initialized and connected proxy!"
        else:
            print "Unable to connect to server."

    def AddEntryListener(self,   includeValue, eventhandler):
        msg=mapcodec.MapAddEntryListenerCodec.encodeRequest( encode.encodestring(self.title), includeValue)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        self.connection.eventregistry[correlationid]=mapcodec.MapAddEntryListenerCodec.EventHandler(eventhandler)
        return mapcodec.MapAddEntryListenerCodec.decodeResponse(msg2)
    def AddEntryListenerToKey(self,   key, includeValue, eventhandler):
        msg=mapcodec.MapAddEntryListenerToKeyCodec.encodeRequest( self.title, key, includeValue)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        self.connection.eventregistry[correlationid]=mapcodec.MapAddEntryListenerToKeyCodec.EventHandler(eventhandler)
        return mapcodec.MapAddEntryListenerToKeyCodec.decodeResponse(msg2)
    def AddEntryListenerToKeyWithPredicate(self,   key, predicate, includeValue, eventhandler):
        msg=mapcodec.MapAddEntryListenerToKeyWithPredicateCodec.encodeRequest( self.title, key, predicate, includeValue)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        self.connection.eventregistry[correlationid]=mapcodec.MapAddEntryListenerToKeyWithPredicateCodec.EventHandler(eventhandler)
        return mapcodec.MapAddEntryListenerToKeyWithPredicateCodec.decodeResponse(msg2)
    def AddEntryListenerWithPredicate(self,   predicate, includeValue, eventhandler):
        msg=mapcodec.MapAddEntryListenerWithPredicateCodec.encodeRequest( self.title, predicate, includeValue)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        self.connection.eventregistry[correlationid]=mapcodec.MapAddEntryListenerWithPredicateCodec.EventHandler(eventhandler)
        return mapcodec.MapAddEntryListenerWithPredicateCodec.decodeResponse(msg2)
    def AddIndex(self,   attribute, ordered):
        msg=mapcodec.MapAddIndexCodec.encodeRequest( self.title, attribute, ordered)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapAddIndexCodec.decodeResponse(msg2)
    def AddInterceptor(self,   interceptor):
        msg=mapcodec.MapAddInterceptorCodec.encodeRequest( self.title, interceptor)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapAddInterceptorCodec.decodeResponse(msg2)
    def AddNearCacheEntryListener(self,   includeValue, eventhandler):
        msg=mapcodec.MapAddNearCacheEntryListenerCodec.encodeRequest( self.title, includeValue)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        self.connection.eventregistry[correlationid]=mapcodec.MapAddNearCacheEntryListenerCodec.EventHandler(eventhandler)
        return mapcodec.MapAddNearCacheEntryListenerCodec.decodeResponse(msg2)
    def AddPartitionLostListener(self,   eventhandler):
        msg=mapcodec.MapAddPartitionLostListenerCodec.encodeRequest( self.title)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        self.connection.eventregistry[correlationid]=mapcodec.MapAddPartitionLostListenerCodec.EventHandler(eventhandler)
        return mapcodec.MapAddPartitionLostListenerCodec.decodeResponse(msg2)
    def Clear(self,  ):
        msg=mapcodec.MapClearCodec.encodeRequest( self.title)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapClearCodec.decodeResponse(msg2)
    def ContainsKey(self,   key, threadId):
        msg=mapcodec.MapContainsKeyCodec.encodeRequest( self.title, key, threadId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapContainsKeyCodec.decodeResponse(msg2)
    def ContainsValue(self,   value):
        msg=mapcodec.MapContainsValueCodec.encodeRequest( self.title, value)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapContainsValueCodec.decodeResponse(msg2)
    def Delete(self,   key, threadId):
        msg=mapcodec.MapDeleteCodec.encodeRequest( self.title, key, threadId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapDeleteCodec.decodeResponse(msg2)
    def EntriesWithPagingPredicate(self,   predicate):
        msg=mapcodec.MapEntriesWithPagingPredicateCodec.encodeRequest( self.title, predicate)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapEntriesWithPagingPredicateCodec.decodeResponse(msg2)
    def EntriesWithPredicate(self,   predicate):
        msg=mapcodec.MapEntriesWithPredicateCodec.encodeRequest( self.title, predicate)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapEntriesWithPredicateCodec.decodeResponse(msg2)
    def EntrySet(self,  ):
        msg=mapcodec.MapEntrySetCodec.encodeRequest( self.title)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapEntrySetCodec.decodeResponse(msg2)
    def EvictAll(self,  ):
        msg=mapcodec.MapEvictAllCodec.encodeRequest( self.title)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapEvictAllCodec.decodeResponse(msg2)
    def Evict(self,   key, threadId):
        msg=mapcodec.MapEvictCodec.encodeRequest( self.title, key, threadId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapEvictCodec.decodeResponse(msg2)
    def ExecuteOnAllKeys(self,   entryProcessor):
        msg=mapcodec.MapExecuteOnAllKeysCodec.encodeRequest( self.title, entryProcessor)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapExecuteOnAllKeysCodec.decodeResponse(msg2)
    def ExecuteOnKey(self,   entryProcessor, key):
        msg=mapcodec.MapExecuteOnKeyCodec.encodeRequest( self.title, entryProcessor, key)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapExecuteOnKeyCodec.decodeResponse(msg2)
    def ExecuteOnKeys(self,   entryProcessor, keys):
        msg=mapcodec.MapExecuteOnKeysCodec.encodeRequest( self.title, entryProcessor, keys)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapExecuteOnKeysCodec.decodeResponse(msg2)
    def ExecuteWithPredicate(self,   entryProcessor, predicate):
        msg=mapcodec.MapExecuteWithPredicateCodec.encodeRequest( self.title, entryProcessor, predicate)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapExecuteWithPredicateCodec.decodeResponse(msg2)
    def Flush(self,  ):
        msg=mapcodec.MapFlushCodec.encodeRequest( self.title)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapFlushCodec.decodeResponse(msg2)
    def ForceUnlock(self,   key):
        msg=mapcodec.MapForceUnlockCodec.encodeRequest( self.title, key)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapForceUnlockCodec.decodeResponse(msg2)
    def GetAll(self,   keys):
        msg=mapcodec.MapGetAllCodec.encodeRequest( self.title, keys)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapGetAllCodec.decodeResponse(msg2)
    def GetAsync(self,   key, threadId):
        msg=mapcodec.MapGetAsyncCodec.encodeRequest( self.title, key, threadId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapGetAsyncCodec.decodeResponse(msg2)
    def Get(self,   key, threadId):
        msg=mapcodec.MapGetCodec.encodeRequest( self.title, key, threadId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapGetCodec.decodeResponse(msg2)
    def GetEntryView(self,   key, threadId):
        msg=mapcodec.MapGetEntryViewCodec.encodeRequest( self.title, key, threadId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapGetEntryViewCodec.decodeResponse(msg2)
    def IsEmpty(self,  ):
        msg=mapcodec.MapIsEmptyCodec.encodeRequest( self.title)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapIsEmptyCodec.decodeResponse(msg2)
    def IsLocked(self,   key):
        msg=mapcodec.MapIsLockedCodec.encodeRequest( self.title, key)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapIsLockedCodec.decodeResponse(msg2)
    def KeySet(self):
        msg=mapcodec.MapKeySetCodec.encodeRequest(self.title)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapKeySetCodec.decodeResponse(msg2)
    def KeySetWithPagingPredicate(self,   predicate):
        msg=mapcodec.MapKeySetWithPagingPredicateCodec.encodeRequest( self.title, predicate)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapKeySetWithPagingPredicateCodec.decodeResponse(msg2)
    def KeySetWithPredicate(self,   predicate):
        msg=mapcodec.MapKeySetWithPredicateCodec.encodeRequest( self.title, predicate)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapKeySetWithPredicateCodec.decodeResponse(msg2)
    def LoadAll(self,   replaceExistingValues):
        msg=mapcodec.MapLoadAllCodec.encodeRequest( self.title, replaceExistingValues)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapLoadAllCodec.decodeResponse(msg2)
    def LoadGivenKeys(self,   keys, replaceExistingValues):
        msg=mapcodec.MapLoadGivenKeysCodec.encodeRequest( self.title, keys, replaceExistingValues)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapLoadGivenKeysCodec.decodeResponse(msg2)
    def Lock(self,   key, threadId, ttl):
        msg=mapcodec.MapLockCodec.encodeRequest( self.title, key, threadId, ttl)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapLockCodec.decodeResponse(msg2)
    def PutAll(self,   entries):
        msg=mapcodec.MapPutAllCodec.encodeRequest( self.title, entries)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapPutAllCodec.decodeResponse(msg2)
    def PutAsync(self,   key, value, threadId, ttl):
        msg=mapcodec.MapPutAsyncCodec.encodeRequest( self.title, key, value, threadId, ttl)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapPutAsyncCodec.decodeResponse(msg2)
    def Put(self,   key, value, threadId, ttl):
        msg=mapcodec.MapPutCodec.encodeRequest( self.title, key, value, threadId, ttl)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapPutCodec.decodeResponse(msg2)
    def PutIfAbsent(self,   key, value, threadId, ttl):
        msg=mapcodec.MapPutIfAbsentCodec.encodeRequest( self.title, key, value, threadId, ttl)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapPutIfAbsentCodec.decodeResponse(msg2)
    def PutTransient(self,   key, value, threadId, ttl):
        msg=mapcodec.MapPutTransientCodec.encodeRequest( self.title, key, value, threadId, ttl)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapPutTransientCodec.decodeResponse(msg2)
    def RemoveAsync(self,   key, threadId):
        msg=mapcodec.MapRemoveAsyncCodec.encodeRequest( self.title, key, threadId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapRemoveAsyncCodec.decodeResponse(msg2)
    def Remove(self,   key, threadId):
        msg=mapcodec.MapRemoveCodec.encodeRequest( self.title, key, threadId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapRemoveCodec.decodeResponse(msg2)
    def RemoveEntryListener(self,   registrationId):
        msg=mapcodec.MapRemoveEntryListenerCodec.encodeRequest( self.title, registrationId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapRemoveEntryListenerCodec.decodeResponse(msg2)
    def RemoveIfSame(self,   key, value, threadId):
        msg=mapcodec.MapRemoveIfSameCodec.encodeRequest( self.title, key, value, threadId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapRemoveIfSameCodec.decodeResponse(msg2)
    def RemoveInterceptor(self,   id):
        msg=mapcodec.MapRemoveInterceptorCodec.encodeRequest( self.title, id)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapRemoveInterceptorCodec.decodeResponse(msg2)
    def RemovePartitionLostListener(self,   registrationId):
        msg=mapcodec.MapRemovePartitionLostListenerCodec.encodeRequest( self.title, registrationId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapRemovePartitionLostListenerCodec.decodeResponse(msg2)
    def Replace(self,   key, value, threadId):
        msg=mapcodec.MapReplaceCodec.encodeRequest( self.title, key, value, threadId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapReplaceCodec.decodeResponse(msg2)
    def ReplaceIfSame(self,   key, testValue, value, threadId):
        msg=mapcodec.MapReplaceIfSameCodec.encodeRequest( self.title, key, testValue, value, threadId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapReplaceIfSameCodec.decodeResponse(msg2)
    def Set(self,   key, value, threadId, ttl):
        msg=mapcodec.MapSetCodec.encodeRequest( self.title, key, value, threadId, ttl)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapSetCodec.decodeResponse(msg2)
    def Size(self,  ):
        msg=mapcodec.MapSizeCodec.encodeRequest( encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapSizeCodec.decodeResponse(msg2)
    def SubmitToKey(self,   entryProcessor, key):
        msg=mapcodec.MapSubmitToKeyCodec.encodeRequest( self.title, entryProcessor, key)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapSubmitToKeyCodec.decodeResponse(msg2)
    def TryLock(self,   key, threadId, lease, timeout):
        msg=mapcodec.MapTryLockCodec.encodeRequest( self.title, key, threadId, lease, timeout)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapTryLockCodec.decodeResponse(msg2)
    def TryPut(self,   key, value, threadId, timeout):
        msg=mapcodec.MapTryPutCodec.encodeRequest( self.title, key, value, threadId, timeout)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapTryPutCodec.decodeResponse(msg2)
    def TryRemove(self,   key, threadId, timeout):
        msg=mapcodec.MapTryRemoveCodec.encodeRequest( self.title, key, threadId, timeout)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapTryRemoveCodec.decodeResponse(msg2)
    def Unlock(self,   key, threadId):
        msg=mapcodec.MapUnlockCodec.encodeRequest( self.title, key, threadId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapUnlockCodec.decodeResponse(msg2)
    def Values(self):
        msg=mapcodec.MapValuesCodec.encodeRequest(self.title)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapValuesCodec.decodeResponse(msg2)
    def ValuesWithPagingPredicate(self,   predicate):
        msg=mapcodec.MapValuesWithPagingPredicateCodec.encodeRequest( self.title, predicate)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapValuesWithPagingPredicateCodec.decodeResponse(msg2)
    def ValuesWithPredicate(self,   predicate):
        msg=mapcodec.MapValuesWithPredicateCodec.encodeRequest( self.title, predicate)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)
        return mapcodec.MapValuesWithPredicateCodec.decodeResponse(msg2)