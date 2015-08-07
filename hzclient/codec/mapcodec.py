__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util
import eventconstant
class MapMessageType:
    MAP_PUT=0x0101
    MAP_GET=0x0102
    MAP_REMOVE=0x0103
    MAP_REPLACE=0x0104
    MAP_REPLACEIFSAME=0x0105
    MAP_PUTASYNC=0x0106
    MAP_GETASYNC=0x0107
    MAP_REMOVEASYNC=0x0108
    MAP_CONTAINSKEY=0x0109
    MAP_CONTAINSVALUE=0x010a
    MAP_REMOVEIFSAME=0x010b
    MAP_DELETE=0x010c
    MAP_FLUSH=0x010d
    MAP_TRYREMOVE=0x010e
    MAP_TRYPUT=0x010f
    MAP_PUTTRANSIENT=0x0110
    MAP_PUTIFABSENT=0x0111
    MAP_SET=0x0112
    MAP_LOCK=0x0113
    MAP_TRYLOCK=0x0114
    MAP_ISLOCKED=0x0115
    MAP_UNLOCK=0x0116
    MAP_ADDINTERCEPTOR=0x0117
    MAP_REMOVEINTERCEPTOR=0x0118
    MAP_ADDENTRYLISTENERTOKEYWITHPREDICATE=0x0119
    MAP_ADDENTRYLISTENERWITHPREDICATE=0x011a
    MAP_ADDENTRYLISTENERTOKEY=0x011b
    MAP_ADDENTRYLISTENER=0x011c
    MAP_ADDNEARCACHEENTRYLISTENER=0x011d
    MAP_REMOVEENTRYLISTENER=0x011e
    MAP_ADDPARTITIONLOSTLISTENER=0x011f
    MAP_REMOVEPARTITIONLOSTLISTENER=0x0120
    MAP_GETENTRYVIEW=0x0121
    MAP_EVICT=0x0122
    MAP_EVICTALL=0x0123
    MAP_LOADALL=0x0124
    MAP_LOADGIVENKEYS=0x0125
    MAP_KEYSET=0x0126
    MAP_GETALL=0x0127
    MAP_VALUES=0x0128
    MAP_ENTRYSET=0x0129
    MAP_KEYSETWITHPREDICATE=0x012a
    MAP_VALUESWITHPREDICATE=0x012b
    MAP_ENTRIESWITHPREDICATE=0x012c
    MAP_ADDINDEX=0x012d
    MAP_SIZE=0x012e
    MAP_ISEMPTY=0x012f
    MAP_PUTALL=0x0130
    MAP_CLEAR=0x0131
    MAP_EXECUTEONKEY=0x0132
    MAP_SUBMITTOKEY=0x0133
    MAP_EXECUTEONALLKEYS=0x0134
    MAP_EXECUTEWITHPREDICATE=0x0135
    MAP_EXECUTEONKEYS=0x0136
    MAP_FORCEUNLOCK=0x0137
    MAP_KEYSETWITHPAGINGPREDICATE=0x0138
    MAP_VALUESWITHPAGINGPREDICATE=0x0139
    MAP_ENTRIESWITHPAGINGPREDICATE=0x013a

    def ___init__(self, messageType):
        self.id = messageType

    def id(self):
        return self.id
'''
PUT
'''
class MapPutCodec:
    REQUEST_TYPE = MapMessageType.MAP_PUT
    RESPONSE_TYPE = 105
    RETRYABLE = False
    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = MapPutCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.value=None
            self.threadId=None
            self.ttl=None
    @classmethod
    def encodeRequest(cls, name, key, value, threadId, ttl):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapPutCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapPutCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(value)
        clientMessage.set(threadId)
        clientMessage.set(ttl)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapPutCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        ttl=None
        ttl = clientMessage.extractLongFromPayload()
        parameters.ttl = ttl
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = MapPutCodec.RESPONSE_TYPE
            self.response=None

    @classmethod
    def encodeResponse(cls,response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapPutCodec.RESPONSE_TYPE)
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
        parameters=MapPutCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response
        return parameters



'''
GET
'''
class MapGetCodec:
    REQUEST_TYPE = MapMessageType.MAP_GET
    RESPONSE_TYPE = 105
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = MapGetCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, key, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapGetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapGetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapGetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = MapGetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls,response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapGetCodec.RESPONSE_TYPE)
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
        parameters=MapGetCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters



'''
REMOVE
'''
class MapRemoveCodec:
    REQUEST_TYPE = MapMessageType.MAP_REMOVE
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = MapRemoveCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, key, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapRemoveCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapRemoveCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapRemoveCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = MapRemoveCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls,response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapRemoveCodec.RESPONSE_TYPE)
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
        parameters=MapRemoveCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters


'''
REPLACE
'''
class MapReplaceCodec:
    REQUEST_TYPE = MapMessageType.MAP_REPLACE
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = MapReplaceCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.value=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, key, value, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapReplaceCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapReplaceCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(value)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapReplaceCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = MapReplaceCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls,response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapReplaceCodec.RESPONSE_TYPE)
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
        parameters=MapReplaceCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters



'''
REPLACEIFSAME
'''
class MapReplaceIfSameCodec:
    REQUEST_TYPE = MapMessageType.MAP_REPLACEIFSAME
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = MapReplaceIfSameCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.testValue=None
            self.value=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, key, testValue, value, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapReplaceIfSameCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapReplaceIfSameCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(testValue)
        clientMessage.set(value)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapReplaceIfSameCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        testValue=None
        testValue = clientMessage.extractBytesFromPayload()
        parameters.testValue = testValue
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = MapReplaceIfSameCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapReplaceIfSameCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapReplaceIfSameCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters



'''
PUTASYNC
'''
class MapPutAsyncCodec:
    REQUEST_TYPE = MapMessageType.MAP_PUTASYNC
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = MapPutAsyncCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.value=None
            self.threadId=None
            self.ttl=None
    @classmethod
    def encodeRequest(cls, name, key, value, threadId, ttl):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapPutAsyncCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapPutAsyncCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(value)
        clientMessage.set(threadId)
        clientMessage.set(ttl)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapPutAsyncCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        ttl=None
        ttl = clientMessage.extractLongFromPayload()
        parameters.ttl = ttl
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = MapPutAsyncCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls,response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapPutAsyncCodec.RESPONSE_TYPE)
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
        parameters=MapPutAsyncCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters



'''
GETASYNC
'''
class MapGetAsyncCodec:
    REQUEST_TYPE = MapMessageType.MAP_GETASYNC
    RESPONSE_TYPE = 105
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = MapGetAsyncCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, key, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapGetAsyncCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapGetAsyncCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapGetAsyncCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = MapGetAsyncCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls,response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapGetAsyncCodec.RESPONSE_TYPE)
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
        parameters=MapGetAsyncCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters



'''
REMOVEASYNC
'''
class MapRemoveAsyncCodec:
    REQUEST_TYPE = MapMessageType.MAP_REMOVEASYNC
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapRemoveAsyncCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, key, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapRemoveAsyncCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapRemoveAsyncCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapRemoveAsyncCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = MapRemoveAsyncCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls,response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapRemoveAsyncCodec.RESPONSE_TYPE)
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
        parameters=MapRemoveAsyncCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

'''
CONTAINSKEY
'''
class MapContainsKeyCodec:
    REQUEST_TYPE = MapMessageType.MAP_CONTAINSKEY
    RESPONSE_TYPE = 101
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapContainsKeyCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, key, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapContainsKeyCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapContainsKeyCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapContainsKeyCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapContainsKeyCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapContainsKeyCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapContainsKeyCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters



