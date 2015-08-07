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
        self.connection.sendPackage(firstpack.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(firstpack.correlation,False)
        newresponse=ClientMessage.decodeMessage(response)
        print newresponse.payload
        if response is not None:
            print "Initialized and connected proxy!"
        else:
            print "Unable to connect to server."
        print datetime.datetime.now()

    def publish(self,data):
        msg=topiccodec.TopicPublishCodec.encodeRequest(encode.encodestring(self.title),data)
        msg.partition=1
        retryable=msg.retryable
        self.connection.adjustCorrelationId(msg)
        correlationid=msg.correlation
        self.connection.sendPackage(msg.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(correlationid,True)
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

    def removeMessageListener(self):
        registrationId=None
        for key, value in self.connection.events.iteritems():
            if isinstance(topiccodec.TopicAddMessageListenerCodec.EventHandler,value):
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