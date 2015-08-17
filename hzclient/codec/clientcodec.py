__author__ = 'jonathanbrodie'
import eventconstant,ctypes
from hzclient.clientmessage import ClientMessage
from hzclient.codec.addresscodec import AddressCodec
from hzclient.codec.membercodec import MemberCodec
from hzclient.codec.membercodec import MemberAttributeChangeCodec

class ClientMessageType:
    CLIENT_AUTHENTICATION=0x2
    CLIENT_AUTHENTICATIONCUSTOM=0x3
    CLIENT_MEMBERSHIPLISTENER=0x4
    CLIENT_CREATEPROXY=0x5
    CLIENT_DESTROYPROXY=0x6
    CLIENT_GETPARTITIONS=0x8
    CLIENT_REMOVEALLLISTENERS=0x9
    CLIENT_ADDPARTITIONLOSTLISTENER=0xa
    CLIENT_REMOVEPARTITIONLOSTLISTENER=0xb
    CLIENT_GETDISTRIBUTEDOBJECT=0xc
    CLIENT_ADDDISTRIBUTEDOBJECTLISTENER=0xd
    CLIENT_REMOVEDISTRIBUTEDOBJECTLISTENER=0xe
    CLIENT_PING=0xf

    def ___init__(self, messageType):
        self.id = messageType

    def id(self):
        return self.id

class ClientAuthenticationCodec:
    REQUEST_TYPE = ClientMessageType.CLIENT_AUTHENTICATION
    RESPONSE_TYPE = 107
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ClientAuthenticationCodec.REQUEST_TYPE
            self.username=None
            self.password=None
            self.uuid=None
            self.ownerUuid=None
            self.isOwnerConnection=None
    @classmethod
    def encodeRequest(cls, username, password, uuid, ownerUuid, isOwnerConnection):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ClientAuthenticationCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ClientAuthenticationCodec.RETRYABLE)
        clientMessage.set(username)
        clientMessage.set(password)
        uuid_isNull=None
        if uuid is None:
            uuid_isNull = True
            uuid_isNull=bytearray(ctypes.c_uint8(uuid_isNull))
            clientMessage.set(uuid_isNull)

        else:
            uuid_isNull= False
            uuid_isNull=bytearray(ctypes.c_uint8(uuid_isNull))
            clientMessage.set(uuid_isNull)
            clientMessage.set(uuid)
        ownerUuid_isNull=None
        if ownerUuid is None:
            ownerUuid_isNull = True
            ownerUuid_isNull=bytearray(ctypes.c_uint8(ownerUuid_isNull))
            clientMessage.set(ownerUuid_isNull)
        else:
            ownerUuid_isNull= False
            ownerUuid_isNull=bytearray(ctypes.c_uint8(ownerUuid_isNull))

            clientMessage.set(ownerUuid_isNull)
            clientMessage.set(ownerUuid)

        clientMessage.set(isOwnerConnection)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ClientAuthenticationCodec.RequestParameters()
        username=None
        username = clientMessage.extractStringFromPayload()
        parameters.username = username
        password=None
        password = clientMessage.extractStringFromPayload()
        parameters.password = password
        uuid=None
        uuid_isNull = clientMessage.extractBooleanFromPayload()
        if not uuid_isNull:
            uuid = clientMessage.extractStringFromPayload()
        parameters.uuid = uuid
        ownerUuid=None
        ownerUuid_isNull = clientMessage.extractBooleanFromPayload()
        if not ownerUuid_isNull:
            ownerUuid = clientMessage.extractStringFromPayload()
        parameters.ownerUuid = ownerUuid
        isOwnerConnection=None
        isOwnerConnection = clientMessage.extractBooleanFromPayload()
        parameters.isOwnerConnection = isOwnerConnection
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ClientAuthenticationCodec.RESPONSE_TYPE
            self.address=None
            self.uuid=None
            self.ownerUuid=None

    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ClientAuthenticationCodec.ResponseParameters()
        address=None
        address = AddressCodec.decode(clientMessage)
        parameters.address = address
        uuid=None
        uuid = clientMessage.extractStringFromPayload()
        parameters.uuid = uuid
        ownerUuid=None
        ownerUuid = clientMessage.extractStringFromPayload()
        parameters.ownerUuid = ownerUuid

        return parameters

class ClientMembershipListenerCodec:
    REQUEST_TYPE = ClientMessageType.CLIENT_MEMBERSHIPLISTENER
    RESPONSE_TYPE = 104
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ClientMembershipListenerCodec.REQUEST_TYPE
    @classmethod
    def encodeRequest(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ClientMembershipListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ClientMembershipListenerCodec.RETRYABLE)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ClientMembershipListenerCodec.RequestParameters()
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ClientMembershipListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ClientMembershipListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ClientMembershipListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response

        return parameters


    '''************************ EVENTS *************************'''


    class EventHandler:
        def __init__(self,handler):
            self.handler=handler
        def handle(self, clientMessage):
            messageType = clientMessage.getOperationType()
            if (messageType == eventconstant.EVENT_MEMBER):
                member=None
                member = com.hazelcast.client.impl.protocol.codec.MemberCodec.decode(clientMessage)
                eventType=None
                eventType = clientMessage.extractIntFromPayload()
                self.handler.handle(member, eventType)
                return
            if (messageType == eventconstant.EVENT_MEMBERSET):
                members=None
                members_size = clientMessage.extractIntFromPayload()
                members = []
                for i in range(members_size):
                    members_item=None
                    members_item = MemberCodec.decode(clientMessage)
                    members.append(members_item)
                self.handler.handle(members)
                return
            if (messageType == eventconstant.EVENT_MEMBERATTRIBUTECHANGE):
                memberAttributeChange=None
                memberAttributeChange = MemberAttributeChangeCodec.decode(clientMessage)
                self.handler.handle(memberAttributeChange)
                return



