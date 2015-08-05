__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util

'''
PUT
'''
def putEncode():
    msg=ClientMessage()
    msg.optype=0x0201
    util.raiseNotDefined()
def putDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GET
'''
def getEncode():
    msg=ClientMessage()
    msg.optype=0x0202
    util.raiseNotDefined()
def getDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVE
'''
def removeEncode():
    msg=ClientMessage()
    msg.optype=0x0203
    util.raiseNotDefined()
def removeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
KEYSET
'''
def keysetEncode():
    msg=ClientMessage()
    msg.optype=0x0204
    util.raiseNotDefined()
def keysetDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
VALUES
'''
def valuesEncode():
    msg=ClientMessage()
    msg.optype=0x0205
    util.raiseNotDefined()
def valuesDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ENTRYSET
'''
def entrysetEncode():
    msg=ClientMessage()
    msg.optype=0x0206
    util.raiseNotDefined()
def entrysetDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CONTAINSKEY
'''
def containskeyEncode():
    msg=ClientMessage()
    msg.optype=0x0207
    util.raiseNotDefined()
def containskeyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CONTAINSVALUE
'''
def containsvalueEncode():
    msg=ClientMessage()
    msg.optype=0x0208
    util.raiseNotDefined()
def containsvalueDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CONTAINSENTRY
'''
def containsentryEncode():
    msg=ClientMessage()
    msg.optype=0x0209
    util.raiseNotDefined()
def containsentryDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
SIZE
'''
def sizeEncode():
    msg=ClientMessage()
    msg.optype=0x020a
    util.raiseNotDefined()
def sizeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CLEAR
'''
def clearEncode():
    msg=ClientMessage()
    msg.optype=0x020b
    util.raiseNotDefined()
def clearDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
COUNT
'''
def countEncode():
    msg=ClientMessage()
    msg.optype=0x020c
    util.raiseNotDefined()
def countDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDENTRYLISTENERTOKEY
'''
def addentrylistenertokeyEncode():
    msg=ClientMessage()
    msg.optype=0x020d
    util.raiseNotDefined()
def addentrylistenertokeyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDENTRYLISTENER
'''
def addentrylistenerEncode():
    msg=ClientMessage()
    msg.optype=0x020e
    util.raiseNotDefined()
def addentrylistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEENTRYLISTENER
'''
def removeentrylistenerEncode():
    msg=ClientMessage()
    msg.optype=0x020f
    util.raiseNotDefined()
def removeentrylistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
LOCK
'''
def lockEncode():
    msg=ClientMessage()
    msg.optype=0x0210
    util.raiseNotDefined()
def lockDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
TRYLOCK
'''
def trylockEncode():
    msg=ClientMessage()
    msg.optype=0x0211
    util.raiseNotDefined()
def trylockDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ISLOCKED
'''
def islockedEncode():
    msg=ClientMessage()
    msg.optype=0x0212
    util.raiseNotDefined()
def islockedDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
UNLOCK
'''
def unlockEncode():
    msg=ClientMessage()
    msg.optype=0x0213
    util.raiseNotDefined()
def unlockDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
FORCEUNLOCK
'''
def forceunlockEncode():
    msg=ClientMessage()
    msg.optype=0x0214
    util.raiseNotDefined()
def forceunlockDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEENTRY
'''
def removeentryEncode():
    msg=ClientMessage()
    msg.optype=0x0215
    util.raiseNotDefined()
def removeentryDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
VALUECOUNT
'''
def valuecountEncode():
    msg=ClientMessage()
    msg.optype=0x0216
    util.raiseNotDefined()
def valuecountDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

