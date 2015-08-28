__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util

class LockForceUnlockCodec:
    REQUEST_TYPE = LockMessageType.LOCK_FORCEUNLOCK
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = LockForceUnlockCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockForceUnlockCodec.REQUEST_TYPE)
        clientMessage.setRetryable(LockForceUnlockCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = LockForceUnlockCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = LockForceUnlockCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockForceUnlockCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=LockForceUnlockCodec.ResponseParameters()

        return parameters


class LockGetLockCountCodec:
    REQUEST_TYPE = LockMessageType.LOCK_GETLOCKCOUNT
    RESPONSE_TYPE = 102
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = LockGetLockCountCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockGetLockCountCodec.REQUEST_TYPE)
        clientMessage.setRetryable(LockGetLockCountCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = LockGetLockCountCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = LockGetLockCountCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockGetLockCountCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=LockGetLockCountCodec.ResponseParameters()
        response=None
        response = clientMessage.extractIntFromPayload()
        parameters.response = response

        return parameters


class LockGetRemainingLeaseTimeCodec:
    REQUEST_TYPE = LockMessageType.LOCK_GETREMAININGLEASETIME
    RESPONSE_TYPE = 103
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = LockGetRemainingLeaseTimeCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockGetRemainingLeaseTimeCodec.REQUEST_TYPE)
        clientMessage.setRetryable(LockGetRemainingLeaseTimeCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = LockGetRemainingLeaseTimeCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = LockGetRemainingLeaseTimeCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockGetRemainingLeaseTimeCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=LockGetRemainingLeaseTimeCodec.ResponseParameters()
        response=None
        response = clientMessage.extractLongFromPayload()
        parameters.response = response

        return parameters


class LockIsLockedByCurrentThreadCodec:
    REQUEST_TYPE = LockMessageType.LOCK_ISLOCKEDBYCURRENTTHREAD
    RESPONSE_TYPE = 101
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = LockIsLockedByCurrentThreadCodec.REQUEST_TYPE
            self.name=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockIsLockedByCurrentThreadCodec.REQUEST_TYPE)
        clientMessage.setRetryable(LockIsLockedByCurrentThreadCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = LockIsLockedByCurrentThreadCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = LockIsLockedByCurrentThreadCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockIsLockedByCurrentThreadCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=LockIsLockedByCurrentThreadCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class LockIsLockedCodec:
    REQUEST_TYPE = LockMessageType.LOCK_ISLOCKED
    RESPONSE_TYPE = 101
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = LockIsLockedCodec.REQUEST_TYPE
            self.name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockIsLockedCodec.REQUEST_TYPE)
        clientMessage.setRetryable(LockIsLockedCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = LockIsLockedCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = LockIsLockedCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockIsLockedCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=LockIsLockedCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class LockLockCodec:
    REQUEST_TYPE = LockMessageType.LOCK_LOCK
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = LockLockCodec.REQUEST_TYPE
            self.name=None
            self.leaseTime=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, leaseTime, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockLockCodec.REQUEST_TYPE)
        clientMessage.setRetryable(LockLockCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(leaseTime)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = LockLockCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        leaseTime=None
        leaseTime = clientMessage.extractLongFromPayload()
        parameters.leaseTime = leaseTime
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = LockLockCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockLockCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=LockLockCodec.ResponseParameters()

        return parameters


class LockMessageType:
    LOCK_ISLOCKED=0x0701
    LOCK_ISLOCKEDBYCURRENTTHREAD=0x0702
    LOCK_GETLOCKCOUNT=0x0703
    LOCK_GETREMAININGLEASETIME=0x0704
    LOCK_LOCK=0x0705
    LOCK_UNLOCK=0x0706
    LOCK_FORCEUNLOCK=0x0707
    LOCK_TRYLOCK=0x0708

    def ___init__(self, messageType):
        self.id = messageType

    def id(self):
        return self.id
class LockTryLockCodec:
    REQUEST_TYPE = LockMessageType.LOCK_TRYLOCK
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = LockTryLockCodec.REQUEST_TYPE
            self.name=None
            self.threadId=None
            self.lease=None
            self.timeout=None
    @classmethod
    def encodeRequest(cls, name, threadId, lease, timeout):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockTryLockCodec.REQUEST_TYPE)
        clientMessage.setRetryable(LockTryLockCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(threadId)
        clientMessage.set(lease)
        clientMessage.set(timeout)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = LockTryLockCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
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
            self.TYPE = LockTryLockCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockTryLockCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=LockTryLockCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response

        return parameters


class LockUnlockCodec:
    REQUEST_TYPE = LockMessageType.LOCK_UNLOCK
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = LockUnlockCodec.REQUEST_TYPE
            self.name=None
            self.threadId=None
    @classmethod
    def encodeRequest(cls, name, threadId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockUnlockCodec.REQUEST_TYPE)
        clientMessage.setRetryable(LockUnlockCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(threadId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = LockUnlockCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        threadId=None
        threadId = clientMessage.extractLongFromPayload()
        parameters.threadId = threadId
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = LockUnlockCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(LockUnlockCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=LockUnlockCodec.ResponseParameters()

        return parameters