'''
CONTAINSVALUE
'''
class MapContainsValueCodec:
    REQUEST_TYPE = MapMessageType.MAP_CONTAINSVALUE
    RESPONSE_TYPE = 101
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapContainsValueCodec.REQUEST_TYPE
            self.name=None
            self.value=None
    @classmethod
    def encodeRequest(cls, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapContainsValueCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapContainsValueCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapContainsValueCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapContainsValueCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapContainsValueCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapContainsValueCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


'''
REMOVEIFSAME
'''
class MapRemoveIfSameCodec:
    REQUEST_TYPE = MapMessageType.MAP_REMOVEIFSAME
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapRemoveIfSameCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.value=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, key, value, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapRemoveIfSameCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapRemoveIfSameCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(value)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapRemoveIfSameCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapRemoveIfSameCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls,response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapRemoveIfSameCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapRemoveIfSameCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


'''
DELETE
'''
class MapDeleteCodec:
    REQUEST_TYPE = MapMessageType.MAP_DELETE
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapDeleteCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, key, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapDeleteCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapDeleteCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapDeleteCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapDeleteCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapDeleteCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapDeleteCodec.ResponseParameters()

        return parameters

'''
FLUSH
'''
class MapFlushCodec:
    REQUEST_TYPE = MapMessageType.MAP_FLUSH
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapFlushCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapFlushCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapFlushCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapFlushCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapFlushCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapFlushCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapFlushCodec.ResponseParameters()

        return parameters


'''
TRYREMOVE
'''
class MapTryRemoveCodec:
    REQUEST_TYPE = MapMessageType.MAP_TRYREMOVE
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapTryRemoveCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.threadId=None
            self.timeout=None
    @classmethod
    def encodeRequest(cls, name, key, threadId, timeout):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapTryRemoveCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapTryRemoveCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(threadId)
        clientMessage.set(timeout)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapTryRemoveCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        timeout=None
        timeout = clientMessage.extractLongFromPayload()
        parameters.timeout = timeout
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapTryRemoveCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapTryRemoveCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapTryRemoveCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

'''
TRYPUT
'''
class MapTryPutCodec:
    REQUEST_TYPE = MapMessageType.MAP_TRYPUT
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapTryPutCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.value=None
            self.threadId=None
            self.timeout=None
    @classmethod
    def encodeRequest(cls, name, key, value, threadId, timeout):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapTryPutCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapTryPutCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(value)
        clientMessage.set(threadId)
        clientMessage.set(timeout)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapTryPutCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        timeout=None
        timeout = clientMessage.extractLongFromPayload()
        parameters.timeout = timeout
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapTryPutCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapTryPutCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapTryPutCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters



'''
PUTTRANSIENT
'''
class MapPutTransientCodec:
    REQUEST_TYPE = MapMessageType.MAP_PUTTRANSIENT
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapPutTransientCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.value=None
            self.threadId=None
            self.ttl=None
    @classmethod
    def encodeRequest(cls, name, key, value, threadId, ttl):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapPutTransientCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapPutTransientCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(value)
        clientMessage.set(threadId)
        clientMessage.set(ttl)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapPutTransientCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        ttl=None
        ttl = clientMessage.extractLongFromPayload()
        parameters.ttl = ttl
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapPutTransientCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapPutTransientCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapPutTransientCodec.ResponseParameters()

        return parameters


'''
PUTIFABSENT
'''
class MapPutIfAbsentCodec:
    REQUEST_TYPE = MapMessageType.MAP_PUTIFABSENT
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapPutIfAbsentCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.value=None
            self.threadId=None
            self.ttl=None
    @classmethod
    def encodeRequest(cls, name, key, value, threadId, ttl):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapPutIfAbsentCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapPutIfAbsentCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(value)
        clientMessage.set(threadId)
        clientMessage.set(ttl)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapPutIfAbsentCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        ttl=None
        ttl = clientMessage.extractLongFromPayload()
        parameters.ttl = ttl
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapPutIfAbsentCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapPutIfAbsentCodec.RESPONSE_TYPE)
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
        parameters=MapPutIfAbsentCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
            parameters.response = response
        return parameters



'''
SET
'''
class MapSetCodec:
    REQUEST_TYPE = MapMessageType.MAP_SET
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapSetCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.value=None
            self.threadId=None
            self.ttl=None
    @classmethod
    def encodeRequest(cls, name, key, value, threadId, ttl):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapSetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapSetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(value)
        clientMessage.set(threadId)
        clientMessage.set(ttl)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapSetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        ttl=None
        ttl = clientMessage.extractLongFromPayload()
        parameters.ttl = ttl
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapSetCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapSetCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapSetCodec.ResponseParameters()

        return parameters


'''
LOCK
'''
class MapLockCodec:
    REQUEST_TYPE = MapMessageType.MAP_LOCK
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapLockCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.threadId=None
            self.ttl=None
    @classmethod
    def encodeRequest(cls, name, key, threadId, ttl):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapLockCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapLockCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(threadId)
        clientMessage.set(ttl)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapLockCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        ttl=None
        ttl = clientMessage.extractLongFromPayload()
        parameters.ttl = ttl
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapLockCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapLockCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapLockCodec.ResponseParameters()

        return None



'''
TRYLOCK
'''
class MapTryLockCodec:
    REQUEST_TYPE = MapMessageType.MAP_TRYLOCK
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapTryLockCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.threadId=None
            self.lease=None
            self.timeout=None
    @classmethod
    def encodeRequest(cls, name, key, threadId, lease, timeout):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapTryLockCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapTryLockCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(threadId)
        clientMessage.set(lease)
        clientMessage.set(timeout)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapTryLockCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        lease=None
        lease = clientMessage.extractLongFromPayload()
        parameters.lease = lease
        timeout=None
        timeout = clientMessage.extractLongFromPayload()
        parameters.timeout = timeout
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapTryLockCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapTryLockCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapTryLockCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters



'''
ISLOCKED
'''
class MapIsLockedCodec:
    REQUEST_TYPE = MapMessageType.MAP_ISLOCKED
    RESPONSE_TYPE = 101
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapIsLockedCodec.REQUEST_TYPE
            self.name=None
            self.key=None
    @classmethod
    def encodeRequest(cls, name, key):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapIsLockedCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapIsLockedCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapIsLockedCodec.RequestParameters()
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
            self.TYPE = MapIsLockedCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapIsLockedCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapIsLockedCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters



'''
UNLOCK
'''
class MapUnlockCodec:
    REQUEST_TYPE = MapMessageType.MAP_UNLOCK
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapUnlockCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, key, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapUnlockCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapUnlockCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapUnlockCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapUnlockCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapUnlockCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapUnlockCodec.ResponseParameters()

        return parameters


'''
ADDINTERCEPTOR
'''
class MapAddInterceptorCodec:
    REQUEST_TYPE = MapMessageType.MAP_ADDINTERCEPTOR
    RESPONSE_TYPE = 104
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapAddInterceptorCodec.REQUEST_TYPE
            self.name=None
            self.interceptor=None
    @classmethod
    def encodeRequest(cls, name, interceptor):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddInterceptorCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapAddInterceptorCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(interceptor)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapAddInterceptorCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        interceptor=None
        interceptor = clientMessage.extractBytesFromPayload()
        parameters.interceptor = interceptor
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapAddInterceptorCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddInterceptorCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapAddInterceptorCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response

        return parameters


