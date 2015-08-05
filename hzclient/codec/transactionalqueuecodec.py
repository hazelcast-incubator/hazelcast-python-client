__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util
'''
OFFER
'''
def offerEncode():
    msg=ClientMessage()
    msg.optype=0x1401
    util.raiseNotDefined()
def offerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
TAKE
'''
def takeEncode():
    msg=ClientMessage()
    msg.optype=0x1402
    util.raiseNotDefined()
def takeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
POLL
'''
def pollEncode():
    msg=ClientMessage()
    msg.optype=0x1403
    util.raiseNotDefined()
def pollDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
PEEK
'''
def peekEncode():
    msg=ClientMessage()
    msg.optype=0x1404
    util.raiseNotDefined()
def peekDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
SIZE
'''
def sizeEncode():
    msg=ClientMessage()
    msg.optype=0x1405
    util.raiseNotDefined()
def sizeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

