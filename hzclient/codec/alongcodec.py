__author__ = 'Jonathan Brodie'

import ctypes
from hzclient.clientmessage import ClientMessage
from util import util
import eventconstant

class AtomicLongAddAndGetCodec:
    REQUEST_TYPE = AtomicLongMessageType.ATOMICLONG_ADDANDGET
    RESPONSE_TYPE = 103
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicLongAddAndGetCodec.REQUEST_TYPE
            self.name=None
            self.delta=None
    @classmethod
    def encodeRequest(cls, name, delta):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongAddAndGetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicLongAddAndGetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(delta)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicLongAddAndGetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        delta=None
        delta = clientMessage.extractLongFromPayload()
        parameters.delta = delta
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicLongAddAndGetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongAddAndGetCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicLongAddAndGetCodec.ResponseParameters()
        response=None
        response = clientMessage.extractLongFromPayload()
        parameters.response = response
        return parameters


class AtomicLongAlterAndGetCodec:
    REQUEST_TYPE = AtomicLongMessageType.ATOMICLONG_ALTERANDGET
    RESPONSE_TYPE = 103
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicLongAlterAndGetCodec.REQUEST_TYPE
            self.name=None
            self.function=None
    @classmethod
    def encodeRequest(cls, name, function):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongAlterAndGetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicLongAlterAndGetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(function)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicLongAlterAndGetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        function=None
        function = clientMessage.extractBytesFromPayload()
        parameters.function = function
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicLongAlterAndGetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongAlterAndGetCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicLongAlterAndGetCodec.ResponseParameters()
        response=None
        response = clientMessage.extractLongFromPayload()
        parameters.response = response

        return parameters


class AtomicLongAlterCodec:
    REQUEST_TYPE = AtomicLongMessageType.ATOMICLONG_ALTER
    RESPONSE_TYPE = 103
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicLongAlterCodec.REQUEST_TYPE
            self.name=None
            self.function=None
    @classmethod
    def encodeRequest(cls, name, function):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongAlterCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicLongAlterCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(function)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicLongAlterCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        function=None
        function = clientMessage.extractBytesFromPayload()
        parameters.function = function
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicLongAlterCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongAlterCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicLongAlterCodec.ResponseParameters()
        response=None
        response = clientMessage.extractLongFromPayload()
        parameters.response = response

        return parameters


class AtomicLongApplyCodec:
    REQUEST_TYPE = AtomicLongMessageType.ATOMICLONG_APPLY
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicLongApplyCodec.REQUEST_TYPE
            self.name=None
            self.function=None
    @classmethod
    def encodeRequest(cls, name, function):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongApplyCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicLongApplyCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(function)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicLongApplyCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        function=None
        function = clientMessage.extractBytesFromPayload()
        parameters.function = function
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicLongApplyCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongApplyCodec.RESPONSE_TYPE)
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
        parameters=AtomicLongApplyCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters


class AtomicLongCompareAndSetCodec:
    REQUEST_TYPE = AtomicLongMessageType.ATOMICLONG_COMPAREANDSET
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicLongCompareAndSetCodec.REQUEST_TYPE
            self.name=None
            self.expected=None
            self.updated=None
    @classmethod
    def encodeRequest(cls, name, expected, updated):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongCompareAndSetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicLongCompareAndSetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(expected)
        clientMessage.set(updated)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicLongCompareAndSetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        expected=None
        expected = clientMessage.extractLongFromPayload()
        parameters.expected = expected
        updated=None
        updated = clientMessage.extractLongFromPayload()
        parameters.updated = updated
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicLongCompareAndSetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongCompareAndSetCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicLongCompareAndSetCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class AtomicLongDecrementAndGetCodec:
    REQUEST_TYPE = AtomicLongMessageType.ATOMICLONG_DECREMENTANDGET
    RESPONSE_TYPE = 103
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicLongDecrementAndGetCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongDecrementAndGetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicLongDecrementAndGetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicLongDecrementAndGetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicLongDecrementAndGetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongDecrementAndGetCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicLongDecrementAndGetCodec.ResponseParameters()
        response=None
        response = clientMessage.extractLongFromPayload()
        parameters.response = response

        return parameters


class AtomicLongGetAndAddCodec:
    REQUEST_TYPE = AtomicLongMessageType.ATOMICLONG_GETANDADD
    RESPONSE_TYPE = 103
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicLongGetAndAddCodec.REQUEST_TYPE
            self.name=None
            self.delta=None
    @classmethod
    def encodeRequest(cls, name, delta):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongGetAndAddCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicLongGetAndAddCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(delta)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicLongGetAndAddCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        delta=None
        delta = clientMessage.extractLongFromPayload()
        parameters.delta = delta
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicLongGetAndAddCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongGetAndAddCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicLongGetAndAddCodec.ResponseParameters()
        response=None
        response = clientMessage.extractLongFromPayload()
        parameters.response = response

        return parameters


