__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util

'''
ISLOCKED
'''
def islockedEncode():
    msg=ClientMessage()
    msg.optype=0x0701
    util.raiseNotDefined()
def islockedDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ISLOCKEDBYCURRENTTHREAD
'''
def islockedbycurrentthreadEncode():
    msg=ClientMessage()
    msg.optype=0x0702
    util.raiseNotDefined()
def islockedbycurrentthreadDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GETLOCKCOUNT
'''
def getlockcountEncode():
    msg=ClientMessage()
    msg.optype=0x0703
    util.raiseNotDefined()
def getlockcountDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GETREMAININGLEASETIME
'''
def getremainingleasetimeEncode():
    msg=ClientMessage()
    msg.optype=0x0704
    util.raiseNotDefined()
def getremainingleasetimeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
LOCK
'''
def lockEncode():
    msg=ClientMessage()
    msg.optype=0x0705
    util.raiseNotDefined()
def lockDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
UNLOCK
'''
def unlockEncode():
    msg=ClientMessage()
    msg.optype=0x0706
    util.raiseNotDefined()
def unlockDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
FORCEUNLOCK
'''
def forceunlockEncode():
    msg=ClientMessage()
    msg.optype=0x0707
    util.raiseNotDefined()
def forceunlockDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
TRYLOCK
'''
def trylockEncode():
    msg=ClientMessage()
    msg.optype=0x0708
    util.raiseNotDefined()
def trylockDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()