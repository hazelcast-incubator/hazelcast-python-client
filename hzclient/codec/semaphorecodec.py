__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util

'''
INIT
'''
def initEncode():
    msg=ClientMessage()
    msg.optype=0x0d01
    util.raiseNotDefined()
def initDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ACQUIRE
'''
def acquireEncode():
    msg=ClientMessage()
    msg.optype=0x0d02
    util.raiseNotDefined()
def acquireDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
AVAILABLEPERMITS
'''
def availablepermitsEncode():
    msg=ClientMessage()
    msg.optype=0x0d03
    util.raiseNotDefined()
def availablepermitsDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
DRAINPERMITS
'''
def drainpermitsEncode():
    msg=ClientMessage()
    msg.optype=0x0d04
    util.raiseNotDefined()
def drainpermitsDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REDUCEPERMITS
'''
def reducepermitsEncode():
    msg=ClientMessage()
    msg.optype=0x0d05
    util.raiseNotDefined()
def reducepermitsDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
RELEASE
'''
def releaseEncode():
    msg=ClientMessage()
    msg.optype=0x0d06
    util.raiseNotDefined()
def releaseDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
TRYACQUIRE
'''
def tryacquireEncode():
    msg=ClientMessage()
    msg.optype=0x0d07
    util.raiseNotDefined()
def tryacquireDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

