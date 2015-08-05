__author__ = 'Jonathan Brodie'
from hzclient.clientmessage import ClientMessage
from hzclient.clientmessage import AuthenticationMessage


import unittest,ctypes
class ClientMessageTests(unittest.TestCase):

    def testHeaderNormal(self):
        msg=ClientMessage()
        self.assertEqual(len(msg.encodeMessage()),msg.FRAME_SIZE)

    def testDecoding(self):
        msg=ClientMessage()
        vr=0
        optype=20
        corrID=0
        parID=-1

        msg.setVersion(0)
        msg.setFlagBoth()
        msg.setOperationType(20)
        msg.correlation=corrID
        msg.setPartition(parID)

        frame = bytearray()

        #Create a byte array of size 18
        frame+=bytearray(ctypes.c_int32(18))
        frame+=bytearray(ctypes.c_uint8(vr))
        frame+=bytearray(ctypes.c_uint8(192))
        frame+=bytearray(ctypes.c_uint16(optype))
        frame+=bytearray(ctypes.c_int32(corrID))
        frame+=bytearray(ctypes.c_int32(parID))
        frame+=bytearray(ctypes.c_uint16(18))

        msg2=ClientMessage.decodeMessage(frame)
        self.assertEqual(msg.encodeMessage(),msg2.encodeMessage())

    def testEncoding(self):
        msg=ClientMessage()
        vr=0
        optype=200
        corrID=0
        parID=-1

        msg.setVersion(vr)
        msg.setFlagBoth()
        msg.setOperationType(200)
        msg.correlation=corrID
        msg.setPartition(parID)

        frame = bytearray()

        #Create a byte array of size 18
        frame+=bytearray(ctypes.c_int32(18))
        frame+=bytearray(ctypes.c_uint8(vr))
        frame+=bytearray(ctypes.c_uint8(192))
        frame+=bytearray(ctypes.c_uint16(optype))
        frame+=bytearray(ctypes.c_int32(corrID))
        frame+=bytearray(ctypes.c_int32(parID))
        frame+=bytearray(ctypes.c_uint16(18))

        self.assertEqual(frame,msg.encodeMessage())

    def testEncodingWithPayload(self):
        msg=ClientMessage()
        vr=0
        optype=200
        corrID=0
        parID=-1

        msg.version=vr
        msg.optype=optype
        msg.correlation=corrID
        msg.partition=parID
        msg.setPayload(bytearray(ctypes.c_uint32(4203239)))
        frame = bytearray()
        #Create a byte array of size 18


        frame+=bytearray(ctypes.c_int32(18+4))
        frame+=bytearray(ctypes.c_uint8(vr))
        frame+=bytearray(ctypes.c_uint8(192))
        frame+=bytearray(ctypes.c_uint16(optype))
        frame+=bytearray(ctypes.c_int32(corrID))
        frame+=bytearray(ctypes.c_int32(parID))
        frame+=bytearray(ctypes.c_uint16(18+4))
        frame+=bytearray(ctypes.c_uint32(4203239))

        encodedMsg=msg.encodeMessage()


        self.assertEqual(frame,encodedMsg)

    def testEncodingWithExtension(self):
        msg=ClientMessage()
        vr=0
        optype=200
        corrID=0
        parID=-1

        msg.version=vr
        msg.optype=optype
        msg.correlation=corrID
        msg.partition=parID
        msg.addExtension(bytearray(ctypes.c_uint32(4203239)))
        frame = bytearray()
        #Create a byte array of size 18


        frame+=bytearray(ctypes.c_int32(18+4))
        frame+=bytearray(ctypes.c_uint8(vr))
        frame+=bytearray(ctypes.c_uint8(192))
        frame+=bytearray(ctypes.c_uint16(optype))
        frame+=bytearray(ctypes.c_int32(corrID))
        frame+=bytearray(ctypes.c_int32(parID))
        frame+=bytearray(ctypes.c_uint16(22))
        frame+=bytearray(ctypes.c_uint32(4203239))

        encodedMsg=msg.encodeMessage()


        self.assertEqual(frame,encodedMsg)

    def testEncodingWithExtensionAndPayload(self):
        msg=ClientMessage()
        vr=0
        optype=200
        corrID=0
        parID=-1

        msg.version=vr
        msg.optype=optype
        msg.correlation=corrID
        msg.partition=parID
        msg.addExtension(bytearray(ctypes.c_uint32(4203239)))
        msg.setPayload(bytearray(ctypes.c_uint32(4203239)))

        frame = bytearray()
        #Create a byte array of size 18


        frame+=bytearray(ctypes.c_int32(18+4+4))
        frame+=bytearray(ctypes.c_uint8(vr))
        frame+=bytearray(ctypes.c_uint8(192))
        frame+=bytearray(ctypes.c_uint16(optype))
        frame+=bytearray(ctypes.c_int32(corrID))
        frame+=bytearray(ctypes.c_int32(parID))
        frame+=bytearray(ctypes.c_uint16(26))
        frame+=bytearray(ctypes.c_uint32(4203239))
        frame+=bytearray(ctypes.c_uint32(4203239))


        encodedMsg=msg.encodeMessage()


        self.assertEqual(frame,encodedMsg)

    def testAuthentication(self):
        msg=AuthenticationMessage()
        newmsg=msg.encodeMessage()

        msg2=AuthenticationMessage.decodeMessage(newmsg)
        self.assertEqual(msg.FRAME_SIZE,msg2.FRAME_SIZE)


if __name__ == '__main__':
    unittest.main()

