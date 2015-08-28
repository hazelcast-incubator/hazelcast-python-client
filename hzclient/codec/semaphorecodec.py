__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util
class SemaphoreAcquireCodec:
    REQUEST_TYPE = SemaphoreMessageType.SEMAPHORE_ACQUIRE
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SemaphoreAcquireCodec.REQUEST_TYPE
            self.name=None
            self.permits=None
    @classmethod
    def encodeRequest(cls, name, permits):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SemaphoreAcquireCodec.REQUEST_TYPE.id)
        clientMessage.setRetryable(SemaphoreAcquireCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(permits)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SemaphoreAcquireCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        permits=None
        permits = clientMessage.extractIntFromPayload()
        parameters.permits = permits
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = SemaphoreAcquireCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SemaphoreAcquireCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SemaphoreAcquireCodec.ResponseParameters()

        return parameters


class SemaphoreAvailablePermitsCodec:
    REQUEST_TYPE = SemaphoreMessageType.SEMAPHORE_AVAILABLEPERMITS
    RESPONSE_TYPE = 102
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SemaphoreAvailablePermitsCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SemaphoreAvailablePermitsCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SemaphoreAvailablePermitsCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SemaphoreAvailablePermitsCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = SemaphoreAvailablePermitsCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SemaphoreAvailablePermitsCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SemaphoreAvailablePermitsCodec.ResponseParameters()
        response=None
        response = clientMessage.extractIntFromPayload()
        parameters.response = response

        return parameters


class SemaphoreDrainPermitsCodec:
    REQUEST_TYPE = SemaphoreMessageType.SEMAPHORE_DRAINPERMITS
    RESPONSE_TYPE = 102
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SemaphoreDrainPermitsCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SemaphoreDrainPermitsCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SemaphoreDrainPermitsCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SemaphoreDrainPermitsCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = SemaphoreDrainPermitsCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SemaphoreDrainPermitsCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SemaphoreDrainPermitsCodec.ResponseParameters()
        response=None
        response = clientMessage.extractIntFromPayload()
        parameters.response = response

        return parameters


class SemaphoreInitCodec:
    REQUEST_TYPE = SemaphoreMessageType.SEMAPHORE_INIT
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SemaphoreInitCodec.REQUEST_TYPE
            self.name=None
            self.permits=None
    @classmethod
    def encodeRequest(cls, name, permits):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SemaphoreInitCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SemaphoreInitCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(permits)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SemaphoreInitCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        permits=None
        permits = clientMessage.extractIntFromPayload()
        parameters.permits = permits
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = SemaphoreInitCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SemaphoreInitCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SemaphoreInitCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response
        return parameters


class SemaphoreMessageType:
    SEMAPHORE_INIT=0x0d01
    SEMAPHORE_ACQUIRE=0x0d02
    SEMAPHORE_AVAILABLEPERMITS=0x0d03
    SEMAPHORE_DRAINPERMITS=0x0d04
    SEMAPHORE_REDUCEPERMITS=0x0d05
    SEMAPHORE_RELEASE=0x0d06
    SEMAPHORE_TRYACQUIRE=0x0d07
    id=None

    def ___init__(self, messageType):
        self.id = messageType

    def id(self):
        return self.id
class SemaphoreReducePermitsCodec:
    REQUEST_TYPE = SemaphoreMessageType.SEMAPHORE_REDUCEPERMITS
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SemaphoreReducePermitsCodec.REQUEST_TYPE
            self.name=None
            self.reduction=None
    @classmethod
    def encodeRequest(cls, name, reduction):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SemaphoreReducePermitsCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SemaphoreReducePermitsCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(reduction)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SemaphoreReducePermitsCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        reduction=None
        reduction = clientMessage.extractIntFromPayload()
        parameters.reduction = reduction
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = SemaphoreReducePermitsCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SemaphoreReducePermitsCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SemaphoreReducePermitsCodec.ResponseParameters()

        return parameters


class SemaphoreReleaseCodec:
    REQUEST_TYPE = SemaphoreMessageType.SEMAPHORE_RELEASE
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SemaphoreReleaseCodec.REQUEST_TYPE
            self.name=None
            self.permits=None
    @classmethod
    def encodeRequest(cls, name, permits):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SemaphoreReleaseCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SemaphoreReleaseCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(permits)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SemaphoreReleaseCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        permits=None
        permits = clientMessage.extractIntFromPayload()
        parameters.permits = permits
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = SemaphoreReleaseCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SemaphoreReleaseCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SemaphoreReleaseCodec.ResponseParameters()

        return parameters


class SemaphoreTryAcquireCodec:
    REQUEST_TYPE = SemaphoreMessageType.SEMAPHORE_TRYACQUIRE
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = SemaphoreTryAcquireCodec.REQUEST_TYPE
            self.name=None
            self.permits=None
            self.timeout=None
    @classmethod
    def encodeRequest(cls, name, permits, timeout):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SemaphoreTryAcquireCodec.REQUEST_TYPE)
        clientMessage.setRetryable(SemaphoreTryAcquireCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(permits)
        clientMessage.set(timeout)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = SemaphoreTryAcquireCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        permits=None
        permits = clientMessage.extractIntFromPayload()
        parameters.permits = permits
        timeout=None
        timeout = clientMessage.extractLongFromPayload()
        parameters.timeout = timeout
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = SemaphoreTryAcquireCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(SemaphoreTryAcquireCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=SemaphoreTryAcquireCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


