import ctypes
from hzclient.clientmessage import ClientMessage
from util import util
import eventconstant


class AtomicReferenceAlterAndGetCodec:
    REQUEST_TYPE = AtomicReferenceMessageType.ATOMICREFERENCE_ALTERANDGET
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceAlterAndGetCodec.REQUEST_TYPE
            self.name=None
            self.function=None
    @classmethod
    def encodeRequest(cls, name, function):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceAlterAndGetCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(AtomicReferenceAlterAndGetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(function)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicReferenceAlterAndGetCodec.RequestParameters()
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
            self.TYPE = AtomicReferenceAlterAndGetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceAlterAndGetCodec.RESPONSE_TYPE)
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
        parameters=AtomicReferenceAlterAndGetCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters


class AtomicReferenceAlterCodec:
    REQUEST_TYPE = AtomicReferenceMessageType.ATOMICREFERENCE_ALTER
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceAlterCodec.REQUEST_TYPE
            self.name=None
            self.function=None
    @classmethod
    def encodeRequest(cls, name, function):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceAlterCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicReferenceAlterCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(function)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicReferenceAlterCodec.RequestParameters()
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
            self.TYPE = AtomicReferenceAlterCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceAlterCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicReferenceAlterCodec.ResponseParameters()

        return parameters


class AtomicReferenceApplyCodec:
    REQUEST_TYPE = AtomicReferenceMessageType.ATOMICREFERENCE_APPLY
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceApplyCodec.REQUEST_TYPE
            self.name=None
            self.function=None
    @classmethod
    def encodeRequest(cls, name, function):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceApplyCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicReferenceApplyCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(function)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicReferenceApplyCodec.RequestParameters()
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
            self.TYPE = AtomicReferenceApplyCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceApplyCodec.RESPONSE_TYPE)
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
        parameters=AtomicReferenceApplyCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters


class AtomicReferenceClearCodec:
    REQUEST_TYPE = AtomicReferenceMessageType.ATOMICREFERENCE_CLEAR
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceClearCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceClearCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicReferenceClearCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicReferenceClearCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceClearCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceClearCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicReferenceClearCodec.ResponseParameters()

        return parameters


class AtomicReferenceCompareAndSetCodec:
    REQUEST_TYPE = AtomicReferenceMessageType.ATOMICREFERENCE_COMPAREANDSET
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceCompareAndSetCodec.REQUEST_TYPE
            self.name=None
            self.expected=None
            self.updated=None
    @classmethod
    def encodeRequest(cls, name, expected, updated):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceCompareAndSetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicReferenceCompareAndSetCodec.RETRYABLE)
        clientMessage.set(name)
        expected_isNull=None
        if expected is None:
            expected_isNull = True
            clientMessage.set(expected_isNull)
        else:
            expected_isNull= False
            clientMessage.set(expected_isNull)
        clientMessage.set(expected)
        updated_isNull=None
        if updated is None:
            updated_isNull = True
            clientMessage.set(updated_isNull)
        else:
            updated_isNull= False
            clientMessage.set(updated_isNull)
        clientMessage.set(updated)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicReferenceCompareAndSetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        expected=None
        expected_isNull = clientMessage.extractBooleanFromPayload()
        if not expected_isNull:
            expected = clientMessage.extractBytesFromPayload()
        parameters.expected = expected
        updated=None
        updated_isNull = clientMessage.extractBooleanFromPayload()
        if not updated_isNull:
            updated = clientMessage.extractBytesFromPayload()
        parameters.updated = updated
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceCompareAndSetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceCompareAndSetCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicReferenceCompareAndSetCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class AtomicReferenceContainsCodec:
    REQUEST_TYPE = AtomicReferenceMessageType.ATOMICREFERENCE_CONTAINS
    RESPONSE_TYPE = 101
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceContainsCodec.REQUEST_TYPE
            self.name=None
            self.expected=None
    @classmethod
    def encodeRequest(cls, name, expected):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceContainsCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicReferenceContainsCodec.RETRYABLE)
        clientMessage.set(name)
        expected_isNull=None
        if expected is None:
            expected_isNull = True
            clientMessage.set(expected_isNull)
        else:
            expected_isNull= False
            clientMessage.set(expected_isNull)
        clientMessage.set(expected)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicReferenceContainsCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        expected=None
        expected_isNull = clientMessage.extractBooleanFromPayload()
        if not expected_isNull:
            expected = clientMessage.extractBytesFromPayload()
        parameters.expected = expected
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceContainsCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceContainsCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicReferenceContainsCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class AtomicReferenceGetAndAlterCodec:
    REQUEST_TYPE = AtomicReferenceMessageType.ATOMICREFERENCE_GETANDALTER
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceGetAndAlterCodec.REQUEST_TYPE
            self.name=None
            self.function=None
    @classmethod
    def encodeRequest(cls, name, function):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceGetAndAlterCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicReferenceGetAndAlterCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(function)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicReferenceGetAndAlterCodec.RequestParameters()
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
            self.TYPE = AtomicReferenceGetAndAlterCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceGetAndAlterCodec.RESPONSE_TYPE)
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
        parameters=AtomicReferenceGetAndAlterCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters


