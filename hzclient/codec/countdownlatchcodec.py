__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util

'''
AWAIT
'''
def awaitEncode():
    msg=ClientMessage()
    msg.optype=0x0c01
    util.raiseNotDefined()
def awaitDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
COUNTDOWN
'''
def countdownEncode():
    msg=ClientMessage()
    msg.optype=0x0c02
    util.raiseNotDefined()
def countdownDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GETCOUNT
'''
def getcountEncode():
    msg=ClientMessage()
    msg.optype=0x0c03
    util.raiseNotDefined()
def getcountDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
TRYSETCOUNT
'''
def trysetcountEncode():
    msg=ClientMessage()
    msg.optype=0x0c04
    util.raiseNotDefined()
def trysetcountDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

