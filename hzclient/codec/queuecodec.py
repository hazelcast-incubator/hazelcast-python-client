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
            self.TYPE = QueueOfferCodec.REQUEST_TYPE
            self.name=None
            self.value=None
            self.timeoutMillis=None
    @classmethod
    def encodeRequest(cls, name, value, timeoutMillis):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueOfferCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueOfferCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.set(timeoutMillis)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = QueueOfferCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        timeoutMillis=None
        timeoutMillis = clientMessage.extractLongFromPayload()
        parameters.timeoutMillis = timeoutMillis
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = QueueOfferCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueOfferCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
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
        def __init__(self):
            self.TYPE = QueuePutCodec.REQUEST_TYPE
            self.name=None
            self.value=None
    @classmethod
    def encodeRequest(cls, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueuePutCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueuePutCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = QueuePutCodec.RequestParameters()
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
            self.TYPE = QueuePutCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueuePutCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=QueuePutCodec.ResponseParameters()

        return parameters



class QueueSizeCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_SIZE
    RESPONSE_TYPE = 102
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = QueueSizeCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueSizeCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(QueueSizeCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = QueueSizeCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = QueueSizeCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueSizeCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
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
            self.TYPE = QueueRemoveCodec.REQUEST_TYPE
            self.name=None
            self.value=None
    @classmethod
    def encodeRequest(cls, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueRemoveCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueRemoveCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
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
            self.TYPE = QueueRemoveCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueRemoveCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
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
            self.TYPE = QueuePollCodec.REQUEST_TYPE
            self.name=None
            self.timeoutMillis=None
    @classmethod
    def encodeRequest(cls, name, timeoutMillis):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueuePollCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueuePollCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(timeoutMillis)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
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
            self.TYPE = QueuePollCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
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
    @classmethod
    def decodeResponse(cls, clientMessage):
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
            self.TYPE = QueueTakeCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueTakeCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueTakeCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = QueueTakeCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = QueueTakeCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
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
    @classmethod
    def decodeResponse(cls, clientMessage):
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
            self.TYPE = QueuePeekCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueuePeekCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueuePeekCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = QueuePeekCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = QueuePeekCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
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
    @classmethod
    def decodeResponse(cls, clientMessage):
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
            self.TYPE = QueueIteratorCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueIteratorCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueIteratorCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = QueueIteratorCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = QueueIteratorCodec.RESPONSE_TYPE
            self.list=None
    @classmethod
    def encodeResponse(cls, list):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueIteratorCodec.RESPONSE_TYPE)
        clientMessage.set(list.size())
        for list_item in list:
            clientMessage.set(list_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
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
            self.TYPE = QueueDrainToCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueDrainToCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueDrainToCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = QueueDrainToCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = QueueDrainToCodec.RESPONSE_TYPE
            self.list=None
    @classmethod
    def encodeResponse(cls, list):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueDrainToCodec.RESPONSE_TYPE)
        clientMessage.set(list.size())
        for list_item in list:
            clientMessage.set(list_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
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
            self.TYPE = QueueDrainToMaxSizeCodec.REQUEST_TYPE
            self.name=None
            self.maxSize=None
    @classmethod
    def encodeRequest(cls, name, maxSize):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueDrainToMaxSizeCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueDrainToMaxSizeCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(maxSize)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
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
            self.TYPE = QueueDrainToMaxSizeCodec.RESPONSE_TYPE
            self.list=None
    @classmethod
    def encodeResponse(cls, list):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueDrainToMaxSizeCodec.RESPONSE_TYPE)
        clientMessage.set(list.size())
        for list_item in list:
            clientMessage.set(list_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
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
            self.TYPE = QueueContainsCodec.REQUEST_TYPE
            self.name=None
            self.value=None
    @classmethod
    def encodeRequest(cls, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueContainsCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueContainsCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
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
            self.TYPE = QueueContainsCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueContainsCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=QueueContainsCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class QueueContainsAllCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_CONTAINSALL
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = QueueContainsAllCodec.REQUEST_TYPE
            self.name=None
            self.dataList=None
    @classmethod
    def encodeRequest(cls, name, dataList):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueContainsAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueContainsAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(dataList.size())
        for dataList_item in dataList:
            clientMessage.set(dataList_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
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
            self.TYPE = QueueContainsAllCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueContainsAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
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
            self.TYPE = QueueCompareAndRemoveAllCodec.REQUEST_TYPE
            self.name=None
            self.dataList=None
    @classmethod
    def encodeRequest(cls, name, dataList):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueCompareAndRemoveAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueCompareAndRemoveAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(dataList.size())
        for dataList_item in dataList:
            clientMessage.set(dataList_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
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
            self.TYPE = QueueCompareAndRemoveAllCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueCompareAndRemoveAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
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
            self.TYPE = QueueCompareAndRetainAllCodec.REQUEST_TYPE
            self.name=None
            self.dataList=None
    @classmethod
    def encodeRequest(cls, name, dataList):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueCompareAndRetainAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueCompareAndRetainAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(dataList.size())
        for dataList_item in dataList:
            clientMessage.set(dataList_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
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
            self.TYPE = QueueCompareAndRetainAllCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueCompareAndRetainAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
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
            self.TYPE = QueueClearCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueClearCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueClearCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = QueueClearCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = QueueClearCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueClearCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=QueueClearCodec.ResponseParameters()

        return parameters



class QueueAddAllCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_ADDALL
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = QueueAddAllCodec.REQUEST_TYPE
            self.name=None
            self.dataList=None
    @classmethod
    def encodeRequest(cls, name, dataList):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueAddAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueAddAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(dataList.size())
        for dataList_item in dataList:
            clientMessage.set(dataList_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
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
            self.TYPE = QueueAddAllCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueAddAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
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
            self.TYPE = QueueAddListenerCodec.REQUEST_TYPE
            self.name=None
            self.includeValue=None
    @classmethod
    def encodeRequest(cls, name, includeValue):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueAddListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueAddListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(includeValue)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
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
            self.TYPE = QueueAddListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueAddListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=QueueAddListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response

        return parameters


    '''************************ EVENTS *************************'''

    @classmethod
    def encodeItemEvent(cls,  item, uuid, eventType):
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

    class EventHandler:
        def __init__(self,handler)
            self.handler=handler
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
                self.handler.handle(item, uuid, eventType)
                return


class QueueRemoveListenerCodec:
    REQUEST_TYPE = QueueMessageType.QUEUE_REMOVELISTENER
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = QueueRemoveListenerCodec.REQUEST_TYPE
            self.name=None
            self.registrationId=None
    @classmethod
    def encodeRequest(cls, name, registrationId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueRemoveListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueRemoveListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(registrationId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
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
            self.TYPE = QueueRemoveListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueRemoveListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
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
            self.TYPE = QueueRemainingCapacityCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueRemainingCapacityCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueRemainingCapacityCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = QueueRemainingCapacityCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = QueueRemainingCapacityCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueRemainingCapacityCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
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
            self.TYPE = QueueIsEmptyCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueIsEmptyCodec.REQUEST_TYPE)
        clientMessage.setRetryable(QueueIsEmptyCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = QueueIsEmptyCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = QueueIsEmptyCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(QueueIsEmptyCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=QueueIsEmptyCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