class AtomicReferenceGetAndSetCodec:
    REQUEST_TYPE = AtomicReferenceMessageType.ATOMICREFERENCE_GETANDSET
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceGetAndSetCodec.REQUEST_TYPE
            self.name=None
            self.newValue=None
    @classmethod
    def encodeRequest(cls, name, newValue):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceGetAndSetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicReferenceGetAndSetCodec.RETRYABLE)
        clientMessage.set(name)
        newValue_isNull=None
        if newValue is None:
            newValue_isNull = True
            clientMessage.set(newValue_isNull)
        else:
            newValue_isNull= False
            clientMessage.set(newValue_isNull)
        clientMessage.set(newValue)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicReferenceGetAndSetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        newValue=None
        newValue_isNull = clientMessage.extractBooleanFromPayload()
        if not newValue_isNull:
            newValue = clientMessage.extractBytesFromPayload()
        parameters.newValue = newValue
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceGetAndSetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceGetAndSetCodec.RESPONSE_TYPE)
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
        parameters=AtomicReferenceGetAndSetCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters


class AtomicReferenceGetCodec:
    REQUEST_TYPE = AtomicReferenceMessageType.ATOMICREFERENCE_GET
    RESPONSE_TYPE = 105
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceGetCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceGetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicReferenceGetCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicReferenceGetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceGetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceGetCodec.RESPONSE_TYPE)
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
        parameters=AtomicReferenceGetCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters


class AtomicReferenceIsNullCodec:
    REQUEST_TYPE = AtomicReferenceMessageType.ATOMICREFERENCE_ISNULL
    RESPONSE_TYPE = 101
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceIsNullCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceIsNullCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicReferenceIsNullCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicReferenceIsNullCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceIsNullCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceIsNullCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicReferenceIsNullCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class AtomicReferenceMessageType:
    ATOMICREFERENCE_APPLY=0x0b01
    ATOMICREFERENCE_ALTER=0x0b02
    ATOMICREFERENCE_ALTERANDGET=0x0b03
    ATOMICREFERENCE_GETANDALTER=0x0b04
    ATOMICREFERENCE_CONTAINS=0x0b05
    ATOMICREFERENCE_COMPAREANDSET=0x0b06
    ATOMICREFERENCE_GET=0x0b08
    ATOMICREFERENCE_SET=0x0b09
    ATOMICREFERENCE_CLEAR=0x0b0a
    ATOMICREFERENCE_GETANDSET=0x0b0b
    ATOMICREFERENCE_SETANDGET=0x0b0c
    ATOMICREFERENCE_ISNULL=0x0b0d

    def ___init__(self, messageType):
        self.id = messageType

    def id(self):
        return self.id
class AtomicReferenceSetAndGetCodec:
    REQUEST_TYPE = AtomicReferenceMessageType.ATOMICREFERENCE_SETANDGET
    RESPONSE_TYPE = 105
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceSetAndGetCodec.REQUEST_TYPE
            self.name=None
            self.newValue=None
    @classmethod
    def encodeRequest(cls, name, newValue):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceSetAndGetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicReferenceSetAndGetCodec.RETRYABLE)
        clientMessage.set(name)
        newValue_isNull=None
        if newValue is None:
            newValue_isNull = True
            clientMessage.set(newValue_isNull)
        else:
            newValue_isNull= False
            clientMessage.set(newValue_isNull)
        clientMessage.set(newValue)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicReferenceSetAndGetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        newValue=None
        newValue_isNull = clientMessage.extractBooleanFromPayload()
        if not newValue_isNull:
            newValue = clientMessage.extractBytesFromPayload()
        parameters.newValue = newValue
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceSetAndGetCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceSetAndGetCodec.RESPONSE_TYPE)
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
        parameters=AtomicReferenceSetAndGetCodec.ResponseParameters()
        response=None
        response_isNull = clientMessage.extractBooleanFromPayload()
        if not response_isNull:
            response = clientMessage.extractBytesFromPayload()
        parameters.response = response

        return parameters


class AtomicReferenceSetCodec:
    REQUEST_TYPE = AtomicReferenceMessageType.ATOMICREFERENCE_SET
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceSetCodec.REQUEST_TYPE
            self.name=None
            self.newValue=None
    @classmethod
    def encodeRequest(cls, name, newValue):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceSetCodec.REQUEST_TYPE)
        clientMessage.setRetryable(AtomicReferenceSetCodec.RETRYABLE)
        clientMessage.set(name)
        newValue_isNull=None
        if newValue is None:
            newValue_isNull = True
            clientMessage.set(newValue_isNull)
        else:
            newValue_isNull= False
            clientMessage.set(newValue_isNull)
        clientMessage.set(newValue)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = AtomicReferenceSetCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        newValue=None
        newValue_isNull = clientMessage.extractBooleanFromPayload()
        if not newValue_isNull:
                newValue = clientMessage.extractBytesFromPayload()
        parameters.newValue = newValue
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = AtomicReferenceSetCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(AtomicReferenceSetCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=AtomicReferenceSetCodec.ResponseParameters()

        return parameters


