__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util
'''
PUT
'''
def putEncode():
    msg=ClientMessage()
    msg.optype=0x1101
    util.raiseNotDefined()
def putDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GET
'''
def getEncode():
    msg=ClientMessage()
    msg.optype=0x1102
    util.raiseNotDefined()
def getDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVE
'''
def removeEncode():
    msg=ClientMessage()
    msg.optype=0x1103
    util.raiseNotDefined()
def removeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEENTRY
'''
def removeentryEncode():
    msg=ClientMessage()
    msg.optype=0x1104
    util.raiseNotDefined()
def removeentryDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
VALUECOUNT
'''
def valuecountEncode():
    msg=ClientMessage()
    msg.optype=0x1105
    util.raiseNotDefined()
def valuecountDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
SIZE
'''
def sizeEncode():
    msg=ClientMessage()
    msg.optype=0x1106
    util.raiseNotDefined()
def sizeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()