class ClientGetPartitionsCodec:
    REQUEST_TYPE = ClientMessageType.CLIENT_GETPARTITIONS
    RESPONSE_TYPE = 108
    RETRYABLE = False

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ClientGetPartitionsCodec.REQUEST_TYPE
    @classmethod
    def encodeRequest(cls, ):
        """

        :rtype : ClientMessage
        """
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ClientGetPartitionsCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ClientGetPartitionsCodec.RETRYABLE)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ClientGetPartitionsCodec.RequestParameters()
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ClientGetPartitionsCodec.RESPONSE_TYPE
            self.members=None
            self.index=None

    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ClientGetPartitionsCodec.ResponseParameters()
        members=[]
        members_size=clientMessage.extractIntFromPayload()
        for i in range(members_size):
            member=AddressCodec.decode(clientMessage)
            members.append(member)
        parameters.members=members

        partitions_val_size = clientMessage.extractIntFromPayload()
        partitions_val = []
        for i in range(partitions_val_size):
                partitions_val_item = clientMessage.extractIntFromPayload()
                partitions_val.append(partitions_val_item)
        parameters.index = partitions_val

        return parameters




class ClientAddPartitionLostListenerCodec:
    REQUEST_TYPE = ClientMessageType.CLIENT_ADDPARTITIONLOSTLISTENER
    RESPONSE_TYPE = 104
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ClientAddPartitionLostListenerCodec.REQUEST_TYPE
    @classmethod
    def encodeRequest(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ClientAddPartitionLostListenerCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ClientAddPartitionLostListenerCodec.RETRYABLE)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ClientAddPartitionLostListenerCodec.RequestParameters()
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ClientAddPartitionLostListenerCodec.RESPONSE_TYPE
            self.response=None
    @classmethod
    def encodeResponse(cls, response):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ClientAddPartitionLostListenerCodec.RESPONSE_TYPE)
        clientMessage.set(response)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ClientAddPartitionLostListenerCodec.ResponseParameters()
        response=None
        response = clientMessage.extractStringFromPayload()
        parameters.response = response

        return parameters


    '''************************ EVENTS *************************'''
    #this doesn't need to be used
    @classmethod
    def encodePartitionLostEvent(cls, partitionId, lostBackupCount, source):
        clientMessage=ClientMessage()
        clientMessage.setOperationType(eventconstant.EVENT_PARTITIONLOST)
        clientMessage.setEventFlag()
        clientMessage.set(partitionId)
        clientMessage.set(lostBackupCount)
        source_isNull=None
        if source is None:
            source_isNull = True
            clientMessage.set(source_isNull)
        else:
            source_isNull= False
            clientMessage.set(source_isNull)
        #AddressCodec.encode(source, clientMessage)
        return clientMessage

    class EventHandler:
        def __init__(self,handler):
            self.handler=handler
        def handle(self, clientMessage):
            messageType = clientMessage.getOperationType()
            if (messageType == eventconstant.EVENT_PARTITIONLOST):
                partitionId=None
                partitionId = clientMessage.extractIntFromPayload()
                lostBackupCount=None
                lostBackupCount = clientMessage.extractIntFromPayload()
                source=None
                source_isNull = clientMessage.extractBooleanFromPayload()
                if not source_isNull:
                    source = AddressCodec.decode(clientMessage)
                self.handler.handle(partitionId, lostBackupCount, source)
                return
class ClientPingCodec:
    REQUEST_TYPE = ClientMessageType.CLIENT_PING
    RESPONSE_TYPE = 100
    RETRYABLE = True

    '''************************ REQUEST *************************'''

    class RequestParameters:
        def __init__(self):
            self.TYPE = ClientPingCodec.REQUEST_TYPE
    @classmethod
    def encodeRequest(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ClientPingCodec.REQUEST_TYPE)
        clientMessage.setRetryable(ClientPingCodec.RETRYABLE)
        clientMessage.updateSize()
        return clientMessage

    @classmethod
    def decodeRequest(cls, clientMessage):
        parameters = ClientPingCodec.RequestParameters()
        return parameters

    '''************************ RESPONSE *************************'''

    class ResponseParameters:
        def __init__(self):
            self.TYPE = ClientPingCodec.RESPONSE_TYPE
    @classmethod
    def encodeResponse(cls, ):
        clientMessage = ClientMessage()
        clientMessage.setOperationType(ClientPingCodec.RESPONSE_TYPE)

        return clientMessage
    @classmethod
    def decodeResponse(cls, clientMessage):
        parameters=ClientPingCodec.ResponseParameters()

        return parameters
