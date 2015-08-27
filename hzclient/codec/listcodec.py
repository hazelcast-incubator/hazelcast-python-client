import ctypes
from hzclient.clientmessage import ClientMessage
from util import util
from util import encode

import eventconstant


class ListMessageType:
    LIST_SIZE=0x0501
    LIST_CONTAINS=0x0502
    LIST_CONTAINSALL=0x0503
    LIST_ADD=0x0504
    LIST_REMOVE=0x0505
    LIST_ADDALL=0x0506
    LIST_COMPAREANDREMOVEALL=0x0507
    LIST_COMPAREANDRETAINALL=0x0508
    LIST_CLEAR=0x0509
    LIST_GETALL=0x050a
    LIST_ADDLISTENER=0x050b
    LIST_REMOVELISTENER=0x050c
    LIST_ISEMPTY=0x050d
    LIST_ADDALLWITHINDEX=0x050e
    LIST_GET=0x050f
    LIST_SET=0x0510
    LIST_ADDWITHINDEX=0x0511
    LIST_REMOVEWITHINDEX=0x0512
    LIST_LASTINDEXOF=0x0513
    LIST_INDEXOF=0x0514
    LIST_SUB=0x0515
    LIST_ITERATOR=0x0516
    LIST_LISTITERATOR=0x0517

    def ___init__(self, messageType):
        self.id = messageType

    def id(self):
        return self.id



