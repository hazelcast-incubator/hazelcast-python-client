__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util
'''
COMMIT
'''
def commitEncode():
    msg=ClientMessage()
    msg.optype=0x1701
    util.raiseNotDefined()
def commitDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CREATE
'''
def createEncode():
    msg=ClientMessage()
    msg.optype=0x1702
    util.raiseNotDefined()
def createDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ROLLBACK
'''
def rollbackEncode():
    msg=ClientMessage()
    msg.optype=0x1703
    util.raiseNotDefined()
def rollbackDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