class AtomicLongGetAndAlterCodec:
    REQUEST_TYPE = AtomicLongMessageType.ATOMICLONG_GETANDALTER
    RESPONSE_TYPE = 103
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicLongGetAndAlterCodec.REQUEST_TYPE
            self.name=None
            self.function=None
    @classmethod
    def encodeRequest(cls, name, function):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongGetAndAlterCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicLongGetAndAlterCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(function)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicLongGetAndAlterCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        function=None
        function = clientMessage.extractBytesFromPayload()
        parameters.function = function
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicLongGetAndAlterCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongGetAndAlterCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicLongGetAndAlterCodec.ResponseParameters()
        response=None
        response = clientMessage.extractLongFromPayload()
        parameters.response = response

        return parameters


class AtomicLongGetAndIncrementCodec:
    REQUEST_TYPE = AtomicLongMessageType.ATOMICLONG_GETANDINCREMENT
    RESPONSE_TYPE = 103
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicLongGetAndIncrementCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongGetAndIncrementCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicLongGetAndIncrementCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicLongGetAndIncrementCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicLongGetAndIncrementCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongGetAndIncrementCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicLongGetAndIncrementCodec.ResponseParameters()
        response=None
        response = clientMessage.extractLongFromPayload()
        parameters.response = response

        return parameters


class AtomicLongGetAndSetCodec:
    REQUEST_TYPE = AtomicLongMessageType.ATOMICLONG_GETANDSET
    RESPONSE_TYPE = 103
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicLongGetAndSetCodec.REQUEST_TYPE
            self.name=None
            self.newValue=None
    @classmethod
    def encodeRequest(cls, name, newValue):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongGetAndSetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicLongGetAndSetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(newValue)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicLongGetAndSetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        newValue=None
        newValue = clientMessage.extractLongFromPayload()
        parameters.newValue = newValue
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicLongGetAndSetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongGetAndSetCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicLongGetAndSetCodec.ResponseParameters()
        response=None
        response = clientMessage.extractLongFromPayload()
        parameters.response = response

        return parameters


class AtomicLongGetCodec:
    REQUEST_TYPE = AtomicLongMessageType.ATOMICLONG_GET
    RESPONSE_TYPE = 103
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicLongGetCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongGetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicLongGetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicLongGetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicLongGetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongGetCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicLongGetCodec.ResponseParameters()
        response=None
        response = clientMessage.extractLongFromPayload()
        parameters.response = response

        return parameters


class AtomicLongIncrementAndGetCodec:
    REQUEST_TYPE = AtomicLongMessageType.ATOMICLONG_INCREMENTANDGET
    RESPONSE_TYPE = 103
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicLongIncrementAndGetCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongIncrementAndGetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicLongIncrementAndGetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicLongIncrementAndGetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicLongIncrementAndGetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongIncrementAndGetCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicLongIncrementAndGetCodec.ResponseParameters()
        response=None
        response = clientMessage.extractLongFromPayload()
        parameters.response = response

        return parameters


class AtomicLongMessageType:
    ATOMICLONG_APPLY=0x0a01
    ATOMICLONG_ALTER=0x0a02
    ATOMICLONG_ALTERANDGET=0x0a03
    ATOMICLONG_GETANDALTER=0x0a04
    ATOMICLONG_ADDANDGET=0x0a05
    ATOMICLONG_COMPAREANDSET=0x0a06
    ATOMICLONG_DECREMENTANDGET=0x0a07
    ATOMICLONG_GET=0x0a08
    ATOMICLONG_GETANDADD=0x0a09
    ATOMICLONG_GETANDSET=0x0a0a
    ATOMICLONG_INCREMENTANDGET=0x0a0b
    ATOMICLONG_GETANDINCREMENT=0x0a0c
    ATOMICLONG_SET=0x0a0d

    def ___init__(self, messageType):
        self.id = messageType

    def id(self):
        return self.id


class AtomicLongSetCodec:
    REQUEST_TYPE = AtomicLongMessageType.ATOMICLONG_SET
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicLongSetCodec.REQUEST_TYPE
            self.name=None
            self.newValue=None
    @classmethod
    def encodeRequest(cls, name, newValue):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongSetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicLongSetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(newValue)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicLongSetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        newValue=None
        newValue = clientMessage.extractLongFromPayload()
        parameters.newValue = newValue
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicLongSetCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicLongSetCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicLongSetCodec.ResponseParameters()

        return parameters