class ListAddAllCodec:
    REQUEST_TYPE = ListMessageType.LIST_ADDALL
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListAddAllCodec.REQUEST_TYPE
            self.name=None
            self.valueList=None
    @classmethod
    def encodeRequest(cls, name, valueList):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListAddAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListAddAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(valueList.size())
        for valueList_item in valueList:
            clientMessage.set(valueList_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListAddAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        valueList=None
        valueList_size = clientMessage.extractIntFromPayload()
        valueList = []
        for i in range(valueList_size):
            valueList_item=None
            valueList_item = clientMessage.extractBytesFromPayload()
            valueList.append(valueList_item)
        parameters.valueList = valueList
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListAddAllCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListAddAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListAddAllCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

class ListAddAllWithIndexCodec:
    REQUEST_TYPE = ListMessageType.LIST_ADDALLWITHINDEX
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListAddAllWithIndexCodec.REQUEST_TYPE
            self.name=None
            self.index=None
            self.valueList=None
    @classmethod
    def encodeRequest(cls, name, index, valueList):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListAddAllWithIndexCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(ListAddAllWithIndexCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(index)
        clientMessage.set(valueList.size())
        for valueList_item in valueList:
            clientMessage.set(valueList_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListAddAllWithIndexCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        index=None
        index = clientMessage.extractIntFromPayload()
        parameters.index = index
        valueList=None
        valueList_size = clientMessage.extractIntFromPayload()
        valueList = []
        for i in range(valueList_size):
            valueList_item=None
            valueList_item = clientMessage.extractBytesFromPayload()
            valueList.append(valueList_item)
        parameters.valueList = valueList
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListAddAllWithIndexCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListAddAllWithIndexCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListAddAllWithIndexCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

class ListAddCodec:
    REQUEST_TYPE = ListMessageType.LIST_ADD
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListAddCodec.REQUEST_TYPE
            self.name=None
            self.value=None
    @classmethod
    def encodeRequest(cls, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListAddCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListAddCodec.RETRYABLE)
        clientMessage.set(encode.encodestring(name))
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListAddCodec.RequestParameters()
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
            self.TYPE = ListAddCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListAddCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListAddCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

class ListAddListenerCodec:
    REQUEST_TYPE = ListMessageType.LIST_ADDLISTENER
    RESPONSE_TYPE = 104
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListAddListenerCodec.REQUEST_TYPE
            self.name=None
            self.includeValue=None
    @classmethod
    def encodeRequest(cls, name, includeValue):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListAddListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListAddListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(includeValue)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListAddListenerCodec.RequestParameters()
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
            self.TYPE = ListAddListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListAddListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListAddListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response

        return parameters


    '''************************ EVENTS *************************'''



    class EventHandler:
        def __init__(self,handler):
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

class ListAddWithIndexCodec:
    REQUEST_TYPE = ListMessageType.LIST_ADDWITHINDEX
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListAddWithIndexCodec.REQUEST_TYPE
            self.name=None
            self.index=None
            self.value=None
    @classmethod
    def encodeRequest(cls, name, index, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListAddWithIndexCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(ListAddWithIndexCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(index)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListAddWithIndexCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        index=None
        index = clientMessage.extractIntFromPayload()
        parameters.index = index
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListAddWithIndexCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListAddWithIndexCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListAddWithIndexCodec.ResponseParameters()

        return parameters

class ListClearCodec:
    REQUEST_TYPE = ListMessageType.LIST_CLEAR
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListClearCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListClearCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(ListClearCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListClearCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListClearCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListClearCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListClearCodec.ResponseParameters()

        return parameters

class ListCompareAndRemoveAllCodec:
    REQUEST_TYPE = ListMessageType.LIST_COMPAREANDREMOVEALL
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListCompareAndRemoveAllCodec.REQUEST_TYPE
            self.name=None
            self.valueSet=None
    @classmethod
    def encodeRequest(cls, name, valueSet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListCompareAndRemoveAllCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(ListCompareAndRemoveAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(valueSet.size())
        for valueSet_item in valueSet:
            clientMessage.set(valueSet_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListCompareAndRemoveAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        valueSet=None
        valueSet_size = clientMessage.extractIntFromPayload()
        valueSet = []
        for i in range(valueSet_size):
            valueSet_item=None
            valueSet_item = clientMessage.extractBytesFromPayload()
            valueSet.append(valueSet_item)
        parameters.valueSet = valueSet
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListCompareAndRemoveAllCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListCompareAndRemoveAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListCompareAndRemoveAllCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

class ListCompareAndRetainAllCodec:
    REQUEST_TYPE = ListMessageType.LIST_COMPAREANDRETAINALL
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListCompareAndRetainAllCodec.REQUEST_TYPE
            self.name=None
            self.valueSet=None
    @classmethod
    def encodeRequest(cls, name, valueSet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListCompareAndRetainAllCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(ListCompareAndRetainAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(valueSet.size())
        for valueSet_item in valueSet:
            clientMessage.set(valueSet_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListCompareAndRetainAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        valueSet=None
        valueSet_size = clientMessage.extractIntFromPayload()
        valueSet = []
        for i in range(valueSet_size):
            valueSet_item=None
            valueSet_item = clientMessage.extractBytesFromPayload()
            valueSet.append(valueSet_item)
        parameters.valueSet = valueSet
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListCompareAndRetainAllCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListCompareAndRetainAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListCompareAndRetainAllCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

class ListContainsAllCodec:
    REQUEST_TYPE = ListMessageType.LIST_CONTAINSALL
    RESPONSE_TYPE = 101
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListContainsAllCodec.REQUEST_TYPE
            self.name=None
            self.valueSet=None
    @classmethod
    def encodeRequest(cls, name, valueSet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListContainsAllCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(ListContainsAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(valueSet.size())
        for valueSet_item in valueSet:
            clientMessage.set(valueSet_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListContainsAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        valueSet=None
        valueSet_size = clientMessage.extractIntFromPayload()
        valueSet = []
        for i in range(valueSet_size):
            valueSet_item=None
            valueSet_item = clientMessage.extractBytesFromPayload()
            valueSet.append(valueSet_item)
        parameters.valueSet = valueSet
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListContainsAllCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListContainsAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListContainsAllCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

class ListContainsCodec:
    REQUEST_TYPE = ListMessageType.LIST_CONTAINS
    RESPONSE_TYPE = 101
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListContainsCodec.REQUEST_TYPE
            self.name=None
            self.value=None
    @classmethod
    def encodeRequest(cls, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListContainsCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(ListContainsCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListContainsCodec.RequestParameters()
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
            self.TYPE = ListContainsCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListContainsCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListContainsCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

class ListGetAllCodec:
    REQUEST_TYPE = ListMessageType.LIST_GETALL
    RESPONSE_TYPE = 106
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListGetAllCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListGetAllCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(ListGetAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListGetAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListGetAllCodec.RESPONSE_TYPE
            self.list=None
    @classmethod
    def encodeResponse(cls, list):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListGetAllCodec.RESPONSE_TYPE)
        clientMessage.set(list.size())
        for list_item in list:
            clientMessage.set(list_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListGetAllCodec.ResponseParameters()
        list=None
        list_size = clientMessage.extractIntFromPayload()
        list = []
        for i in range(list_size):
            list_item=None
            list_item = clientMessage.extractBytesFromPayload()
            list.append(list_item)
        parameters.list = list

        return parameters

class ListGetCodec:
    REQUEST_TYPE = ListMessageType.LIST_GET
    RESPONSE_TYPE = 105
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListGetCodec.REQUEST_TYPE
            self.name=None
            self.index=None
    @classmethod
    def encodeRequest(cls, name, index):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListGetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListGetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(index)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListGetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        index=None
        index = clientMessage.extractIntFromPayload()
        parameters.index = index
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListGetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListGetCodec.RESPONSE_TYPE)
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
        parameters=ListGetCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

class ListIndexOfCodec:
    REQUEST_TYPE = ListMessageType.LIST_INDEXOF
    RESPONSE_TYPE = 102
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListIndexOfCodec.REQUEST_TYPE
            self.name=None
            self.value=None
    @classmethod
    def encodeRequest(cls, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListIndexOfCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListIndexOfCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListIndexOfCodec.RequestParameters()
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
            self.TYPE = ListIndexOfCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListIndexOfCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListIndexOfCodec.ResponseParameters()
        response=None
        response = clientMessage.extractIntFromPayload()
        parameters.response = response

        return parameters

class ListIsEmptyCodec:
    REQUEST_TYPE = ListMessageType.LIST_ISEMPTY
    RESPONSE_TYPE = 101
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListIsEmptyCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListIsEmptyCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListIsEmptyCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListIsEmptyCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListIsEmptyCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListIsEmptyCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListIsEmptyCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

class ListIteratorCodec:
    REQUEST_TYPE = ListMessageType.LIST_ITERATOR
    RESPONSE_TYPE = 106
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListIteratorCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListIteratorCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListIteratorCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListIteratorCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListIteratorCodec.RESPONSE_TYPE
            self.list=None
    @classmethod
    def encodeResponse(cls, list):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListIteratorCodec.RESPONSE_TYPE)
        clientMessage.set(list.size())
        for list_item in list:
            clientMessage.set(list_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListIteratorCodec.ResponseParameters()
        list=None
        list_size = clientMessage.extractIntFromPayload()
        list = []
        for i in range(list_size):
            list_item=None
            list_item = clientMessage.extractBytesFromPayload()
            list.append(list_item)
        parameters.list = list

        return parameters

class ListLastIndexOfCodec:
    REQUEST_TYPE = ListMessageType.LIST_LASTINDEXOF
    RESPONSE_TYPE = 102
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListLastIndexOfCodec.REQUEST_TYPE
            self.name=None
            self.value=None
    @classmethod
    def encodeRequest(cls, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListLastIndexOfCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListLastIndexOfCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListLastIndexOfCodec.RequestParameters()
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
            self.TYPE = ListLastIndexOfCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListLastIndexOfCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListLastIndexOfCodec.ResponseParameters()
        response=None
        response = clientMessage.extractIntFromPayload()
        parameters.response = response

        return parameters

class ListListIteratorCodec:
    REQUEST_TYPE = ListMessageType.LIST_LISTITERATOR
    RESPONSE_TYPE = 106
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListListIteratorCodec.REQUEST_TYPE
            self.name=None
            self.index=None
    @classmethod
    def encodeRequest(cls, name, index):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListListIteratorCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListListIteratorCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(index)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListListIteratorCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        index=None
        index = clientMessage.extractIntFromPayload()
        parameters.index = index
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListListIteratorCodec.RESPONSE_TYPE
            self.list=None
    @classmethod
    def encodeResponse(cls, list):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListListIteratorCodec.RESPONSE_TYPE)
        clientMessage.set(list.size())
        for list_item in list:
            clientMessage.set(list_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListListIteratorCodec.ResponseParameters()
        list=None
        list_size = clientMessage.extractIntFromPayload()
        list = []
        for i in range(list_size):
            list_item=None
            list_item = clientMessage.extractBytesFromPayload()
            list.append(list_item)
        parameters.list = list

        return parameters



class ListRemoveCodec:
    REQUEST_TYPE = ListMessageType.LIST_REMOVE
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListRemoveCodec.REQUEST_TYPE
            self.name=None
            self.value=None
    @classmethod
    def encodeRequest(cls, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListRemoveCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListRemoveCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListRemoveCodec.RequestParameters()
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
            self.TYPE = ListRemoveCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListRemoveCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListRemoveCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

class ListRemoveListenerCodec:
    REQUEST_TYPE = ListMessageType.LIST_REMOVELISTENER
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListRemoveListenerCodec.REQUEST_TYPE
            self.name=None
            self.registrationId=None
    @classmethod
    def encodeRequest(cls, name, registrationId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListRemoveListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListRemoveListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(registrationId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListRemoveListenerCodec.RequestParameters()
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
            self.TYPE = ListRemoveListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListRemoveListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListRemoveListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters

class ListRemoveWithIndexCodec:
    REQUEST_TYPE = ListMessageType.LIST_REMOVEWITHINDEX
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListRemoveWithIndexCodec.REQUEST_TYPE
            self.name=None
            self.index=None
    @classmethod
    def encodeRequest(cls, name, index):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListRemoveWithIndexCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListRemoveWithIndexCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(index)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListRemoveWithIndexCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        index=None
        index = clientMessage.extractIntFromPayload()
        parameters.index = index
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListRemoveWithIndexCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListRemoveWithIndexCodec.RESPONSE_TYPE)
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
        parameters=ListRemoveWithIndexCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

class ListSetCodec:
    REQUEST_TYPE = ListMessageType.LIST_SET
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListSetCodec.REQUEST_TYPE
            self.name=None
            self.index=None
            self.value=None
    @classmethod
    def encodeRequest(cls, name, index, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListSetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListSetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(index)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListSetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        index=None
        index = clientMessage.extractIntFromPayload()
        parameters.index = index
        value=None
        value = clientMessage.extractBytesFromPayload()
        parameters.value = value
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListSetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListSetCodec.RESPONSE_TYPE)
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
        parameters=ListSetCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters

class ListSizeCodec:
    REQUEST_TYPE = ListMessageType.LIST_SIZE
    RESPONSE_TYPE = 102
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListSizeCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListSizeCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListSizeCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListSizeCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListSizeCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListSizeCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListSizeCodec.ResponseParameters()
        response=None
        response = clientMessage.extractIntFromPayload()
        parameters.response = response

        return parameters

class ListSubCodec:
    REQUEST_TYPE = ListMessageType.LIST_SUB
    RESPONSE_TYPE = 106
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ListSubCodec.REQUEST_TYPE
            self.name=None
            self.fromm=None
            self.to=None
    @classmethod
    def encodeRequest(cls, name, fromm, to):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListSubCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ListSubCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(fromm)
        clientMessage.set(to)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ListSubCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        fromy=None
        fromy = clientMessage.extractIntFromPayload()
        parameters.fromm = fromy
        to=None
        to = clientMessage.extractIntFromPayload()
        parameters.to = to
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ListSubCodec.RESPONSE_TYPE
            self.list=None
    @classmethod
    def encodeResponse(cls, list):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ListSubCodec.RESPONSE_TYPE)
        clientMessage.set(list.size())
        for list_item in list:
            clientMessage.set(list_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ListSubCodec.ResponseParameters()
        list=None
        list_size = clientMessage.extractIntFromPayload()
        list = []
        for i in range(list_size):
            list_item=None
            list_item = clientMessage.extractBytesFromPayload()
            list.append(list_item)
        parameters.list = list

        return parameters

