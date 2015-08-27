__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util
import eventconstant
class CacheMessageType:
    CACHE_ADDENTRYLISTENER=0x1501
    CACHE_ADDINVALIDATIONLISTENER=0x1502
    CACHE_CLEAR=0x1503
    CACHE_REMOVEALLKEYS=0x1504
    CACHE_REMOVEALL=0x1505
    CACHE_CONTAINSKEY=0x1506
    CACHE_CREATECONFIG=0x1507
    CACHE_DESTROY=0x1508
    CACHE_ENTRYPROCESSOR=0x1509
    CACHE_GETALL=0x150a
    CACHE_GETANDREMOVE=0x150b
    CACHE_GETANDREPLACE=0x150c
    CACHE_GETCONFIG=0x150d
    CACHE_GET=0x150e
    CACHE_ITERATE=0x150f
    CACHE_LISTENERREGISTRATION=0x1510
    CACHE_LOADALL=0x1511
    CACHE_MANAGEMENTCONFIG=0x1512
    CACHE_PUTIFABSENT=0x1513
    CACHE_PUT=0x1514
    CACHE_REMOVEENTRYLISTENER=0x1515
    CACHE_REMOVEINVALIDATIONLISTENER=0x1516
    CACHE_REMOVE=0x1517
    CACHE_REPLACE=0x1518
    CACHE_SIZE=0x1519
    id=None

    def ___init__(self, messageType):
        self.id = messageType
    
    def id(self):
        return self.id


class CacheAddEntryListenerCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_ADDENTRYLISTENER
    RESPONSE_TYPE = 104
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheAddEntryListenerCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheAddEntryListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheAddEntryListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheAddEntryListenerCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheAddEntryListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheAddEntryListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheAddEntryListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response

        return parameters


    '''************************ EVENTS *************************'''

    @classmethod
    def encodeCacheEvent(cls, type,  keys, completionId):
        clientMessage=ClientMessage()
        clientMessage.setOperationType(eventconstant.EVENT_CACHE)
        clientMessage.setEventFlag()
        clientMessage.set(type)
        clientMessage.set(keys.size())
        for keys_item in keys:
            CacheEventDataCodec.encode(keys_item, clientMessage)
        clientMessage.set(completionId)
        return clientMessage

    class EventHandler:
        def __init__(self,handler):
            self.handler=handler
        def handle(self, clientMessage):
            messageType = clientMessage.getOperationType()
            if (messageType == eventconstant.EVENT_CACHE):
                type=None
                type = clientMessage.extractIntFromPayload()
                keys=None
                keys_size = clientMessage.extractIntFromPayload()
                keys = []
                for i in range(keys_size):
                    keys_item=None
                    keys_item = CacheEventDataCodec.decode(clientMessage)
                    keys.append(keys_item)
                completionId=None
                completionId = clientMessage.extractIntFromPayload()
                self.handler.handle(type, keys, completionId)
                return
class CacheAddInvalidationListenerCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_ADDINVALIDATIONLISTENER
    RESPONSE_TYPE = 104
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheAddInvalidationListenerCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheAddInvalidationListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheAddInvalidationListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheAddInvalidationListenerCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheAddInvalidationListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheAddInvalidationListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheAddInvalidationListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response

        return parameters


    '''************************ EVENTS *************************'''

    @classmethod
    def encodeCacheInvalidationEvent(cls, name,  key,  sourceUuid):
        clientMessage=ClientMessage()
        clientMessage.setOperationType(eventconstant.EVENT_CACHEINVALIDATION)
        clientMessage.setEventFlag()
        clientMessage.set(name)
        key_isNull=None
        if key is None:
            key_isNull = True
            clientMessage.set(key_isNull)
        else:
            key_isNull= False
            clientMessage.set(key_isNull)
            clientMessage.set(key)
        sourceUuid_isNull=None
        if sourceUuid is None:
            sourceUuid_isNull = True
            clientMessage.set(sourceUuid_isNull)
        else:
            sourceUuid_isNull= False
            clientMessage.set(sourceUuid_isNull)
            clientMessage.set(sourceUuid)
        return clientMessage
    @classmethod
    def encodeCacheBatchInvalidationEvent(cls, name,  keys, sourceUuids):
        clientMessage=ClientMessage()
        clientMessage.setOperationType(eventconstant.EVENT_CACHEBATCHINVALIDATION)
        clientMessage.setEventFlag()
        clientMessage.set(name)
        clientMessage.set(keys.size())
        for keys_item in keys:
            clientMessage.set(keys_item)
        sourceUuids_isNull=None
        if sourceUuids is None:
            sourceUuids_isNull = True
            clientMessage.set(sourceUuids_isNull)
        else:
            sourceUuids_isNull= False
            clientMessage.set(sourceUuids_isNull)
            clientMessage.set(sourceUuids.size())
            for sourceUuids_item in sourceUuids:
                clientMessage.set(sourceUuids_item)
        return clientMessage



