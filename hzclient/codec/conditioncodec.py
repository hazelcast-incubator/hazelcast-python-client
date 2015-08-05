__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util
'''
AWAIT
'''
def awaitEncode():
    msg=ClientMessage()
    msg.optype=0x0801
    util.raiseNotDefined()
def awaitDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
BEFOREAWAIT
'''
def beforeawaitEncode():
    msg=ClientMessage()
    msg.optype=0x0802
    util.raiseNotDefined()
def beforeawaitDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
SIGNAL
'''
def signalEncode():
    msg=ClientMessage()
    msg.optype=0x0803
    util.raiseNotDefined()
def signalDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
SIGNALALL
'''
def signalallEncode():
    msg=ClientMessage()
    msg.optype=0x0804
    util.raiseNotDefined()
def signalallDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