'''
REMOVEINTERCEPTOR
'''
class MapRemoveInterceptorCodec:
    REQUEST_TYPE = MapMessageType.MAP_REMOVEINTERCEPTOR
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapRemoveInterceptorCodec.REQUEST_TYPE
            self.name=None
            self.id=None
    @classmethod
    def encodeRequest(cls, name, id):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapRemoveInterceptorCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapRemoveInterceptorCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(id)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapRemoveInterceptorCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        id=None
        id = clientMessage.extractStringFromPayload()
        parameters.id = id
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapRemoveInterceptorCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapRemoveInterceptorCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapRemoveInterceptorCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


'''
ADDENTRYLISTENERTOKEYWITHPREDICATE
'''
class MapAddEntryListenerToKeyWithPredicateCodec:
    REQUEST_TYPE = MapMessageType.MAP_ADDENTRYLISTENERTOKEYWITHPREDICATE
    RESPONSE_TYPE = 104
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapAddEntryListenerToKeyWithPredicateCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.predicate=None
            self.includeValue=None
    @classmethod
    def encodeRequest(cls, name, key, predicate, includeValue):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddEntryListenerToKeyWithPredicateCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapAddEntryListenerToKeyWithPredicateCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(predicate)
        clientMessage.set(includeValue)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapAddEntryListenerToKeyWithPredicateCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        predicate=None
        predicate = clientMessage.extractBytesFromPayload()
        parameters.predicate = predicate
        includeValue=None
        includeValue = clientMessage.extractBooleanFromPayload()
        parameters.includeValue = includeValue
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapAddEntryListenerToKeyWithPredicateCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddEntryListenerToKeyWithPredicateCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapAddEntryListenerToKeyWithPredicateCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response

        return parameters


    '''************************ EVENTS *************************'''

    @classmethod
    def encodeEntryEvent(cls, key, value, oldValue, mergingValue, eventType, uuid, numberOfAffectedEntries):
        clientMessage=ClientMessage()
        clientMessage.setOperationType(eventconstant.EVENT_ENTRY)
        clientMessage.setEventFlag()
        key_isNull=None
        if key is None:
            key_isNull = True
            clientMessage.set(key_isNull)
        else:
            key_isNull= False
            clientMessage.set(key_isNull)
        clientMessage.set(key)
        value_isNull=None
        if value is None:
            value_isNull = True
            clientMessage.set(value_isNull)
        else:
            value_isNull= False
            clientMessage.set(value_isNull)
        clientMessage.set(value)
        oldValue_isNull=None
        if oldValue is None:
            oldValue_isNull = True
            clientMessage.set(oldValue_isNull)
        else:
            oldValue_isNull= False
            clientMessage.set(oldValue_isNull)
        clientMessage.set(oldValue)
        mergingValue_isNull=None
        if mergingValue is None:
            mergingValue_isNull = True
            clientMessage.set(mergingValue_isNull)
        else:
            mergingValue_isNull= False
            clientMessage.set(mergingValue_isNull)
            clientMessage.set(mergingValue)
        clientMessage.set(eventType)
        clientMessage.set(uuid)
        clientMessage.set(numberOfAffectedEntries)
        return clientMessage

    class EventHandler:
        def __init__(self,handler):
            self.handler=handler
        def handle(self, clientMessage):
            messageType = clientMessage.getOperationType()
            if (messageType == eventconstant.EVENT_ENTRY):
                key=None
                key_isNull = clientMessage.extractBooleanFromPayload()
                if not key_isNull:
                    key = clientMessage.extractBytesFromPayload()
                value=None
                value_isNull = clientMessage.extractBooleanFromPayload()
                if not value_isNull:
                    value = clientMessage.extractBytesFromPayload()
                oldValue=None
                oldValue_isNull = clientMessage.extractBooleanFromPayload()
                if not oldValue_isNull:
                    oldValue = clientMessage.extractBytesFromPayload()
                mergingValue=None
                mergingValue_isNull = clientMessage.extractBooleanFromPayload()
                if not mergingValue_isNull:
                    mergingValue = clientMessage.extractBytesFromPayload()
                eventType=None
                eventType = clientMessage.extractIntFromPayload()
                uuid=None
                uuid = clientMessage.extractStringFromPayload()
                numberOfAffectedEntries=None
                numberOfAffectedEntries = clientMessage.extractIntFromPayload()
                self.handler.handle(key, value, oldValue, mergingValue, eventType, uuid, numberOfAffectedEntries)
                return


'''
ADDENTRYLISTENERWITHPREDICATE
'''
class MapAddEntryListenerWithPredicateCodec:
    REQUEST_TYPE = MapMessageType.MAP_ADDENTRYLISTENERWITHPREDICATE
    RESPONSE_TYPE = 104
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapAddEntryListenerWithPredicateCodec.REQUEST_TYPE
            self.name=None
            self.predicate=None
            self.includeValue=None
    @classmethod
    def encodeRequest(cls, name, predicate, includeValue):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddEntryListenerWithPredicateCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapAddEntryListenerWithPredicateCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(predicate)
        clientMessage.set(includeValue)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapAddEntryListenerWithPredicateCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        predicate=None
        predicate = clientMessage.extractBytesFromPayload()
        parameters.predicate = predicate
        includeValue=None
        includeValue = clientMessage.extractBooleanFromPayload()
        parameters.includeValue = includeValue
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapAddEntryListenerWithPredicateCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddEntryListenerWithPredicateCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapAddEntryListenerWithPredicateCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response

        return parameters


    '''************************ EVENTS *************************'''

    @classmethod
    def encodeEntryEvent(cls,key, value, oldValue, mergingValue,eventType, uuid, numberOfAffectedEntries):
        clientMessage=ClientMessage()
        clientMessage.setOperationType(eventconstant.EVENT_ENTRY)
        clientMessage.setEventFlag()
        key_isNull=None
        if key is None:
            key_isNull = True
            clientMessage.set(key_isNull)
        else:
            key_isNull= False
            clientMessage.set(key_isNull)
        clientMessage.set(key)
        value_isNull=None
        if value is None:
            value_isNull = True
            clientMessage.set(value_isNull)
        else:
            value_isNull= False
            clientMessage.set(value_isNull)
        clientMessage.set(value)
        oldValue_isNull=None
        if oldValue is None:
            oldValue_isNull = True
            clientMessage.set(oldValue_isNull)
        else:
            oldValue_isNull= False
            clientMessage.set(oldValue_isNull)
        clientMessage.set(oldValue)
        mergingValue_isNull=None
        if mergingValue is None:
            mergingValue_isNull = True
            clientMessage.set(mergingValue_isNull)
        else:
            mergingValue_isNull= False
            clientMessage.set(mergingValue_isNull)
        clientMessage.set(mergingValue)
        clientMessage.set(eventType)
        clientMessage.set(uuid)
        clientMessage.set(numberOfAffectedEntries)
        return clientMessage

    class EventHandler:
        def __init__(self,handler):
            self.handler=handler
        def handle(self, clientMessage):
            messageType = clientMessage.getOperationType()
            if (messageType == eventconstant.EVENT_ENTRY):
                key=None
                key_isNull = clientMessage.extractBooleanFromPayload()
                if not key_isNull:
                    key = clientMessage.extractBytesFromPayload()
                value=None
                value_isNull = clientMessage.extractBooleanFromPayload()
                if not value_isNull:
                    value = clientMessage.extractBytesFromPayload()
                oldValue=None
                oldValue_isNull = clientMessage.extractBooleanFromPayload()
                if not oldValue_isNull:
                    oldValue = clientMessage.extractBytesFromPayload()
                mergingValue=None
                mergingValue_isNull = clientMessage.extractBooleanFromPayload()
                if not mergingValue_isNull:
                    mergingValue = clientMessage.extractBytesFromPayload()
                eventType=None
                eventType = clientMessage.extractIntFromPayload()
                uuid=None
                uuid = clientMessage.extractStringFromPayload()
                numberOfAffectedEntries=None
                numberOfAffectedEntries = clientMessage.extractIntFromPayload()
                self.handler.handle(key, value, oldValue, mergingValue, eventType, uuid, numberOfAffectedEntries)
                return


