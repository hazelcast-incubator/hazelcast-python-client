__author__ = 'jonathanbrodie'
from hzclient.codec import proxycodec
from hzclient.codec import topiccodec
from hzclient.clientmessage import ClientMessage
from util import encode
import datetime

class TopicProxy(object):

    def __init__(self,title,connfamily):
        self.title=title
        self.connection=connfamily
        firstpack=proxycodec.createProxy(self.title,"hz:impl:topicService")
        self.connection.adjustCorrelationId(firstpack)
        self.connection.sendPackage(firstpack)
        response=self.connection.getPackageWithCorrelationId(firstpack.correlation,False)
        newresponse=ClientMessage.decodeMessage(response)
        if response is not None:
            print "Initialized and connected proxy!"
        else:
            print "Unable to connect to server."

    def publish(self,data):
        msg=topiccodec.TopicPublishCodec.encodeRequest(encode.encodestring(self.title),data)
        self.connection.adjustPartitionId(msg, data)
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg)
        response=self.connection.getPackageWithCorrelationId(correlationid,retryable)
        msg2=ClientMessage.decodeMessage(response)

        return topiccodec.TopicPublishCodec.decodeResponse(msg2)

    def addMessageListener(self,myeventlistener):
        msg=topiccodec.TopicAddMessageListenerCodec.encodeRequest(encode.encodestring(self.title))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(msg.correlation,retryable)
        self.connection.eventregistry[correlationid]=topiccodec.TopicAddMessageListenerCodec.EventHandler(myeventlistener)
        msg2=ClientMessage.decodeMessage(response)
        return topiccodec.TopicAddMessageListenerCodec.decodeResponse(msg2)

    def removeMessageListener(self,registrationId):
        msg=topiccodec.TopicRemoveMessageListenerCodec.encodeRequest(encode.encodestring(self.title),encode.encodestring(registrationId))
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(msg.correlation,retryable)
        msg2=ClientMessage.decodeMessage(response)

        self.connection.eventregistry.pop(registrationId)
        return topiccodec.TopicPublishCodec.decodeResponse(msg2)