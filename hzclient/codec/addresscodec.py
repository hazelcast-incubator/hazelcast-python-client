__author__ = 'jonathanbrodie'
from hzclient.clientmessage import ClientMessage
'''
Python version of com.hazelcast.nio.Address and its codec
'''

class AddressCodec:
    @classmethod
    def decode(cls,clientmsg):
        host=clientmsg.extractStringFromPayload()
        port=clientmsg.extractIntFromPayload()
        return Address(host,port)

'''
Partial implementation for address
'''
class Address(object):
    def __init__(self,host,port):
        self.host=host
        self.port=port
