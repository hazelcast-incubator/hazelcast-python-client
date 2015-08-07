__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util
import eventconstant

class TopicMessageType:
    TOPIC_PUBLISH=0x0401
    TOPIC_ADDMESSAGELISTENER=0x0402
    TOPIC_REMOVEMESSAGELISTENER=0x0403
    id=None

    def ___init__(self, messageType):
        self.id = messageType

    def id(self):
        return self.id


'''
PUBLISH
'''
class TopicPublishCodec:
    REQUEST_TYPE = TopicMessageType.TOPIC_PUBLISH
    RESPONSE_TYPE = 100
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = TopicPublishCodec.REQUEST_TYPE
            name=None
            message=None
    @classmethod
    def encodeRequest(cls, name, message):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(TopicPublishCodec.REQUEST_TYPE)
        clientMessage.setRetryable(TopicPublishCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(message)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = TopicPublishCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        message=None
        message = clientMessage.extractBytesFromPayload()
        parameters.message = message
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = TopicPublishCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(TopicPublishCodec.RESPONSE_TYPE)
        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=TopicPublishCodec.ResponseParameters()
        return parameters

'''
ADDMESSAGELISTENER
'''


class TopicAddMessageListenerCodec:
    REQUEST_TYPE = TopicMessageType.TOPIC_ADDMESSAGELISTENER
    RESPONSE_TYPE = 104
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = TopicAddMessageListenerCodec.REQUEST_TYPE
            name=None
    @classmethod
    def encodeRequest(cls, name):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(TopicAddMessageListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(TopicAddMessageListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = TopicAddMessageListenerCodec.RequestParameters()
        name=None
        name = clientMessage.extractStringFromPayload()
        parameters.name = name
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            TYPE = TopicAddMessageListenerCodec.RESPONSE_TYPE
            response=None

    @classmethod
    def encodeResponse(cls,response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(TopicAddMessageListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)
        return clientMessage

    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=TopicAddMessageListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response
        return parameters


    '''************************ EVENTS *************************'''


    def encodeTopicEvent(cls, item, publishTime,uuid):
        clientMessage=ClientMessage()
        clientMessage.setOperationType(eventconstant.EVENT_TOPIC)
        clientMessage.setEventFlag()
        clientMessage.set(item)
        clientMessage.set(publishTime)
        clientMessage.set(uuid)
        return clientMessage

    class EventHandler:
        def __init__(self,handler):
            self.handler=handler

        def handle(self, clientMessage):
            messageType = clientMessage.getOperationType()
            if (messageType == eventconstant.EVENT_TOPIC):
                item=None
                item = clientMessage.extractBytesFromPayload()
                publishTime=None
                publishTime = clientMessage.extractLongFromPayload()
                uuid=None
                uuid = clientMessage.extractStringFromPayload()
                self.handler.handle(item, publishTime, uuid)
                return


class TopicRemoveMessageListenerCodec:
    REQUEST_TYPE = TopicMessageType.TOPIC_REMOVEMESSAGELISTENER
    RESPONSE_TYPE = 101
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            TYPE = TopicRemoveMessageListenerCodec.REQUEST_TYPE
            name=None
            registrationId=None

    @classmethod
    def encodeRequest(cls, name, registrationId):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(TopicRemoveMessageListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(TopicRemoveMessageListenerCodec.RETRYABLE)
        clientMessage.set(name)
        clientMessage.set(registrationId)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = TopicRemoveMessageListenerCodec.RequestParameters()
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
            TYPE = TopicRemoveMessageListenerCodec.RESPONSE_TYPE
            response=None

    @classmethod
    def encodeResponse(cls,response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(TopicRemoveMessageListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)
        return clientMessage

    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=TopicRemoveMessageListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractBooleanFromPayload()
        parameters.response = response
        return parameters


