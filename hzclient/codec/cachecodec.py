__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util

'''
ADDENTRYLISTENER
'''
def addentrylistenerEncode():
    msg=ClientMessage()
    msg.optype=0x1501
    util.raiseNotDefined()
def addentrylistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ADDINVALIDATIONLISTENER
'''
def addinvalidationlistenerEncode():
    msg=ClientMessage()
    msg.optype=0x1502
    util.raiseNotDefined()
def addinvalidationlistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CLEAR
'''
def clearEncode():
    msg=ClientMessage()
    msg.optype=0x1503
    util.raiseNotDefined()
def clearDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEALLKEYS
'''
def removeallkeysEncode():
    msg=ClientMessage()
    msg.optype=0x1504
    util.raiseNotDefined()
def removeallkeysDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEALL
'''
def removeallEncode():
    msg=ClientMessage()
    msg.optype=0x1505
    util.raiseNotDefined()
def removeallDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CONTAINSKEY
'''
def containskeyEncode():
    msg=ClientMessage()
    msg.optype=0x1506
    util.raiseNotDefined()
def containskeyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
CREATECONFIG
'''
def createconfigEncode():
    msg=ClientMessage()
    msg.optype=0x1507
    util.raiseNotDefined()
def createconfigDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
DESTROY
'''
def destroyEncode():
    msg=ClientMessage()
    msg.optype=0x1508
    util.raiseNotDefined()
def destroyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ENTRYPROCESSOR
'''
def entryprocessorEncode():
    msg=ClientMessage()
    msg.optype=0x1509
    util.raiseNotDefined()
def entryprocessorDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GETALL
'''
def getallEncode():
    msg=ClientMessage()
    msg.optype=0x150a
    util.raiseNotDefined()
def getallDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GETANDREMOVE
'''
def getandremoveEncode():
    msg=ClientMessage()
    msg.optype=0x150b
    util.raiseNotDefined()
def getandremoveDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GETANDREPLACE
'''
def getandreplaceEncode():
    msg=ClientMessage()
    msg.optype=0x150c
    util.raiseNotDefined()
def getandreplaceDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GETCONFIG
'''
def getconfigEncode():
    msg=ClientMessage()
    msg.optype=0x150d
    util.raiseNotDefined()
def getconfigDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
GET
'''
def getEncode():
    msg=ClientMessage()
    msg.optype=0x150e
    util.raiseNotDefined()
def getDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
ITERATE
'''
def iterateEncode():
    msg=ClientMessage()
    msg.optype=0x150f
    util.raiseNotDefined()
def iterateDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
LISTENERREGISTRATION
'''
def listenerregistrationEncode():
    msg=ClientMessage()
    msg.optype=0x1510
    util.raiseNotDefined()
def listenerregistrationDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
LOADALL
'''
def loadallEncode():
    msg=ClientMessage()
    msg.optype=0x1511
    util.raiseNotDefined()
def loadallDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
MANAGEMENTCONFIG
'''
def managementconfigEncode():
    msg=ClientMessage()
    msg.optype=0x1512
    util.raiseNotDefined()
def managementconfigDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
PUTIFABSENT
'''
def putifabsentEncode():
    msg=ClientMessage()
    msg.optype=0x1513
    util.raiseNotDefined()
def putifabsentDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
PUT
'''
def putEncode():
    msg=ClientMessage()
    msg.optype=0x1514
    util.raiseNotDefined()
def putDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEENTRYLISTENER
'''
def removeentrylistenerEncode():
    msg=ClientMessage()
    msg.optype=0x1515
    util.raiseNotDefined()
def removeentrylistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVEINVALIDATIONLISTENER
'''
def removeinvalidationlistenerEncode():
    msg=ClientMessage()
    msg.optype=0x1516
    util.raiseNotDefined()
def removeinvalidationlistenerDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REMOVE
'''
def removeEncode():
    msg=ClientMessage()
    msg.optype=0x1517
    util.raiseNotDefined()
def removeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
REPLACE
'''
def replaceEncode():
    msg=ClientMessage()
    msg.optype=0x1518
    util.raiseNotDefined()
def replaceDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

'''
SIZE
'''
def sizeEncode():
    msg=ClientMessage()
    msg.optype=0x1519
    util.raiseNotDefined()
def sizeDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    util.raiseNotDefined()

