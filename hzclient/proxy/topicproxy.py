__author__ = 'jonathanbrodie'
from hzclient.codec import proxycodec
from hzclient.codec import topiccodec
from hzclient.clientmessage import ClientMessage
from util import encode


class TopicProxy(object):
    def __init__(self,title,connfamily):
        self.title=title
        self.connection=connfamily
        firstpack=proxycodec.createProxy(self.title,"hz:impl:topicService")
        self.connection.adjustCorrelationId(firstpack)
        self.connection.sendPackage(firstpack.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(firstpack.correlation,True)
        if response is not None:
            print "Initialized and connected proxy!"
        else:
            print "Unable to connect to server."

    def publish(self,data):
        msg=topiccodec.TopicPublishCodec.encodeRequest(encode.encodestring(self.title),data)
        msg.partition=1
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(msg.correlation,True)
        msg2=ClientMessage.decodeMessage(response)

        return topiccodec.TopicPublishCodec.decodeResponse(msg2)

    def addMessageListener(self):
        msg=topiccodec.TopicAddMessageListenerCodec.encodeRequest(self.title)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(msg.correlation,retryable)
        self.connection.events[correlationid]=topiccodec.TopicAddMessageListenerCodec.AbstractEventHandler
        if response is not None:
            self.connection.events[correlationid]=topiccodec.TopicAddMessageListenerCodec.AbstractEventHandler()
        msg2=ClientMessage.decodeMessage(response)
        return topiccodec.TopicAddMessageListenerCodec.decodeResponse(msg2)

    def removeMessageListener(self):
        registrationId=None
        for key, value in self.connection.events.iteritems():
            if value is topiccodec.TopicAddMessageListenerCodec.AbstractEventHandler():
                registrationId=key
        msg=topiccodec.TopicRemoveMessageListenerCodec.encodeRequest(self.title,registrationId)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(msg.correlation,retryable)
        msg2=ClientMessage.decodeMessage(response)

        self.connection.events.pop(registrationId)
        return topiccodec.TopicPublishCodec.decodeResponse(msg2)