__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util
'''
SHUTDOWN
'''
def shutdownEncode():
    msg=ClientMessage()
    msg.optype=0x0901
    util.raiseNotDefined()
def shutdownDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ISSHUTDOWN
'''
def isshutdownEncode():
    msg=ClientMessage()
    msg.optype=0x0902
    util.raiseNotDefined()
def isshutdownDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CANCELONPARTITION
'''
def cancelonpartitionEncode():
    msg=ClientMessage()
    msg.optype=0x0903
    util.raiseNotDefined()
def cancelonpartitionDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CANCELONADDRESS
'''
def cancelonaddressEncode():
    msg=ClientMessage()
    msg.optype=0x0904
    util.raiseNotDefined()
def cancelonaddressDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
SUBMITTOPARTITION
'''
def submittopartitionEncode():
    msg=ClientMessage()
    msg.optype=0x0905
    util.raiseNotDefined()
def submittopartitionDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
SUBMITTOADDRESS
'''
def submittoaddressEncode():
    msg=ClientMessage()
    msg.optype=0x0906
    util.raiseNotDefined()
def submittoaddressDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

