__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage
from util import util

'''
APPLY
'''
def applyEncode(name,function):
    msg=ClientMessage()
    msg.optype=0x0b01
    newname=name.encode("UTF8")
    msg.setPayload(bytearray(ctypes.c_uint32(len(newname)))+newname+bytearray(ctypes.c_uint32(len(function)))+function)
    return msg
def applyDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    response=servermsg.extractBytesFromPayload()
    return response

'''
ALTER
'''
def alterEncode(name,function):
    msg=ClientMessage()
    msg.optype=0x0b02
    newname=name.encode("UTF8")
    msg.setPayload(bytearray(ctypes.c_uint32(len(newname)))+newname+bytearray(ctypes.c_uint32(len(function)))+function)
    return msg
def alterDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    response=servermsg.extractLongFromPayload()
    return response

'''
ALTERANDGET
'''
def alterandgetEncode(name,function):
    msg=ClientMessage()
    msg.optype=0x0b03
    newname=name.encode("UTF8")
    msg.setPayload(bytearray(ctypes.c_uint32(len(newname)))+newname+bytearray(ctypes.c_uint32(len(function)))+function)
    return msg
def alterandgetDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    response=servermsg.extractLongFromPayload()
    return response

'''
GETANDALTER
'''
def getandalterEncode(name,function):
    msg=ClientMessage()
    msg.optype=0x0b04
    newname=name.encode("UTF8")
    msg.setPayload(bytearray(ctypes.c_uint32(len(newname)))+newname+bytearray(ctypes.c_uint32(len(function)))+function)
    return msg
def getandalterDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    return servermsg.extractBytesFromPayload()

'''
CONTAINS
'''
def containsEncode(name,expected):
    msg=ClientMessage()
    msg.optype=0x0b05
    newname=name.encode("UTF8")
    msg.setPayload(bytearray(ctypes.c_uint32(len(newname)))+newname+bytearray(ctypes.c_uint32(len(expected)))+expected)
    return msg
def containsDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    return servermsg.extractBooleanFromPayload()


'''
COMPAREANDSET
'''
def compareandsetEncode(name,expected,updated):
    msg=ClientMessage()
    msg.optype=0x0b06
    newname=name.encode("UTF8")
    msg.setPayload(bytearray(ctypes.c_uint32(len(newname)))+newname+bytearray(ctypes.c_uint32(len(expected)))+expected+ctypes.c_uint32(len(updated))+updated)
    return msg
def compareandsetDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    return servermsg.extractBooleanFromPayload()

'''
GET
'''
def getEncode(name):
    msg=ClientMessage()
    msg.optype=0x0b08
    newname=name.encode("UTF8")
    msg.setPayload(bytearray(ctypes.c_uint32(len(newname)))+newname)
    return msg
def getDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    return servermsg.extractBytesFromPayload()

'''
SET
'''
def setEncode(name,newValue):
    msg=ClientMessage()
    msg.optype=0x0b09
    newname=name.encode("UTF8")
    msg.setPayload(bytearray(ctypes.c_uint32(len(newname)))+newname+bytearray(ctypes.c_uint32(len(newValue)))+newValue)
    return msg
def setDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    return None

'''
CLEAR
'''
def clearEncode(name):
    msg=ClientMessage()
    msg.optype=0x0b0a
    newname=name.encode("UTF8")
    msg.setPayload(bytearray(ctypes.c_uint32(len(newname)))+newname)
    return msg
def clearDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    return None

'''
GETANDSET
'''
def getandsetEncode(name,newValue):
    msg=ClientMessage()
    msg.optype=0x0b0b
    newname=name.encode("UTF8")
    msg.setPayload(bytearray(ctypes.c_uint32(len(newname)))+newname+bytearray(ctypes.c_uint32(len(newValue)))+newValue)
    return msg
def getandsetDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    return servermsg.extractBytesFromPayload()

'''
SETANDGET
'''
def setandgetEncode(name,newValue):
    msg=ClientMessage()
    msg.optype=0x0b0c
    newname=name.encode("UTF8")
    msg.setPayload(bytearray(ctypes.c_uint32(len(newname)))+newname+bytearray(ctypes.c_uint32(len(newValue)))+newValue)
    return msg
def setandgetDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    return servermsg.extractBytesFromPayload()

'''
ISNULL
'''
def isnullEncode(name):
    msg=ClientMessage()
    msg.optype=0x0b0d
    newname=name.encode("UTF8")
    msg.setPayload(bytearray(ctypes.c_uint32(len(newname)))+newname)
    return msg
def isnullDecode(bytesobject):
    servermsg=ClientMessage.decodeMessage(bytesobject)
    return servermsg.extractBytesFromPayload()

