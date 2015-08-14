__author__ = 'jonathanbrodie'
from hzclient.codec.addresscodec import AddressCodec
class MemberCodec:
    @classmethod
    def decode(cls,clientMessage):
        address=AddressCodec.decode(clientMessage)
        uuid=clientMessage.extractStringFromPayload()
        attributeSize=clientMessage.extractIntFromPayload()
        map={}
        for i in range(attributeSize):
            key=clientMessage.extractStringFromPayload()
            value=clientMessage.extractStringFromPayload()
            map[key]=value
        return Member(address,uuid,map)
class MemberAttributeChangeCodec(object):
    @classmethod
    def decode(cls,clientmsg):
        uuid=clientmsg.extractStringFromPayload()
        key=clientmsg.extractStringFromPayload()
        optype=clientmsg.extractIntFromPayload()
        value=None
        if optype == 1:
            value=clientmsg.extractStringFromPayload()
        return MemberAttributeChange(uuid,optype,key,value)


class MemberAttributeChange(object):
    def __init__(self,uuid,optype,key,value):
        self.uuid=uuid
        self.optype=optype
        self.key=key
        self.value=value

class Member:
    def __init__(self,address,uuid,attributes):
        self.address=address
        self.uuid=uuid
        self.attributes=attributes
