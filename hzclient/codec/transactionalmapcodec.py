__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util
'''
CONTAINSKEY
'''
def containskeyEncode():
    msg=ClientMessage()
    msg.optype=0x1001
    util.raiseNotDefined()
def containskeyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GET
'''
def getEncode():
    msg=ClientMessage()
    msg.optype=0x1002
    util.raiseNotDefined()
def getDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GETFORUPDATE
'''
def getforupdateEncode():
    msg=ClientMessage()
    msg.optype=0x1003
    util.raiseNotDefined()
def getforupdateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
SIZE
'''
def sizeEncode():
    msg=ClientMessage()
    msg.optype=0x1004
    util.raiseNotDefined()
def sizeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ISEMPTY
'''
def isemptyEncode():
    msg=ClientMessage()
    msg.optype=0x1005
    util.raiseNotDefined()
def isemptyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
PUT
'''
def putEncode():
    msg=ClientMessage()
    msg.optype=0x1006
    util.raiseNotDefined()
def putDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
SET
'''
def setEncode():
    msg=ClientMessage()
    msg.optype=0x1007
    util.raiseNotDefined()
def setDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
PUTIFABSENT
'''
def putifabsentEncode():
    msg=ClientMessage()
    msg.optype=0x1008
    util.raiseNotDefined()
def putifabsentDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REPLACE
'''
def replaceEncode():
    msg=ClientMessage()
    msg.optype=0x1009
    util.raiseNotDefined()
def replaceDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REPLACEIFSAME
'''
def replaceifsameEncode():
    msg=ClientMessage()
    msg.optype=0x100a
    util.raiseNotDefined()
def replaceifsameDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVE
'''
def removeEncode():
    msg=ClientMessage()
    msg.optype=0x100b
    util.raiseNotDefined()
def removeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
DELETE
'''
def deleteEncode():
    msg=ClientMessage()
    msg.optype=0x100c
    util.raiseNotDefined()
def deleteDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEIFSAME
'''
def removeifsameEncode():
    msg=ClientMessage()
    msg.optype=0x100d
    util.raiseNotDefined()
def removeifsameDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
KEYSET
'''
def keysetEncode():
    msg=ClientMessage()
    msg.optype=0x100e
    util.raiseNotDefined()
def keysetDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
KEYSETWITHPREDICATE
'''
def keysetwithpredicateEncode():
    msg=ClientMessage()
    msg.optype=0x100f
    util.raiseNotDefined()
def keysetwithpredicateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
VALUES
'''
def valuesEncode():
    msg=ClientMessage()
    msg.optype=0x1010
    util.raiseNotDefined()
def valuesDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
VALUESWITHPREDICATE
'''
def valueswithpredicateEncode():
    msg=ClientMessage()
    msg.optype=0x1011
    util.raiseNotDefined()
def valueswithpredicateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

