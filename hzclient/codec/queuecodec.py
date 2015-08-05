__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
import eventconstant
class QueueMessageType:
    QUEUE_OFFER=0x0301
    QUEUE_PUT=0x0302
    QUEUE_SIZE=0x0303
    QUEUE_REMOVE=0x0304
    QUEUE_POLL=0x0305
    QUEUE_TAKE=0x0306
    QUEUE_PEEK=0x0307
    QUEUE_ITERATOR=0x0308
    QUEUE_DRAINTO=0x0309
    QUEUE_DRAINTOMAXSIZE=0x030a
    QUEUE_CONTAINS=0x030b
    QUEUE_CONTAINSALL=0x030c
    QUEUE_COMPAREANDREMOVEALL=0x030d
    QUEUE_COMPAREANDRETAINALL=0x030e
    QUEUE_CLEAR=0x030f
    QUEUE_ADDALL=0x0310
    QUEUE_ADDLISTENER=0x0311
    QUEUE_REMOVELISTENER=0x0312
    QUEUE_REMAININGCAPACITY=0x0313
    QUEUE_ISEMPTY=0x0314
    id=None

    def ___init__(self, messageType):
        self.id = messageType

    def id(self):
        return self.id


class QueueOfferCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_OFFER
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueOfferCodec.REQUEST_TYPE
            name=None
            value=None
            timeoutMillis=None

    def encodeRequest(self, name, value, timeoutMillis):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueOfferCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueOfferCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.set(timeoutMillis)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueOfferCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        timeoutMillis=None
        timeoutMillis = clientMessage.extractLongFromPayload();
        parameters.timeoutMillis = timeoutMillis
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = QueueOfferCodec.RESPONSE_TYPE
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueOfferCodec.RESPONSE_TYPE)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueOfferCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response
        return parameters




class QueuePutCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_PUT
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        TYPE = QueuePutCodec.REQUEST_TYPE
        name=None
        value=None

        def __init__(self):
            temp=None

    def encodeRequest(self, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueuePutCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueuePutCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueuePutCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        return parameters

    '''************************ RESPONSE *************************'''

    def encodeResponse(self):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueuePutCodec.RESPONSE_TYPE)
        return clientMessage

    def decodeResponse(self, clientMessage):
        return None

class QueueSizeCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_SIZE
    RESPONSE_TYPE = 102
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueSizeCodec.REQUEST_TYPE
            name=None

    def encodeRequest(self, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueSizeCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueSizeCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueSizeCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueSizeCodec.RESPONSE_TYPE)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueSizeCodec.ResponseParameters()
        response=None
        response = clientMessage.extractIntFromPayload()
        parameters.response = response
        return parameters

class QueueRemoveCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_REMOVE
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueRemoveCodec.REQUEST_TYPE
            name=None
            value=None

    def encodeRequest(self, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueRemoveCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueRemoveCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueRemoveCodec.RequestParameters()
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
            TYPE = QueueRemoveCodec.RESPONSE_TYPE
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueRemoveCodec.RESPONSE_TYPE)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueRemoveCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response
        return parameters


class QueuePollCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_POLL
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueuePollCodec.REQUEST_TYPE
            name=None
            timeoutMillis=None

    def encodeRequest(self, name, timeoutMillis):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueuePollCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueuePollCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(timeoutMillis)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueuePollCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        timeoutMillis=None
        timeoutMillis = clientMessage.extractLongFromPayload()
        parameters.timeoutMillis = timeoutMillis
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = QueuePollCodec.RESPONSE_TYPE
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueuePollCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueuePollCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response
        return parameters

class QueueTakeCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_TAKE
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueTakeCodec.REQUEST_TYPE
            name=None

    def encodeRequest(self, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueTakeCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueTakeCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueTakeCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = QueueTakeCodec.RESPONSE_TYPE
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueTakeCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueTakeCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response
        return parameters

class QueuePeekCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_PEEK
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueuePeekCodec.REQUEST_TYPE
            name=None

    def encodeRequest(self, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueuePeekCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueuePeekCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueuePeekCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = QueuePeekCodec.RESPONSE_TYPE
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueuePeekCodec.RESPONSE_TYPE)
        response_isNull=None
        if response is None:
            response_isNull = True
            clientMessage.set(response_isNull)
        else:
            response_isNull= False
            clientMessage.set(response_isNull)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueuePeekCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response
        return parameters

class QueueIteratorCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_ITERATOR
    RESPONSE_TYPE = 106
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueIteratorCodec.REQUEST_TYPE
            name=None

    def encodeRequest(self, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueIteratorCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueIteratorCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueIteratorCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = QueueIteratorCodec.RESPONSE_TYPE
            list=None

    def encodeResponse(list):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueIteratorCodec.RESPONSE_TYPE)
        clientMessage.set(list.size())
        for list_item in list:
            clientMessage.set(list_item)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueIteratorCodec.ResponseParameters()
        list=None
        list_size = clientMessage.extractIntFromPayload()
        list = []
        for i in range(list_size):
            list_item=None
            list_item = clientMessage.extractBytesFromPayload()
            list.append(list_item)
        parameters.list = list
        return parameters

class QueueDrainToCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_DRAINTO
    RESPONSE_TYPE = 106
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueDrainToCodec.REQUEST_TYPE
            name=None

    def encodeRequest(self, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueDrainToCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueDrainToCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueDrainToCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = QueueDrainToCodec.RESPONSE_TYPE
            list=None

    def encodeResponse(list):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueDrainToCodec.RESPONSE_TYPE)
        clientMessage.set(list.size())
        for list_item in list:
            clientMessage.set(list_item)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueDrainToCodec.ResponseParameters()
        list=None
        list_size = clientMessage.extractIntFromPayload()
        list = []
        for i in range(list_size):
            list_item=None
        list_item = clientMessage.extractBytesFromPayload()
        list.append(list_item)
        parameters.list = list
        return parameters

class QueueDrainToMaxSizeCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_DRAINTOMAXSIZE
    RESPONSE_TYPE = 106
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueDrainToMaxSizeCodec.REQUEST_TYPE
            name=None
            maxSize=None

    def encodeRequest(self, name, maxSize):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueDrainToMaxSizeCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueDrainToMaxSizeCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(maxSize)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueDrainToMaxSizeCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        maxSize=None
        maxSize = clientMessage.extractIntFromPayload()
        parameters.maxSize = maxSize
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = QueueDrainToMaxSizeCodec.RESPONSE_TYPE
            list=None

    def encodeResponse(list):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueDrainToMaxSizeCodec.RESPONSE_TYPE)
        clientMessage.set(list.size())
        for list_item in list:
            clientMessage.set(list_item)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueDrainToMaxSizeCodec.ResponseParameters()
        list=None
        list_size = clientMessage.extractIntFromPayload()
        list = []
        for i in range(list_size):
            list_item=None
            list_item = clientMessage.extractBytesFromPayload()
            list.append(list_item)
        parameters.list = list
        return parameters



class QueueContainsCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_CONTAINS
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueContainsCodec.REQUEST_TYPE
            name=None
            value=None

    def encodeRequest(self, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueContainsCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueContainsCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueContainsCodec.RequestParameters()
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
            TYPE = QueueContainsCodec.RESPONSE_TYPE
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueContainsCodec.RESPONSE_TYPE)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueContainsCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload();
        parameters.response = response
        return parameters

class QueueContainsAllCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_CONTAINSALL
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueContainsAllCodec.REQUEST_TYPE
            name=None
            dataList=None

    def encodeRequest(self, name, dataList):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueContainsAllCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueContainsAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(dataList.size())
        for dataList_item in dataList:
            clientMessage.set(dataList_item)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueContainsAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        dataList=None
        dataList_size = clientMessage.extractIntFromPayload()
        dataList = []
        for i in range(dataList_size):
            dataList_item=None
            dataList_item = clientMessage.extractBytesFromPayload()
            dataList.append(dataList_item)
        parameters.dataList = dataList
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = QueueContainsAllCodec.RESPONSE_TYPE
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueContainsAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueContainsAllCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response
        return parameters


class QueueCompareAndRemoveAllCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_COMPAREANDREMOVEALL
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueCompareAndRemoveAllCodec.REQUEST_TYPE
            name=None
            dataList=None

    def encodeRequest(self, name, dataList):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueCompareAndRemoveAllCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueCompareAndRemoveAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(dataList.size())
        for dataList_item in dataList:
            clientMessage.set(dataList_item)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueCompareAndRemoveAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        dataList=None
        dataList_size = clientMessage.extractIntFromPayload()
        dataList = []
        for i in range(dataList_size):
            dataList_item=None
            dataList_item = clientMessage.extractBytesFromPayload()
            dataList.append(dataList_item)
        parameters.dataList = dataList
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = QueueCompareAndRemoveAllCodec.RESPONSE_TYPE
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueCompareAndRemoveAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueCompareAndRemoveAllCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response
        return parameters

class QueueCompareAndRetainAllCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_COMPAREANDRETAINALL
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueCompareAndRetainAllCodec.REQUEST_TYPE
            name=None
            dataList=None

    def encodeRequest(self, name, dataList):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueCompareAndRetainAllCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueCompareAndRetainAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(dataList.size())
        for dataList_item in dataList:
            clientMessage.set(dataList_item)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueCompareAndRetainAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        dataList=None
        dataList_size = clientMessage.extractIntFromPayload()
        dataList = []
        for i in range(dataList_size):
            dataList_item=None
            dataList_item = clientMessage.extractBytesFromPayload()
            dataList.append(dataList_item)
        parameters.dataList = dataList
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = QueueCompareAndRetainAllCodec.RESPONSE_TYPE
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueCompareAndRetainAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueCompareAndRetainAllCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response
        return parameters



class QueueClearCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_CLEAR
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueClearCodec.REQUEST_TYPE
            name=None

    def encodeRequest(self, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueClearCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueClearCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueClearCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    def encodeResponse(self):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueClearCodec.RESPONSE_TYPE)
        return clientMessage

    def decodeResponse(self, clientMessage):
        return None

class QueueAddAllCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_ADDALL
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueAddAllCodec.REQUEST_TYPE
            name=None
            dataList=None

    def encodeRequest(self, name, dataList):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueAddAllCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueAddAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(dataList.size())
        for dataList_item in dataList:
            clientMessage.set(dataList_item)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueAddAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        dataList=None
        dataList_size = clientMessage.extractIntFromPayload()
        dataList = []
        for i in range(dataList_size):
            dataList_item=None
            dataList_item = clientMessage.extractBytesFromPayload()
            dataList.append(dataList_item)
        parameters.dataList = dataList
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = QueueAddAllCodec.RESPONSE_TYPE
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueAddAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueAddAllCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response
        return parameters

class QueueAddListenerCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_ADDLISTENER
    RESPONSE_TYPE = 104
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueAddListenerCodec.REQUEST_TYPE
            name=None
            includeValue=None

    def encodeRequest(self, name, includeValue):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueAddListenerCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueAddListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(includeValue)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueAddListenerCodec.RequestParameters()
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
            TYPE = QueueAddListenerCodec.RESPONSE_TYPE
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueAddListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueAddListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response
        return parameters


    '''************************ EVENTS *************************'''


    def encodeItemEvent(self, item, uuid, eventType):
        clientMessage=ClientMessage()
        clientMessage.setOperationType(eventconstant.EVENT_ITEM)
        clientMessage.setEventFlag()
        item_isNull=None
        if item is None:
            item_isNull = True
            clientMessage.set(item_isNull)
        else:
            item_isNull= False
            clientMessage.set(item_isNull)
            clientMessage.set(item)
            clientMessage.set(uuid)
            clientMessage.set(eventType)
            return clientMessage

    class AbstractEventHandler:
        def handle(self, clientMessage):
            messageType = clientMessage.getOperationType()
            if (messageType == eventconstant.EVENT_ITEM):
                item=None
                item_isNull = clientMessage.extractBooleanFromPayload()
                if not item_isNull:
                    item = clientMessage.extractBytesFromPayload()
                    uuid=None
                    uuid = clientMessage.extractStringFromPayload()
                    eventType=None
                    eventType = clientMessage.extractIntFromPayload()
                    self.handle(item, uuid, eventType)
                    return


class QueueRemoveListenerCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_REMOVELISTENER
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueRemoveListenerCodec.REQUEST_TYPE
            name=None
            registrationId=None

    def encodeRequest(self, name, registrationId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueRemoveListenerCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueRemoveListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(registrationId)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueRemoveListenerCodec.RequestParameters()
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
            TYPE = QueueRemoveListenerCodec.RESPONSE_TYPE
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueRemoveListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueRemoveListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response
        return parameters


class QueueRemainingCapacityCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_REMAININGCAPACITY
    RESPONSE_TYPE = 102
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueRemainingCapacityCodec.REQUEST_TYPE
            name=None

    def encodeRequest(self, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueRemainingCapacityCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueRemainingCapacityCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueRemainingCapacityCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = QueueRemainingCapacityCodec.RESPONSE_TYPE
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueRemainingCapacityCodec.RESPONSE_TYPE)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueRemainingCapacityCodec.ResponseParameters()
        response=None
        response = clientMessage.extractIntFromPayload()
        parameters.response = response
        return parameters


class QueueIsEmptyCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_ISEMPTY
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = QueueIsEmptyCodec.REQUEST_TYPE
            name=None

    def encodeRequest(self, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueIsEmptyCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueIsEmptyCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage


    def decodeRequest(self, clientMessage):
        parameters = QueueIsEmptyCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = QueueIsEmptyCodec.RESPONSE_TYPE
            response=None

    def encodeResponse(response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueIsEmptyCodec.RESPONSE_TYPE)
        clientMessage.set(response)
        return clientMessage

    def decodeResponse(self, clientMessage):
        parameters=QueueIsEmptyCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response
        return parameters