'''
ADDENTRYLISTENERTOKEY
'''
class MapAddEntryListenerToKeyCodec:
    REQUEST_TYPE = MapMessageType.MAP_ADDENTRYLISTENERTOKEY
    RESPONSE_TYPE = 104
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapAddEntryListenerToKeyCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.includeValue=None
    @classmethod
    def encodeRequest(cls, name, key, includeValue):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddEntryListenerToKeyCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapAddEntryListenerToKeyCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(includeValue)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapAddEntryListenerToKeyCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        includeValue=None
        includeValue = clientMessage.extractBooleanFromPayload()
        parameters.includeValue = includeValue
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapAddEntryListenerToKeyCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddEntryListenerToKeyCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapAddEntryListenerToKeyCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response

        return parameters


    '''************************ EVENTS *************************'''

    @classmethod
    def encodeEntryEvent(cls,key, value,oldValue,  mergingValue, eventType, uuid, numberOfAffectedEntries):
        clientMessage=ClientMessage()
        clientMessage.setOperationType(eventconstant.EVENT_ENTRY)
        clientMessage.setEventFlag()
        key_isNull=None
        if key is None:
            key_isNull = True
            clientMessage.set(key_isNull)
        else:
            key_isNull= False
            clientMessage.set(key_isNull)
        clientMessage.set(key)
        value_isNull=None
        if value is None:
            value_isNull = True
            clientMessage.set(value_isNull)
        else:
            value_isNull= False
            clientMessage.set(value_isNull)
        clientMessage.set(value)
        oldValue_isNull=None
        if oldValue is None:
            oldValue_isNull = True
            clientMessage.set(oldValue_isNull)
        else:
            oldValue_isNull= False
            clientMessage.set(oldValue_isNull)
        clientMessage.set(oldValue)
        mergingValue_isNull=None
        if mergingValue is None:
            mergingValue_isNull = True
            clientMessage.set(mergingValue_isNull)
        else:
            mergingValue_isNull= False
            clientMessage.set(mergingValue_isNull)
            clientMessage.set(mergingValue)
        clientMessage.set(eventType)
        clientMessage.set(uuid)
        clientMessage.set(numberOfAffectedEntries)
        return clientMessage

    class EventHandler:
        def __init__(self,handler):
            self.handler=handler

        def handle(self, clientMessage):
            messageType = clientMessage.getOperationType()
            if (messageType == eventconstant.EVENT_ENTRY):
                key=None
                key_isNull = clientMessage.extractBooleanFromPayload()
                if not key_isNull:
                    key = clientMessage.extractBytesFromPayload()
                value=None
                value_isNull = clientMessage.extractBooleanFromPayload()
                if not value_isNull:
                    value = clientMessage.extractBytesFromPayload()
                oldValue=None
                oldValue_isNull = clientMessage.extractBooleanFromPayload()
                if not oldValue_isNull:
                    oldValue = clientMessage.extractBytesFromPayload()
                mergingValue=None
                mergingValue_isNull = clientMessage.extractBooleanFromPayload()
                if not mergingValue_isNull:
                    mergingValue = clientMessage.extractBytesFromPayload()
                eventType=None
                eventType = clientMessage.extractIntFromPayload()
                uuid=None
                uuid = clientMessage.extractStringFromPayload()
                numberOfAffectedEntries=None
                numberOfAffectedEntries = clientMessage.extractIntFromPayload()
                self.handler.handle(key, value, oldValue, mergingValue, eventType, uuid, numberOfAffectedEntries)
                return

'''
ADDENTRYLISTENER
'''
class MapAddEntryListenerCodec:
    REQUEST_TYPE = MapMessageType.MAP_ADDENTRYLISTENER
    RESPONSE_TYPE = 104
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapAddEntryListenerCodec.REQUEST_TYPE
            self.name=None
            self.includeValue=None
    @classmethod
    def encodeRequest(cls, name, includeValue):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddEntryListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapAddEntryListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(includeValue)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapAddEntryListenerCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        includeValue=None
        includeValue = clientMessage.extractBooleanFromPayload()
        parameters.includeValue = includeValue
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapAddEntryListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddEntryListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapAddEntryListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response

        return parameters


    '''************************ EVENTS *************************'''

    @classmethod
    def encodeEntryEvent(cls, key,value, oldValue, mergingValue, eventType, uuid, numberOfAffectedEntries):
        clientMessage=ClientMessage()
        clientMessage.setOperationType(eventconstant.EVENT_ENTRY)
        clientMessage.setEventFlag()
        key_isNull=None
        if key is None:
            key_isNull = True
            clientMessage.set(key_isNull)
        else:
            key_isNull= False
            clientMessage.set(key_isNull)
        clientMessage.set(key)
        value_isNull=None
        if value is None:
            value_isNull = True
            clientMessage.set(value_isNull)
        else:
            value_isNull= False
            clientMessage.set(value_isNull)
        clientMessage.set(value)
        oldValue_isNull=None
        if oldValue is None:
            oldValue_isNull = True
            clientMessage.set(oldValue_isNull)
        else:
            oldValue_isNull= False
            clientMessage.set(oldValue_isNull)
        clientMessage.set(oldValue)
        mergingValue_isNull=None
        if mergingValue is None:
            mergingValue_isNull = True
            clientMessage.set(mergingValue_isNull)
        else:
            mergingValue_isNull= False
            clientMessage.set(mergingValue_isNull)
            clientMessage.set(mergingValue)
        clientMessage.set(eventType)
        clientMessage.set(uuid)
        clientMessage.set(numberOfAffectedEntries)
        return clientMessage

    class EventHandler:
        def __init__(self,handler):
            self.handler=handler
        def handle(self, clientMessage):
            messageType = clientMessage.getOperationType()
            if (messageType == eventconstant.EVENT_ENTRY):
                key=None
                key_isNull = clientMessage.extractBooleanFromPayload()
                if not key_isNull:
                    key = clientMessage.extractBytesFromPayload()
                value=None
                value_isNull = clientMessage.extractBooleanFromPayload()
                if not value_isNull:
                    value = clientMessage.extractBytesFromPayload()
                oldValue=None
                oldValue_isNull = clientMessage.extractBooleanFromPayload()
                if not oldValue_isNull:
                    oldValue = clientMessage.extractBytesFromPayload()
                mergingValue=None
                mergingValue_isNull = clientMessage.extractBooleanFromPayload()
                if not mergingValue_isNull:
                    mergingValue = clientMessage.extractBytesFromPayload()
                eventType=None
                eventType = clientMessage.extractIntFromPayload()
                uuid=None

                self.handler.handle(key, value, oldValue, mergingValue, eventType, "", 1)

                #uuid = clientMessage.extractStringFromPayload()
                #numberOfAffectedEntries=None
                #numberOfAffectedEntries = clientMessage.extractIntFromPayload()
                #self.handler.handle(key, value, oldValue, mergingValue, eventType, uuid, numberOfAffectedEntries)
                return


