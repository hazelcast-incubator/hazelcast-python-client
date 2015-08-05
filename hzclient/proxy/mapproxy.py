__author__ = 'jonathanbrodie'
from hzclient.codec import proxycodec
from hzclient.codec import topiccodec
from hzclient.clientmessage import ClientMessage

class MapProxy(object):
    def __init__(self,title,connfamily):
        self.title=title
        self.connection=connfamily
        firstpack=proxycodec.createProxy(self.title,"hz:impl:mapService")
        self.connection.sendPackage(firstpack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        if response is not None:
            print "Initialized and connected proxy!"
        else:
            print "Unable to connect to server."