class EventHandler:
    def __init__(self,handler):
        self.handler=handler
    def handle(self, clientMessage):
        messageType = clientMessage.getOperationType()
        if (messageType == eventconstant.EVENT_CACHEINVALIDATION):
            name=None
            name = clientMessage.extractStringFromPayload()
            key=None
            key_isNull = clientMessage.extractBooleanFromPayload()
            if not key_isNull:
                key = clientMessage.extractBytesFromPayload()
            sourceUuid=None
            sourceUuid_isNull = clientMessage.extractBooleanFromPayload()
            if not sourceUuid_isNull:
                sourceUuid = clientMessage.extractStringFromPayload()
            self.handler.handle(name, key, sourceUuid)
            return
        if (messageType == eventconstant.EVENT_CACHEBATCHINVALIDATION):
            name=None
            name = clientMessage.extractStringFromPayload()
            keys=None
            keys_size = clientMessage.extractIntFromPayload()
            keys = []
            for i in range(keys_size):
                keys_item=None
                keys_item = clientMessage.extractBytesFromPayload()
                keys.append(keys_item)
            sourceUuids=None
            sourceUuids_isNull = clientMessage.extractBooleanFromPayload()
            if not sourceUuids_isNull:
                sourceUuids_size = clientMessage.extractIntFromPayload()
                sourceUuids = []
                for i in range(sourceUuids_size):
                    sourceUuids_item=None
            sourceUuids_item = clientMessage.extractStringFromPayload()
            sourceUuids.append(sourceUuids_item)
            self.handler.handle(name, keys, sourceUuids)
            return
class CacheClearCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_CLEAR
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheClearCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheClearCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheClearCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheClearCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheClearCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheClearCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheClearCodec.ResponseParameters()

        return parameters

class CacheContainsKeyCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_CONTAINSKEY
    RESPONSE_TYPE = 101
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheContainsKeyCodec.REQUEST_TYPE
            self.name=None
            self.key=None
    @classmethod
    def encodeRequest(cls, name, key):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheContainsKeyCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheContainsKeyCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheContainsKeyCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheContainsKeyCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheContainsKeyCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheContainsKeyCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

class CacheCreateConfigCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_CREATECONFIG
    RESPONSE_TYPE = 105
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheCreateConfigCodec.REQUEST_TYPE
            self.cacheConfig=None
            self.createAlsoOnOthers=None
    @classmethod
    def encodeRequest(cls, cacheConfig, createAlsoOnOthers):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheCreateConfigCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheCreateConfigCodec.RETRYABLE)
        clientMessage.set(cacheConfig)
        clientMessage.set(createAlsoOnOthers)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheCreateConfigCodec.RequestParameters()
        cacheConfig=None
        cacheConfig = clientMessage.extractBytesFromPayload()
        parameters.cacheConfig = cacheConfig
        createAlsoOnOthers=None
        createAlsoOnOthers = clientMessage.extractBooleanFromPayload()
        parameters.createAlsoOnOthers = createAlsoOnOthers
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheCreateConfigCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheCreateConfigCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheCreateConfigCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

class CacheDestroyCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_DESTROY
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheDestroyCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheDestroyCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheDestroyCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheDestroyCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheDestroyCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheDestroyCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheDestroyCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
            parameters.response = response

        return parameters

class CacheEntryProcessorCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_ENTRYPROCESSOR
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheEntryProcessorCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.entryProcessor=None
            self.arguments=None
            self.completionId=None
    @classmethod
    def encodeRequest(cls, name, key, entryProcessor, arguments, completionId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheEntryProcessorCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheEntryProcessorCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(entryProcessor)
        clientMessage.set(arguments.size())
        for arguments_item in arguments:
            clientMessage.set(arguments_item)
        clientMessage.set(completionId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheEntryProcessorCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        entryProcessor=None
        entryProcessor = clientMessage.extractBytesFromPayload()
        parameters.entryProcessor = entryProcessor
        arguments=None
        arguments_size = clientMessage.extractIntFromPayload()
        arguments = []
        for i in range(arguments_size):
            arguments_item=None
            arguments_item = clientMessage.extractBytesFromPayload()
            arguments.append(arguments_item)
        parameters.arguments = arguments
        completionId=None
        completionId = clientMessage.extractIntFromPayload()
        parameters.completionId = completionId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheEntryProcessorCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheEntryProcessorCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheEntryProcessorCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

class CacheGetAllCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_GETALL
    RESPONSE_TYPE = 114
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheGetAllCodec.REQUEST_TYPE
            self.name=None
            self.keys=None
            self.expiryPolicy=None
    @classmethod
    def encodeRequest(cls, name, keys, expiryPolicy):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheGetAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheGetAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(keys.size())
        for keys_item in keys:
            clientMessage.set(keys_item)
        expiryPolicy_isNull=None
        if expiryPolicy is None:
            expiryPolicy_isNull = True
            clientMessage.set(expiryPolicy_isNull)
        else:
            expiryPolicy_isNull= False
            clientMessage.set(expiryPolicy_isNull)
        clientMessage.set(expiryPolicy)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheGetAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        keys=None
        keys_size = clientMessage.extractIntFromPayload()
        keys = []
        for i in range(keys_size):
            keys_item=None
            keys_item = clientMessage.extractBytesFromPayload()
            keys.append(keys_item)
        parameters.keys = keys
        expiryPolicy=None
        expiryPolicy_isNull = clientMessage.extractBooleanFromPayload()
        if not expiryPolicy_isNull:
            expiryPolicy = clientMessage.extractBytesFromPayload()
        parameters.expiryPolicy = expiryPolicy
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheGetAllCodec.RESPONSE_TYPE
            self.entrySet=None
    @classmethod
    def encodeResponse(cls, entrySet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheGetAllCodec.RESPONSE_TYPE)
        clientMessage.set(entrySet.size())
        for entrySet_item in entrySet:
            clientMessage.set(entrySet_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheGetAllCodec.ResponseParameters()
        entrySet=None
        entrySet_size = clientMessage.extractIntFromPayload()
        entrySet = []
        for i in range(entrySet_size):
            entrySet_item=None
            entrySet_item = clientMessage.getMapEntry();
            entrySet.append(entrySet_item)
        parameters.entrySet = entrySet

        return parameters

class CacheGetAndRemoveCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_GETANDREMOVE
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheGetAndRemoveCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.completionId=None
    @classmethod
    def encodeRequest(cls, name, key, completionId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheGetAndRemoveCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheGetAndRemoveCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(completionId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheGetAndRemoveCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        completionId=None
        completionId = clientMessage.extractIntFromPayload()
        parameters.completionId = completionId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheGetAndRemoveCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheGetAndRemoveCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheGetAndRemoveCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

class CacheGetAndReplaceCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_GETANDREPLACE
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheGetAndReplaceCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.value=None
            self.expiryPolicy=None
            self.completionId=None
    @classmethod
    def encodeRequest(cls, name, key, value, expiryPolicy, completionId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheGetAndReplaceCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheGetAndReplaceCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(value)
        expiryPolicy_isNull=None
        if expiryPolicy is None:
            expiryPolicy_isNull = True
            clientMessage.set(expiryPolicy_isNull)
        else:
            expiryPolicy_isNull= False
            clientMessage.set(expiryPolicy_isNull)
        clientMessage.set(expiryPolicy)
        clientMessage.set(completionId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheGetAndReplaceCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        expiryPolicy=None
        expiryPolicy_isNull = clientMessage.extractBooleanFromPayload()
        if not expiryPolicy_isNull:
            expiryPolicy = clientMessage.extractBytesFromPayload()
        parameters.expiryPolicy = expiryPolicy
        completionId=None
        completionId = clientMessage.extractIntFromPayload()
        parameters.completionId = completionId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheGetAndReplaceCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheGetAndReplaceCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheGetAndReplaceCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

class CacheGetCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_GET
    RESPONSE_TYPE = 105
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheGetCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.expiryPolicy=None
    @classmethod
    def encodeRequest(cls, name, key, expiryPolicy):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheGetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheGetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        expiryPolicy_isNull=None
        if expiryPolicy is None:
            expiryPolicy_isNull = True
            clientMessage.set(expiryPolicy_isNull)
        else:
            expiryPolicy_isNull= False
            clientMessage.set(expiryPolicy_isNull)
        clientMessage.set(expiryPolicy)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheGetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        expiryPolicy=None
        expiryPolicy_isNull = clientMessage.extractBooleanFromPayload()
        if not expiryPolicy_isNull:
            expiryPolicy = clientMessage.extractBytesFromPayload()
        parameters.expiryPolicy = expiryPolicy
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheGetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheGetCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheGetCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

class CacheGetConfigCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_GETCONFIG
    RESPONSE_TYPE = 105
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheGetConfigCodec.REQUEST_TYPE
            self.name=None
            self.simpleName=None
    @classmethod
    def encodeRequest(cls, name, simpleName):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheGetConfigCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheGetConfigCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(simpleName)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheGetConfigCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        simpleName=None
        simpleName = clientMessage.extractStringFromPayload()
        parameters.simpleName = simpleName
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheGetConfigCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheGetConfigCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheGetConfigCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

class CacheIterateCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_ITERATE
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheIterateCodec.REQUEST_TYPE
            self.name=None
            self.partitionId=None
            self.tableIndex=None
            self.batch=None
    @classmethod
    def encodeRequest(cls, name, partitionId, tableIndex, batch):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheIterateCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheIterateCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(partitionId)
        clientMessage.set(tableIndex)
        clientMessage.set(batch)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheIterateCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        partitionId=None
        partitionId = clientMessage.extractIntFromPayload()
        parameters.partitionId = partitionId
        tableIndex=None
        tableIndex = clientMessage.extractIntFromPayload()
        parameters.tableIndex = tableIndex
        batch=None
        batch = clientMessage.extractIntFromPayload()
        parameters.batch = batch
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheIterateCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheIterateCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheIterateCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

class CacheListenerRegistrationCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_LISTENERREGISTRATION
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheListenerRegistrationCodec.REQUEST_TYPE
            self.name=None
            self.listenerConfig=None
            self.register=None
            self.hostname=None
            self.port=None
    @classmethod
    def encodeRequest(cls, name, listenerConfig, register, hostname, port):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheListenerRegistrationCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheListenerRegistrationCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(listenerConfig)
        clientMessage.set(register)
        clientMessage.set(hostname)
        clientMessage.set(port)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheListenerRegistrationCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        listenerConfig=None
        listenerConfig = clientMessage.extractBytesFromPayload()
        parameters.listenerConfig = listenerConfig
        register=None
        register = clientMessage.extractBooleanFromPayload()
        parameters.register = register
        hostname=None
        hostname = clientMessage.extractStringFromPayload()
        parameters.hostname = hostname
        port=None
        port = clientMessage.extractIntFromPayload()
        parameters.port = port
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheListenerRegistrationCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheListenerRegistrationCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheListenerRegistrationCodec.ResponseParameters()

        return parameters

class CacheLoadAllCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_LOADALL
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheLoadAllCodec.REQUEST_TYPE
            self.name=None
            self.keys=None
            self.replaceExistingValues=None
    @classmethod
    def encodeRequest(cls, name, keys, replaceExistingValues):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheLoadAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheLoadAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(keys.size())
        for keys_item in keys:
            clientMessage.set(keys_item)
        clientMessage.set(replaceExistingValues)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheLoadAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        keys=None
        keys_size = clientMessage.extractIntFromPayload()
        keys = []
        for i in range(keys_size):
            keys_item=None
            keys_item = clientMessage.extractBytesFromPayload()
            keys.append(keys_item)
        parameters.keys = keys
        replaceExistingValues=None
        replaceExistingValues = clientMessage.extractBooleanFromPayload()
        parameters.replaceExistingValues = replaceExistingValues
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheLoadAllCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheLoadAllCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheLoadAllCodec.ResponseParameters()

        return parameters

class CacheManagementConfigCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_MANAGEMENTCONFIG
    RESPONSE_TYPE = 105
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheManagementConfigCodec.REQUEST_TYPE
            self.name=None
            self.isStat=None
            self.enabled=None
            self.hostname=None
            self.port=None
    @classmethod
    def encodeRequest(cls, name, isStat, enabled, hostname, port):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheManagementConfigCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheManagementConfigCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(isStat)
        clientMessage.set(enabled)
        clientMessage.set(hostname)
        clientMessage.set(port)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheManagementConfigCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        isStat=None
        isStat = clientMessage.extractBooleanFromPayload()
        parameters.isStat = isStat
        enabled=None
        enabled = clientMessage.extractBooleanFromPayload()
        parameters.enabled = enabled
        hostname=None
        hostname = clientMessage.extractStringFromPayload()
        parameters.hostname = hostname
        port=None
        port = clientMessage.extractIntFromPayload()
        parameters.port = port
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheManagementConfigCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheManagementConfigCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheManagementConfigCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

class CachePutCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_PUT
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CachePutCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.value=None
            self.expiryPolicy=None
            self.get=None
            self.completionId=None
    @classmethod
    def encodeRequest(cls, name, key, value, expiryPolicy, get, completionId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CachePutCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CachePutCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(value)
        expiryPolicy_isNull=None
        if expiryPolicy is None:
            expiryPolicy_isNull = True
            clientMessage.set(expiryPolicy_isNull)
        else:
            expiryPolicy_isNull= False
            clientMessage.set(expiryPolicy_isNull)
        clientMessage.set(expiryPolicy)
        clientMessage.set(get)
        clientMessage.set(completionId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CachePutCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        expiryPolicy=None
        expiryPolicy_isNull = clientMessage.extractBooleanFromPayload()
        if not expiryPolicy_isNull:
            expiryPolicy = clientMessage.extractBytesFromPayload()
        parameters.expiryPolicy = expiryPolicy
        get=None
        get = clientMessage.extractBooleanFromPayload()
        parameters.get = get
        completionId=None
        completionId = clientMessage.extractIntFromPayload()
        parameters.completionId = completionId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CachePutCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CachePutCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CachePutCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

class CachePutIfAbsentCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_PUTIFABSENT
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CachePutIfAbsentCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.value=None
            self.expiryPolicy=None
            self.completionId=None
    @classmethod
    def encodeRequest(cls, name, key, value, expiryPolicy, completionId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CachePutIfAbsentCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CachePutIfAbsentCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(value)
        expiryPolicy_isNull=None
        if expiryPolicy is None:
            expiryPolicy_isNull = True
            clientMessage.set(expiryPolicy_isNull)
        else:
            expiryPolicy_isNull= False
            clientMessage.set(expiryPolicy_isNull)
        clientMessage.set(expiryPolicy)
        clientMessage.set(completionId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CachePutIfAbsentCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        expiryPolicy=None
        expiryPolicy_isNull = clientMessage.extractBooleanFromPayload()
        if not expiryPolicy_isNull:
            expiryPolicy = clientMessage.extractBytesFromPayload()
        parameters.expiryPolicy = expiryPolicy
        completionId=None
        completionId = clientMessage.extractIntFromPayload()
        parameters.completionId = completionId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CachePutIfAbsentCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CachePutIfAbsentCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CachePutIfAbsentCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
    parameters.response = response

    return parameters

class CacheRemoveAllCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_REMOVEALL
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheRemoveAllCodec.REQUEST_TYPE
            self.name=None
            self.completionId=None
    @classmethod
    def encodeRequest(cls, name, completionId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheRemoveAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheRemoveAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(completionId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheRemoveAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        completionId=None
        completionId = clientMessage.extractIntFromPayload()
        parameters.completionId = completionId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheRemoveAllCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheRemoveAllCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheRemoveAllCodec.ResponseParameters()

        return parameters

class CacheRemoveAllKeysCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_REMOVEALLKEYS
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheRemoveAllKeysCodec.REQUEST_TYPE
            self.name=None
            self.keys=None
            self.completionId=None
    @classmethod
    def encodeRequest(cls, name, keys, completionId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheRemoveAllKeysCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheRemoveAllKeysCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(keys.size())
        for keys_item in keys:
            clientMessage.set(keys_item)
        clientMessage.set(completionId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheRemoveAllKeysCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        keys=None
        keys_size = clientMessage.extractIntFromPayload()
        keys = []
        for i in range(keys_size):
            keys_item=None
            keys_item = clientMessage.extractBytesFromPayload()
            keys.append(keys_item)
        parameters.keys = keys
        completionId=None
        completionId = clientMessage.extractIntFromPayload()
        parameters.completionId = completionId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheRemoveAllKeysCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheRemoveAllKeysCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheRemoveAllKeysCodec.ResponseParameters()

        return parameters

class CacheRemoveCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_REMOVE
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheRemoveCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.currentValue=None
            self.completionId=None
    @classmethod
    def encodeRequest(cls, name, key, currentValue, completionId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheRemoveCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheRemoveCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        currentValue_isNull=None
        if currentValue is None:
            currentValue_isNull = True
            clientMessage.set(currentValue_isNull)
        else:
            currentValue_isNull= False
            clientMessage.set(currentValue_isNull)
        clientMessage.set(currentValue)
        clientMessage.set(completionId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheRemoveCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        currentValue=None
        currentValue_isNull = clientMessage.extractBooleanFromPayload()
        if not currentValue_isNull:
            currentValue = clientMessage.extractBytesFromPayload()
        parameters.currentValue = currentValue
        completionId=None
        completionId = clientMessage.extractIntFromPayload()
        parameters.completionId = completionId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheRemoveCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheRemoveCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheRemoveCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

class CacheRemoveEntryListenerCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_REMOVEENTRYLISTENER
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheRemoveEntryListenerCodec.REQUEST_TYPE
            self.name=None
            self.registrationId=None
    @classmethod
    def encodeRequest(cls, name, registrationId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheRemoveEntryListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheRemoveEntryListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(registrationId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheRemoveEntryListenerCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        registrationId=None
        registrationId = clientMessage.extractStringFromPayload()
        parameters.registrationId = registrationId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheRemoveEntryListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheRemoveEntryListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheRemoveEntryListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

class CacheRemoveInvalidationListenerCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_REMOVEINVALIDATIONLISTENER
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheRemoveInvalidationListenerCodec.REQUEST_TYPE
            self.name=None
            self.registrationId=None
    @classmethod
    def encodeRequest(cls, name, registrationId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheRemoveInvalidationListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheRemoveInvalidationListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(registrationId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheRemoveInvalidationListenerCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        registrationId=None
        registrationId = clientMessage.extractStringFromPayload()
        parameters.registrationId = registrationId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheRemoveInvalidationListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheRemoveInvalidationListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheRemoveInvalidationListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

class CacheReplaceCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_REPLACE
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheReplaceCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.oldValue=None
            self.newValue=None
            self.expiryPolicy=None
            self.completionId=None
    @classmethod
    def encodeRequest(cls, name, key, oldValue, newValue, expiryPolicy, completionId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheReplaceCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheReplaceCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        oldValue_isNull=None
        if oldValue is None:
            oldValue_isNull = True
            clientMessage.set(oldValue_isNull)
        else:
            oldValue_isNull= False
            clientMessage.set(oldValue_isNull)
        clientMessage.set(oldValue)
        clientMessage.set(newValue)
        expiryPolicy_isNull=None
        if expiryPolicy is None:
            expiryPolicy_isNull = True
            clientMessage.set(expiryPolicy_isNull)
        else:
            expiryPolicy_isNull= False
            clientMessage.set(expiryPolicy_isNull)
        clientMessage.set(expiryPolicy)
        clientMessage.set(completionId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheReplaceCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        oldValue=None
        oldValue_isNull = clientMessage.extractBooleanFromPayload()
        if not oldValue_isNull:
            oldValue = clientMessage.extractBytesFromPayload()
        parameters.oldValue = oldValue
        newValue=None
        newValue = clientMessage.extractBytesFromPayload()
        parameters.newValue = newValue
        expiryPolicy=None
        expiryPolicy_isNull = clientMessage.extractBooleanFromPayload()
        if not expiryPolicy_isNull:
            expiryPolicy = clientMessage.extractBytesFromPayload()
        parameters.expiryPolicy = expiryPolicy
        completionId=None
        completionId = clientMessage.extractIntFromPayload()
        parameters.completionId = completionId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheReplaceCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheReplaceCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheReplaceCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

class CacheSizeCodec:
    REQUEST_TYPE = CacheMessageType.CACHE_SIZE
    RESPONSE_TYPE = 102
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = CacheSizeCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheSizeCodec.REQUEST_TYPE)
        clientMessage.setRetryable(CacheSizeCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = CacheSizeCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = CacheSizeCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(CacheSizeCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=CacheSizeCodec.ResponseParameters()
        response=None
        response = clientMessage.extractIntFromPayload()
        parameters.response = response

        return parameters

class CacheEventDataCodec():
    @classmethod
    def decode(cls, clientMessage):
        typeId=clientMessage.extractIntFromPayload()
        mystr=clientMessage.extractStringFromPayload()
        key=clientMessage.extractBytesFromPayload()
        isNull=clientMessage.extractBooleanFromPayload()
        value=None
        if not isNull:
            value=clientMessage.extractBytesFromPayload()