'''
ADDNEARCACHEENTRYLISTENER
'''
class MapAddNearCacheEntryListenerCodec:
    REQUEST_TYPE = MapMessageType.MAP_ADDNEARCACHEENTRYLISTENER
    RESPONSE_TYPE = 104
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapAddNearCacheEntryListenerCodec.REQUEST_TYPE
            self.name=None
            self.includeValue=None
    @classmethod
    def encodeRequest(cls, name, includeValue):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddNearCacheEntryListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapAddNearCacheEntryListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(includeValue)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapAddNearCacheEntryListenerCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        includeValue=None
        includeValue = clientMessage.extractBooleanFromPayload()
        parameters.includeValue = includeValue
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapAddNearCacheEntryListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddNearCacheEntryListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapAddNearCacheEntryListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response

        return parameters


    '''************************ EVENTS *************************'''

    @classmethod
    def encodeEntryEvent(cls,  key, value,oldValue,  mergingValue,  eventType,  uuid, numberOfAffectedEntries):
        clientMessage=ClientMessage()
        clientMessage.setOperationType(eventconstant.EVENT_ENTRY)
        clientMessage.setEventFlag()
        key_isNull=None
        if key is None:
            key_isNull = True
            clientMessage.set(key_isNull)
        else:
            key_isNull= False
            clientMessage.set(key_isNull)
        clientMessage.set(key)
        value_isNull=None
        if value is None:
            value_isNull = True
            clientMessage.set(value_isNull)
        else:
            value_isNull= False
            clientMessage.set(value_isNull)
        clientMessage.set(value)
        oldValue_isNull=None
        if oldValue is None:
            oldValue_isNull = True
            clientMessage.set(oldValue_isNull)
        else:
            oldValue_isNull= False
            clientMessage.set(oldValue_isNull)
        clientMessage.set(oldValue)
        mergingValue_isNull=None
        if mergingValue is None:
            mergingValue_isNull = True
            clientMessage.set(mergingValue_isNull)
        else:
            mergingValue_isNull= False
            clientMessage.set(mergingValue_isNull)
        clientMessage.set(mergingValue)
        clientMessage.set(eventType)
        clientMessage.set(uuid)
        clientMessage.set(numberOfAffectedEntries)
        return clientMessage

    class EventHandler:
        def __init__(self,handler):
            self.handler=handler
        def handle(self, clientMessage):
            messageType = clientMessage.getOperationType()
            if (messageType == eventconstant.EVENT_ENTRY):
                key=None
                key_isNull = clientMessage.extractBooleanFromPayload()
                if not key_isNull:
                    key = clientMessage.extractBytesFromPayload()
                value=None
                value_isNull = clientMessage.extractBooleanFromPayload()
                if not value_isNull:
                    value = clientMessage.extractBytesFromPayload()
                oldValue=None
                oldValue_isNull = clientMessage.extractBooleanFromPayload()
                if not oldValue_isNull:
                    oldValue = clientMessage.extractBytesFromPayload()
                mergingValue=None
                mergingValue_isNull = clientMessage.extractBooleanFromPayload()
                if not mergingValue_isNull:
                    mergingValue = clientMessage.extractBytesFromPayload()
                eventType=None
                eventType = clientMessage.extractIntFromPayload()
                uuid=None
                uuid = clientMessage.extractStringFromPayload()
                numberOfAffectedEntries=None
                numberOfAffectedEntries = clientMessage.extractIntFromPayload()
                self.handler.handle(key, value, oldValue, mergingValue, eventType, uuid, numberOfAffectedEntries)
                return


