__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util

'''
PUT
'''
def putEncode():
    msg=ClientMessage()
    msg.optype=0x0e01
    util.raiseNotDefined()
def putDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
SIZE
'''
def sizeEncode():
    msg=ClientMessage()
    msg.optype=0x0e02
    util.raiseNotDefined()
def sizeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ISEMPTY
'''
def isemptyEncode():
    msg=ClientMessage()
    msg.optype=0x0e03
    util.raiseNotDefined()
def isemptyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CONTAINSKEY
'''
def containskeyEncode():
    msg=ClientMessage()
    msg.optype=0x0e04
    util.raiseNotDefined()
def containskeyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CONTAINSVALUE
'''
def containsvalueEncode():
    msg=ClientMessage()
    msg.optype=0x0e05
    util.raiseNotDefined()
def containsvalueDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GET
'''
def getEncode():
    msg=ClientMessage()
    msg.optype=0x0e06
    util.raiseNotDefined()
def getDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVE
'''
def removeEncode():
    msg=ClientMessage()
    msg.optype=0x0e07
    util.raiseNotDefined()
def removeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
PUTALL
'''
def putallEncode():
    msg=ClientMessage()
    msg.optype=0x0e08
    util.raiseNotDefined()
def putallDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CLEAR
'''
def clearEncode():
    msg=ClientMessage()
    msg.optype=0x0e09
    util.raiseNotDefined()
def clearDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDENTRYLISTENERTOKEYWITHPREDICATE
'''
def addentrylistenertokeywithpredicateEncode():
    msg=ClientMessage()
    msg.optype=0x0e0a
    util.raiseNotDefined()
def addentrylistenertokeywithpredicateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDENTRYLISTENERWITHPREDICATE
'''
def addentrylistenerwithpredicateEncode():
    msg=ClientMessage()
    msg.optype=0x0e0b
    util.raiseNotDefined()
def addentrylistenerwithpredicateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDENTRYLISTENERTOKEY
'''
def addentrylistenertokeyEncode():
    msg=ClientMessage()
    msg.optype=0x0e0c
    util.raiseNotDefined()
def addentrylistenertokeyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDENTRYLISTENER
'''
def addentrylistenerEncode():
    msg=ClientMessage()
    msg.optype=0x0e0d
    util.raiseNotDefined()
def addentrylistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEENTRYLISTENER
'''
def removeentrylistenerEncode():
    msg=ClientMessage()
    msg.optype=0x0e0e
    util.raiseNotDefined()
def removeentrylistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
KEYSET
'''
def keysetEncode():
    msg=ClientMessage()
    msg.optype=0x0e0f
    util.raiseNotDefined()
def keysetDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
VALUES
'''
def valuesEncode():
    msg=ClientMessage()
    msg.optype=0x0e10
    util.raiseNotDefined()
def valuesDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ENTRYSET
'''
def entrysetEncode():
    msg=ClientMessage()
    msg.optype=0x0e11
    util.raiseNotDefined()
def entrysetDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

