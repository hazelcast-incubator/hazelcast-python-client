__author__ = 'Jonathan Brodie'
from hzclient.clientmessage import ClientMessage
from hzclient.codec import eventconstant
from util import util

class SetMessageType:
    SET_SIZE=0x0601
    SET_CONTAINS=0x0602
    SET_CONTAINSALL=0x0603
    SET_ADD=0x0604
    SET_REMOVE=0x0605
    SET_ADDALL=0x0606
    SET_COMPAREANDREMOVEALL=0x0607
    SET_COMPAREANDRETAINALL=0x0608
    SET_CLEAR=0x0609
    SET_GETALL=0x060a
    SET_ADDLISTENER=0x060b
    SET_REMOVELISTENER=0x060c
    SET_ISEMPTY=0x060d

    def ___init__(self, messageType):
        self.id = messageType

    def id(self):
        return self.id


class SetAddAllCodec:
    REQUEST_TYPE = SetMessageType.SET_ADDALL
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SetAddAllCodec.REQUEST_TYPE
            self.name=None
            self.valueList=None
    @classmethod
    def encodeRequest(cls, name, valueList):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetAddAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SetAddAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(valueList.size())
        for valueList_item in valueList:
            clientMessage.set(valueList_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SetAddAllCodec.RequestParameters()
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
            self.TYPE = SetAddAllCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetAddAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SetAddAllCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class SetAddCodec:
    REQUEST_TYPE = SetMessageType.SET_ADD
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SetAddCodec.REQUEST_TYPE
            self.name=None
            self.value=None
    @classmethod
    def encodeRequest(cls, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetAddCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SetAddCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SetAddCodec.RequestParameters()
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
            self.TYPE = SetAddCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetAddCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SetAddCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class SetAddListenerCodec:
    REQUEST_TYPE = SetMessageType.SET_ADDLISTENER
    RESPONSE_TYPE = 104
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SetAddListenerCodec.REQUEST_TYPE
            self.name=None
            self.includeValue=None
    @classmethod
    def encodeRequest(cls, name, includeValue):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetAddListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SetAddListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(includeValue)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SetAddListenerCodec.RequestParameters()
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
            self.TYPE = SetAddListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetAddListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SetAddListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response

        return parameters



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
                    return

class SetClearCodec:
    REQUEST_TYPE = SetMessageType.SET_CLEAR
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SetClearCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetClearCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SetClearCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SetClearCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = SetClearCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetClearCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SetClearCodec.ResponseParameters()

        return parameters


class SetCompareAndRemoveAllCodec:
    REQUEST_TYPE = SetMessageType.SET_COMPAREANDREMOVEALL
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SetCompareAndRemoveAllCodec.REQUEST_TYPE
            self.name=None
            self.valueSet=None
    @classmethod
    def encodeRequest(cls, name, valueSet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetCompareAndRemoveAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SetCompareAndRemoveAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(valueSet.size())
        for valueSet_item in valueSet:
            clientMessage.set(valueSet_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SetCompareAndRemoveAllCodec.RequestParameters()
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
            self.TYPE = SetCompareAndRemoveAllCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetCompareAndRemoveAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SetCompareAndRemoveAllCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class SetCompareAndRetainAllCodec:
    REQUEST_TYPE = SetMessageType.SET_COMPAREANDRETAINALL
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SetCompareAndRetainAllCodec.REQUEST_TYPE
            self.name=None
            self.valueSet=None
    @classmethod
    def encodeRequest(cls, name, valueSet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetCompareAndRetainAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SetCompareAndRetainAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(valueSet.size())
        for valueSet_item in valueSet:
            clientMessage.set(valueSet_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SetCompareAndRetainAllCodec.RequestParameters()
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
            self.TYPE = SetCompareAndRetainAllCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetCompareAndRetainAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SetCompareAndRetainAllCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class SetContainsAllCodec:
    REQUEST_TYPE = SetMessageType.SET_CONTAINSALL
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SetContainsAllCodec.REQUEST_TYPE
            self.name=None
            self.valueSet=None
    @classmethod
    def encodeRequest(cls, name, valueSet):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetContainsAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SetContainsAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(valueSet.size())
        for valueSet_item in valueSet:
            clientMessage.set(valueSet_item)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SetContainsAllCodec.RequestParameters()
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
            self.TYPE = SetContainsAllCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetContainsAllCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SetContainsAllCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class SetContainsCodec:
    REQUEST_TYPE = SetMessageType.SET_CONTAINS
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SetContainsCodec.REQUEST_TYPE
            self.name=None
            self.value=None
    @classmethod
    def encodeRequest(cls, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetContainsCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SetContainsCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SetContainsCodec.RequestParameters()
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
            self.TYPE = SetContainsCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetContainsCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SetContainsCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class SetGetAllCodec:
    REQUEST_TYPE = SetMessageType.SET_GETALL
    RESPONSE_TYPE = 106
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SetGetAllCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetGetAllCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SetGetAllCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SetGetAllCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = SetGetAllCodec.RESPONSE_TYPE
            self.list=None
    @classmethod
    def encodeResponse(cls, list):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetGetAllCodec.RESPONSE_TYPE)
        clientMessage.set(list.size())
        for list_item in list:
            clientMessage.set(list_item)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SetGetAllCodec.ResponseParameters()
        list=None
        list_size = clientMessage.extractIntFromPayload()
        list = []
        for i in range(list_size):
            list_item=None
        list_item = clientMessage.extractBytesFromPayload()
        list.append(list_item)
        parameters.list = list

        return parameters


class SetIsEmptyCodec:
    REQUEST_TYPE = SetMessageType.SET_ISEMPTY
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SetIsEmptyCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetIsEmptyCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SetIsEmptyCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SetIsEmptyCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = SetIsEmptyCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetIsEmptyCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SetIsEmptyCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters



class SetRemoveCodec:
    REQUEST_TYPE = SetMessageType.SET_REMOVE
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SetRemoveCodec.REQUEST_TYPE
            self.name=None
            self.value=None
    @classmethod
    def encodeRequest(cls, name, value):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetRemoveCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SetRemoveCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(value)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SetRemoveCodec.RequestParameters()
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
            self.TYPE = SetRemoveCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetRemoveCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SetRemoveCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class SetRemoveListenerCodec:
    REQUEST_TYPE = SetMessageType.SET_REMOVELISTENER
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SetRemoveListenerCodec.REQUEST_TYPE
            self.name=None
            self.registrationId=None
    @classmethod
    def encodeRequest(cls, name, registrationId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetRemoveListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SetRemoveListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(registrationId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SetRemoveListenerCodec.RequestParameters()
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
            self.TYPE = SetRemoveListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetRemoveListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SetRemoveListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class SetSizeCodec:
    REQUEST_TYPE = SetMessageType.SET_SIZE
    RESPONSE_TYPE = 102
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SetSizeCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetSizeCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SetSizeCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SetSizeCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = SetSizeCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SetSizeCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SetSizeCodec.ResponseParameters()
        response=None
        response = clientMessage.extractIntFromPayload()
        parameters.response = response

        return parameters