'''
REMOVEENTRYLISTENER
'''
class MapRemoveEntryListenerCodec:
    REQUEST_TYPE = MapMessageType.MAP_REMOVEENTRYLISTENER
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapRemoveEntryListenerCodec.REQUEST_TYPE
            self.name=None
            self.registrationId=None
    @classmethod
    def encodeRequest(cls, name, registrationId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapRemoveEntryListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapRemoveEntryListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(registrationId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapRemoveEntryListenerCodec.RequestParameters()
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
            self.TYPE = MapRemoveEntryListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapRemoveEntryListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapRemoveEntryListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters



'''
ADDPARTITIONLOSTLISTENER
'''
class MapAddPartitionLostListenerCodec:
    REQUEST_TYPE = MapMessageType.MAP_ADDPARTITIONLOSTLISTENER
    RESPONSE_TYPE = 104
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapAddPartitionLostListenerCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddPartitionLostListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapAddPartitionLostListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapAddPartitionLostListenerCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapAddPartitionLostListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddPartitionLostListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapAddPartitionLostListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response

        return parameters


    '''************************ EVENTS *************************'''

    @classmethod
    def encodeMapPartitionLostEvent(cls, partitionId, uuid):
        clientMessage=ClientMessage()
        clientMessage.setOperationType(eventconstant.EVENT_MAPPARTITIONLOST)
        clientMessage.setEventFlag()
        clientMessage.set(partitionId)
        clientMessage.set(uuid)
        return clientMessage

    class EventHandler:
        def __init__(self,handler):
            self.handler=handler
        def handle(self, clientMessage):
            messageType = clientMessage.getOperationType()
            if (messageType == eventconstant.EVENT_MAPPARTITIONLOST):
                partitionId=None
                partitionId = clientMessage.extractIntFromPayload()
                uuid=None
                uuid = clientMessage.extractStringFromPayload()
                self.handler.handle(partitionId, uuid)


'''
REMOVEPARTITIONLOSTLISTENER
'''
class MapRemovePartitionLostListenerCodec:
    REQUEST_TYPE = MapMessageType.MAP_REMOVEPARTITIONLOSTLISTENER
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapRemovePartitionLostListenerCodec.REQUEST_TYPE
            self.name=None
            self.registrationId=None
    @classmethod
    def encodeRequest(cls, name, registrationId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapRemovePartitionLostListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapRemovePartitionLostListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(registrationId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapRemovePartitionLostListenerCodec.RequestParameters()
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
            self.TYPE = MapRemovePartitionLostListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapRemovePartitionLostListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapRemovePartitionLostListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters



'''
GETENTRYVIEW
'''
class MapGetEntryViewCodec:
    REQUEST_TYPE = MapMessageType.MAP_GETENTRYVIEW
    RESPONSE_TYPE = 111
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapGetEntryViewCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, key, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapGetEntryViewCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapGetEntryViewCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapGetEntryViewCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapGetEntryViewCodec.RESPONSE_TYPE
            self.dataEntryView=None
    @classmethod
    def encodeResponse(cls, dataEntryView):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapGetEntryViewCodec.RESPONSE_TYPE)
        dataEntryView_isNull=None
        if dataEntryView is None:
            dataEntryView_isNull = True
            clientMessage.set(dataEntryView_isNull)
        else:
            dataEntryView_isNull= False
            clientMessage.set(dataEntryView_isNull)
            clientMessage.set(dataEntryView)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapGetEntryViewCodec.ResponseParameters()
        dataEntryView=None
        dataEntryView_isNull = clientMessage.extractBooleanFromPayload()
        if not dataEntryView_isNull:
            dataEntryView = com.hazelcast.client.impl.protocol.codec.EntryViewCodec.decode(clientMessage)
        parameters.dataEntryView = dataEntryView

        return parameters


'''
EVICT
'''
class MapEvictCodec:
    REQUEST_TYPE = MapMessageType.MAP_EVICT
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapEvictCodec.REQUEST_TYPE
            self.name=None
            self.key=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, key, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapEvictCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapEvictCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapEvictCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapEvictCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapEvictCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapEvictCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters



'''
EVICTALL
'''
class MapEvictAllCodec:
    REQUEST_TYPE = MapMessageType.MAP_EVICTALL
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapEvictAllCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapEvictAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapEvictAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapEvictAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapEvictAllCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapEvictAllCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapEvictAllCodec.ResponseParameters()

        return parameters



'''
LOADALL
'''
class MapLoadAllCodec:
    REQUEST_TYPE = MapMessageType.MAP_LOADALL
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapLoadAllCodec.REQUEST_TYPE
            self.name=None
            self.replaceExistingValues=None
    @classmethod
    def encodeRequest(cls, name, replaceExistingValues):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapLoadAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapLoadAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(replaceExistingValues)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapLoadAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        replaceExistingValues=None
        replaceExistingValues = clientMessage.extractBooleanFromPayload()
        parameters.replaceExistingValues = replaceExistingValues
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapLoadAllCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapLoadAllCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapLoadAllCodec.ResponseParameters()

        return parameters



'''
LOADGIVENKEYS
'''
class MapLoadGivenKeysCodec:
    REQUEST_TYPE = MapMessageType.MAP_LOADGIVENKEYS
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapLoadGivenKeysCodec.REQUEST_TYPE
            self.name=None
            self.keys=None
            self.replaceExistingValues=None
    @classmethod
    def encodeRequest(cls, name, keys, replaceExistingValues):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapLoadGivenKeysCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapLoadGivenKeysCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(keys.size())
        for keys_item in keys:
            clientMessage.set(keys_item)
        clientMessage.set(replaceExistingValues)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapLoadGivenKeysCodec.RequestParameters()
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
            self.TYPE = MapLoadGivenKeysCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapLoadGivenKeysCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapLoadGivenKeysCodec.ResponseParameters()

        return parameters



'''
KEYSET
'''
class MapKeySetCodec:
    REQUEST_TYPE = MapMessageType.MAP_KEYSET
    RESPONSE_TYPE = 113
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapKeySetCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapKeySetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapKeySetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapKeySetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapKeySetCodec.RESPONSE_TYPE
            self.set=None
    @classmethod
    def encodeResponse(cls, set):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapKeySetCodec.RESPONSE_TYPE)
        clientMessage.set(set.size())
        for set_item in set:
            clientMessage.set(set_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapKeySetCodec.ResponseParameters()
        set=None
        set_size = clientMessage.extractIntFromPayload()
        set = []
        for i in range(set_size):
            set_item=None
            set_item = clientMessage.extractBytesFromPayload()
            set.append(set_item)
        parameters.set = set

        return parameters


'''
GETALL
'''
class MapGetAllCodec:
    REQUEST_TYPE = MapMessageType.MAP_GETALL
    RESPONSE_TYPE = 114
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapGetAllCodec.REQUEST_TYPE
            self.name=None
            self.keys=None
    @classmethod
    def encodeRequest(cls, name, keys):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapGetAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapGetAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(keys.size())
        for keys_item in keys:
            clientMessage.set(keys_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapGetAllCodec.RequestParameters()
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
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapGetAllCodec.RESPONSE_TYPE
            self.entrySet=None
    @classmethod
    def encodeResponse(cls, entrySet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapGetAllCodec.RESPONSE_TYPE)
        clientMessage.set(entrySet.size())
        for entrySet_item in entrySet:
            clientMessage.set(entrySet_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapGetAllCodec.ResponseParameters()
        entrySet=None
        entrySet_size = clientMessage.extractIntFromPayload()
        entrySet = []
        for i in range(entrySet_size):
            entrySet_item=None
            entrySet_item = clientMessage.getMapEntry();
            entrySet.append(entrySet_item)
        parameters.entrySet = entrySet

        return parameters



'''
VALUES
'''
class MapValuesCodec:
    REQUEST_TYPE = MapMessageType.MAP_VALUES
    RESPONSE_TYPE = 106
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapValuesCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapValuesCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapValuesCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapValuesCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapValuesCodec.RESPONSE_TYPE
            self.list=None
    @classmethod
    def encodeResponse(cls, list):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapValuesCodec.RESPONSE_TYPE)
        clientMessage.set(list.size())
        for list_item in list:
            clientMessage.set(list_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapValuesCodec.ResponseParameters()
        list=None
        list_size = clientMessage.extractIntFromPayload()
        list = []
        for i in range(list_size):
            list_item=None
            list_item = clientMessage.extractBytesFromPayload()
            list.append(list_item)
        parameters.list = list

        return parameters



'''
ENTRYSET
'''
class MapEntrySetCodec:
    REQUEST_TYPE = MapMessageType.MAP_ENTRYSET
    RESPONSE_TYPE = 114
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapEntrySetCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapEntrySetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapEntrySetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapEntrySetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapEntrySetCodec.RESPONSE_TYPE
            self.entrySet=None
    @classmethod
    def encodeResponse(cls, entrySet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapEntrySetCodec.RESPONSE_TYPE)
        clientMessage.set(entrySet.size())
        for entrySet_item in entrySet:
            clientMessage.set(entrySet_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapEntrySetCodec.ResponseParameters()
        entrySet=None
        entrySet_size = clientMessage.extractIntFromPayload()
        entrySet = []
        for i in range(entrySet_size):
            entrySet_item=None
            entrySet_item = clientMessage.getMapEntry();
            entrySet.append(entrySet_item)
        parameters.entrySet = entrySet

        return parameters



'''
KEYSETWITHPREDICATE
'''
class MapKeySetWithPredicateCodec:
    REQUEST_TYPE = MapMessageType.MAP_KEYSETWITHPREDICATE
    RESPONSE_TYPE = 113
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapKeySetWithPredicateCodec.REQUEST_TYPE
            self.name=None
            self.predicate=None
    @classmethod
    def encodeRequest(cls, name, predicate):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapKeySetWithPredicateCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapKeySetWithPredicateCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(predicate)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapKeySetWithPredicateCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        predicate=None
        predicate = clientMessage.extractBytesFromPayload()
        parameters.predicate = predicate
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapKeySetWithPredicateCodec.RESPONSE_TYPE
            self.set=None
    @classmethod
    def encodeResponse(cls, set):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapKeySetWithPredicateCodec.RESPONSE_TYPE)
        clientMessage.set(set.size())
        for set_item in set:
            clientMessage.set(set_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapKeySetWithPredicateCodec.ResponseParameters()
        set=None
        set_size = clientMessage.extractIntFromPayload()
        set = []
        for i in range(set_size):
            set_item=None
            set_item = clientMessage.extractBytesFromPayload()
            set.append(set_item)
        parameters.set = set

        return parameters



'''
VALUESWITHPREDICATE
'''
class MapValuesWithPredicateCodec:
    REQUEST_TYPE = MapMessageType.MAP_VALUESWITHPREDICATE
    RESPONSE_TYPE = 106
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapValuesWithPredicateCodec.REQUEST_TYPE
            self.name=None
            self.predicate=None
    @classmethod
    def encodeRequest(cls, name, predicate):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapValuesWithPredicateCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapValuesWithPredicateCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(predicate)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapValuesWithPredicateCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        predicate=None
        predicate = clientMessage.extractBytesFromPayload()
        parameters.predicate = predicate
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapValuesWithPredicateCodec.RESPONSE_TYPE
            self.list=None
    @classmethod
    def encodeResponse(cls, list):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapValuesWithPredicateCodec.RESPONSE_TYPE)
        clientMessage.set(list.size())
        for list_item in list:
            clientMessage.set(list_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapValuesWithPredicateCodec.ResponseParameters()
        list=None
        list_size = clientMessage.extractIntFromPayload()
        list = []
        for i in range(list_size):
            list_item=None
            list_item = clientMessage.extractBytesFromPayload()
            list.append(list_item)
        parameters.list = list

        return parameters



'''
ENTRIESWITHPREDICATE
'''
class MapEntriesWithPredicateCodec:
    REQUEST_TYPE = MapMessageType.MAP_ENTRIESWITHPREDICATE
    RESPONSE_TYPE = 114
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapEntriesWithPredicateCodec.REQUEST_TYPE
            self.name=None
            self.predicate=None
    @classmethod
    def encodeRequest(cls, name, predicate):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapEntriesWithPredicateCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapEntriesWithPredicateCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(predicate)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapEntriesWithPredicateCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        predicate=None
        predicate = clientMessage.extractBytesFromPayload()
        parameters.predicate = predicate
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapEntriesWithPredicateCodec.RESPONSE_TYPE
            self.entrySet=None
    @classmethod
    def encodeResponse(cls, entrySet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapEntriesWithPredicateCodec.RESPONSE_TYPE)
        clientMessage.set(entrySet.size())
        for entrySet_item in entrySet:
            clientMessage.set(entrySet_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapEntriesWithPredicateCodec.ResponseParameters()
        entrySet=None
        entrySet_size = clientMessage.extractIntFromPayload()
        entrySet = []
        for i in range(entrySet_size):
            entrySet_item=None
            entrySet_item = clientMessage.getMapEntry()
            entrySet.append(entrySet_item)
        parameters.entrySet = entrySet

        return parameters



'''
ADDINDEX
'''
class MapAddIndexCodec:
    REQUEST_TYPE = MapMessageType.MAP_ADDINDEX
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapAddIndexCodec.REQUEST_TYPE
            self.name=None
            self.attribute=None
            self.ordered=None
    @classmethod
    def encodeRequest(cls, name, attribute, ordered):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddIndexCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapAddIndexCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(attribute)
        clientMessage.set(ordered)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapAddIndexCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        attribute=None
        attribute = clientMessage.extractStringFromPayload()
        parameters.attribute = attribute
        ordered=None
        ordered = clientMessage.extractBooleanFromPayload()
        parameters.ordered = ordered
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapAddIndexCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapAddIndexCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapAddIndexCodec.ResponseParameters()

        return parameters



'''
SIZE
'''
class MapSizeCodec:
    REQUEST_TYPE = MapMessageType.MAP_SIZE
    RESPONSE_TYPE = 102
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapSizeCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapSizeCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapSizeCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapSizeCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapSizeCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapSizeCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapSizeCodec.ResponseParameters()
        response=None
        response = clientMessage.extractIntFromPayload()
        parameters.response = response

        return parameters



'''
ISEMPTY
'''
class MapIsEmptyCodec:
    REQUEST_TYPE = MapMessageType.MAP_ISEMPTY
    RESPONSE_TYPE = 101
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapIsEmptyCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapIsEmptyCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapIsEmptyCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapIsEmptyCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapIsEmptyCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapIsEmptyCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapIsEmptyCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters



'''
PUTALL
'''
class MapPutAllCodec:
    REQUEST_TYPE = MapMessageType.MAP_PUTALL
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapPutAllCodec.REQUEST_TYPE
            self.name=None
            self.entries=None
    @classmethod
    def encodeRequest(cls, name, entries):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapPutAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapPutAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(entries.size())
        for keys,values in entries.iteritems():
            key = keys
            val = values
            clientMessage.set(key)
            clientMessage.set(val)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapPutAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        entries=None
        entries_size = clientMessage.extractIntFromPayload()
        entries = {}
        for i in range(entries_size):
            entries_key=None
            entries_val=None
            entries_key = clientMessage.extractBytesFromPayload()
            entries_val = clientMessage.extractBytesFromPayload()
            entries[entries_key]=entries_val
        parameters.entries = entries
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapPutAllCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapPutAllCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapPutAllCodec.ResponseParameters()

        return parameters



'''
CLEAR
'''
class MapClearCodec:
    REQUEST_TYPE = MapMessageType.MAP_CLEAR
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapClearCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapClearCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapClearCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapClearCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapClearCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapClearCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapClearCodec.ResponseParameters()

        return None



'''
EXECUTEONKEY
'''
class MapExecuteOnKeyCodec:
    REQUEST_TYPE = MapMessageType.MAP_EXECUTEONKEY
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapExecuteOnKeyCodec.REQUEST_TYPE
            self.name=None
            self.entryProcessor=None
            self.key=None
    @classmethod
    def encodeRequest(cls, name, entryProcessor, key):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapExecuteOnKeyCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapExecuteOnKeyCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(entryProcessor)
        clientMessage.set(key)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapExecuteOnKeyCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        entryProcessor=None
        entryProcessor = clientMessage.extractBytesFromPayload()
        parameters.entryProcessor = entryProcessor
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapExecuteOnKeyCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapExecuteOnKeyCodec.RESPONSE_TYPE)
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
        parameters=MapExecuteOnKeyCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
            parameters.response = response

        return parameters



'''
SUBMITTOKEY
'''
class MapSubmitToKeyCodec:
    REQUEST_TYPE = MapMessageType.MAP_SUBMITTOKEY
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapSubmitToKeyCodec.REQUEST_TYPE
            self.name=None
            self.entryProcessor=None
            self.key=None
    @classmethod
    def encodeRequest(cls, name, entryProcessor, key):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapSubmitToKeyCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapSubmitToKeyCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(entryProcessor)
        clientMessage.set(key)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapSubmitToKeyCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        entryProcessor=None
        entryProcessor = clientMessage.extractBytesFromPayload()
        parameters.entryProcessor = entryProcessor
        key=None
        key = clientMessage.extractBytesFromPayload()
        parameters.key = key
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapSubmitToKeyCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapSubmitToKeyCodec.RESPONSE_TYPE)
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
        parameters=MapSubmitToKeyCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
            parameters.response = response

        return parameters



'''
EXECUTEONALLKEYS
'''
class MapExecuteOnAllKeysCodec:
    REQUEST_TYPE = MapMessageType.MAP_EXECUTEONALLKEYS
    RESPONSE_TYPE = 114
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapExecuteOnAllKeysCodec.REQUEST_TYPE
            self.name=None
            self.entryProcessor=None
    @classmethod
    def encodeRequest(cls, name, entryProcessor):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapExecuteOnAllKeysCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapExecuteOnAllKeysCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(entryProcessor)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapExecuteOnAllKeysCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        entryProcessor=None
        entryProcessor = clientMessage.extractBytesFromPayload()
        parameters.entryProcessor = entryProcessor
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapExecuteOnAllKeysCodec.RESPONSE_TYPE
            self.entrySet=None
    @classmethod
    def encodeResponse(cls, entrySet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapExecuteOnAllKeysCodec.RESPONSE_TYPE)
        clientMessage.set(entrySet.size())
        for entrySet_item in entrySet:
            clientMessage.set(entrySet_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapExecuteOnAllKeysCodec.ResponseParameters()
        entrySet=None
        entrySet_size = clientMessage.extractIntFromPayload()
        entrySet = []
        for i in range(entrySet_size):
            entrySet_item=None
            entrySet_item = clientMessage.getMapEntry()
            entrySet.append(entrySet_item)
        parameters.entrySet = entrySet

        return parameters



'''
EXECUTEWITHPREDICATE
'''
class MapExecuteWithPredicateCodec:
    REQUEST_TYPE = MapMessageType.MAP_EXECUTEWITHPREDICATE
    RESPONSE_TYPE = 114
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapExecuteWithPredicateCodec.REQUEST_TYPE
            self.name=None
            self.entryProcessor=None
            self.predicate=None
    @classmethod
    def encodeRequest(cls, name, entryProcessor, predicate):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapExecuteWithPredicateCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapExecuteWithPredicateCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(entryProcessor)
        clientMessage.set(predicate)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapExecuteWithPredicateCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        entryProcessor=None
        entryProcessor = clientMessage.extractBytesFromPayload()
        parameters.entryProcessor = entryProcessor
        predicate=None
        predicate = clientMessage.extractBytesFromPayload()
        parameters.predicate = predicate
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapExecuteWithPredicateCodec.RESPONSE_TYPE
            self.entrySet=None
    @classmethod
    def encodeResponse(cls, entrySet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapExecuteWithPredicateCodec.RESPONSE_TYPE)
        clientMessage.set(entrySet.size())
        for entrySet_item in entrySet:
            clientMessage.set(entrySet_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapExecuteWithPredicateCodec.ResponseParameters()
        entrySet=None
        entrySet_size = clientMessage.extractIntFromPayload()
        entrySet = []
        for i in range(entrySet_size):
            entrySet_item=None
            entrySet_item = clientMessage.getMapEntry()
            entrySet.append(entrySet_item)
        parameters.entrySet = entrySet

        return parameters



'''
EXECUTEONKEYS
'''
class MapExecuteOnKeysCodec:
    REQUEST_TYPE = MapMessageType.MAP_EXECUTEONKEYS
    RESPONSE_TYPE = 114
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapExecuteOnKeysCodec.REQUEST_TYPE
            self.name=None
            self.entryProcessor=None
            self.keys=None
    @classmethod
    def encodeRequest(cls, name, entryProcessor, keys):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapExecuteOnKeysCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapExecuteOnKeysCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(entryProcessor)
        clientMessage.set(keys.size())
        for keys_item in keys:
            clientMessage.set(keys_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapExecuteOnKeysCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        entryProcessor=None
        entryProcessor = clientMessage.extractBytesFromPayload()
        parameters.entryProcessor = entryProcessor
        keys=None
        keys_size = clientMessage.extractIntFromPayload()
        keys = []
        for i in range(keys_size):
            keys_item=None
            keys_item = clientMessage.extractBytesFromPayload()
            keys.append(keys_item)
        parameters.keys = keys
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapExecuteOnKeysCodec.RESPONSE_TYPE
            self.entrySet=None
    @classmethod
    def encodeResponse(cls, entrySet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapExecuteOnKeysCodec.RESPONSE_TYPE)
        clientMessage.set(entrySet.size())
        for entrySet_item in entrySet:
            clientMessage.set(entrySet_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapExecuteOnKeysCodec.ResponseParameters()
        entrySet=None
        entrySet_size = clientMessage.extractIntFromPayload()
        entrySet = []
        for i in range(entrySet_size):
            entrySet_item=None
            entrySet_item = clientMessage.getMapEntry()
            entrySet.append(entrySet_item)
        parameters.entrySet = entrySet

        return parameters



'''
FORCEUNLOCK
'''
class MapForceUnlockCodec:
    REQUEST_TYPE = MapMessageType.MAP_FORCEUNLOCK
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapForceUnlockCodec.REQUEST_TYPE
            self.name=None
            self.key=None
    @classmethod
    def encodeRequest(cls, name, key):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapForceUnlockCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapForceUnlockCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(key)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapForceUnlockCodec.RequestParameters()
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
            self.TYPE = MapForceUnlockCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapForceUnlockCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapForceUnlockCodec.ResponseParameters()

        return parameters



'''
KEYSETWITHPAGINGPREDICATE
'''
class MapKeySetWithPagingPredicateCodec:
    REQUEST_TYPE = MapMessageType.MAP_KEYSETWITHPAGINGPREDICATE
    RESPONSE_TYPE = 113
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapKeySetWithPagingPredicateCodec.REQUEST_TYPE
            self.name=None
            self.predicate=None
    @classmethod
    def encodeRequest(cls, name, predicate):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapKeySetWithPagingPredicateCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapKeySetWithPagingPredicateCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(predicate)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapKeySetWithPagingPredicateCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        predicate=None
        predicate = clientMessage.extractBytesFromPayload()
        parameters.predicate = predicate
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapKeySetWithPagingPredicateCodec.RESPONSE_TYPE
            self.set=None
    @classmethod
    def encodeResponse(cls, set):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapKeySetWithPagingPredicateCodec.RESPONSE_TYPE)
        clientMessage.set(set.size())
        for set_item in set:
            clientMessage.set(set_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapKeySetWithPagingPredicateCodec.ResponseParameters()
        set=None
        set_size = clientMessage.extractIntFromPayload()
        set = []
        for i in range(set_size):
            set_item=None
            set_item = clientMessage.extractBytesFromPayload()
            set.append(set_item)
        parameters.set = set

        return parameters


'''
VALUESWITHPAGINGPREDICATE
'''
class MapValuesWithPagingPredicateCodec:
    REQUEST_TYPE = MapMessageType.MAP_VALUESWITHPAGINGPREDICATE
    RESPONSE_TYPE = 114
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapValuesWithPagingPredicateCodec.REQUEST_TYPE
            self.name=None
            self.predicate=None
    @classmethod
    def encodeRequest(cls, name, predicate):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapValuesWithPagingPredicateCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapValuesWithPagingPredicateCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(predicate)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapValuesWithPagingPredicateCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        predicate=None
        predicate = clientMessage.extractBytesFromPayload()
        parameters.predicate = predicate
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapValuesWithPagingPredicateCodec.RESPONSE_TYPE
            self.entrySet=None
    @classmethod
    def encodeResponse(cls, entrySet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapValuesWithPagingPredicateCodec.RESPONSE_TYPE)
        clientMessage.set(entrySet.size())
        for entrySet_item in entrySet:
            clientMessage.set(entrySet_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapValuesWithPagingPredicateCodec.ResponseParameters()
        entrySet=None
        entrySet_size = clientMessage.extractIntFromPayload()
        entrySet = []
        for i in range(entrySet_size):
            entrySet_item=None
            entrySet_item = clientMessage.getMapEntry()
            entrySet.append(entrySet_item)
        parameters.entrySet = entrySet

        return parameters



'''
ENTRIESWITHPAGINGPREDICATE
'''
class MapEntriesWithPagingPredicateCodec:
    REQUEST_TYPE = MapMessageType.MAP_ENTRIESWITHPAGINGPREDICATE
    RESPONSE_TYPE = 114
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = MapEntriesWithPagingPredicateCodec.REQUEST_TYPE
            self.name=None
            self.predicate=None
    @classmethod
    def encodeRequest(cls, name, predicate):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapEntriesWithPagingPredicateCodec.REQUEST_TYPE)
        clientMessage.setRetryable(MapEntriesWithPagingPredicateCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(predicate)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = MapEntriesWithPagingPredicateCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        predicate=None
        predicate = clientMessage.extractBytesFromPayload()
        parameters.predicate = predicate
        return parameters

    '''************************ RESPONSE *************************'''
    
    class ResponseParameters:
        def __init__(self):
            self.TYPE = MapEntriesWithPagingPredicateCodec.RESPONSE_TYPE
            self.entrySet=None
    @classmethod
    def encodeResponse(cls, entrySet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(MapEntriesWithPagingPredicateCodec.RESPONSE_TYPE)
        clientMessage.set(entrySet.size())
        for entrySet_item in entrySet:
            clientMessage.set(entrySet_item)
    
        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=MapEntriesWithPagingPredicateCodec.ResponseParameters()
        entrySet=None
        entrySet_size = clientMessage.extractIntFromPayload()
        entrySet = []
        for i in range(entrySet_size):
            entrySet_item=None
            entrySet_item = clientMessage.getMapEntry()
            entrySet.append(entrySet_item)
        parameters.entrySet = entrySet
        
        return parameters