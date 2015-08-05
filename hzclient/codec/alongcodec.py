__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage


def incrementandgetEncode(title):
    msg=ClientMessage()
    msg.optype=0x0a0b
    msg.correlation=123
    msg.setPartition(1)
    newtitle=title.encode("UTF8")
    payload=bytearray(ctypes.c_uint32(len(newtitle)))+newtitle
    msg.setPayload(payload)
    return msg

def incrementandgetDecode(servermsg):
    msg=ClientMessage.decodeMessage(servermsg)
    result=msg.extractLongFromPayload()
    return result

def getEncode(title):
    msg=ClientMessage()
    msg.optype=0x0a08
    msg.correlation=124
    msg.partition=1
    newtitle=title.encode("UTF8")
    payload=bytearray(ctypes.c_uint32(len(newtitle)))+newtitle
    msg.setPayload(payload)
    return msg

def getDecode(servermsg):
    msg=ClientMessage.decodeMessage(servermsg)
    result=msg.extractLongFromPayload()
    return result

def addandgetEncode(title,delta):
    msg=ClientMessage()
    msg.optype=0x0a05
    msg.correlation=125
    msg.partition=1
    newtitle=title.encode("UTF8")
    payload=bytearray(ctypes.c_uint32(len(newtitle)))+newtitle+bytearray(ctypes.c_uint32(delta))
    msg.setPayload(payload)
    return msg

def addandgetDecode(servermsg):
    msg=ClientMessage.decodeMessage(servermsg)
    result=msg.extractLongFromPayload()
    return result

def compareandsetEncode(title,expected,updated):
    msg=ClientMessage()
    msg.optype=0x0a06
    msg.correlation=126
    msg.partition=1
    newtitle=title.encode("UTF8")
    payload=bytearray(ctypes.c_uint32(len(newtitle)))+newtitle+bytearray(ctypes.c_uint32(expected))+bytearray(ctypes.c_uint32(updated))
    msg.setPayload(payload)
    return msg

def compareandsetDecode(servermsg):
    msg=ClientMessage.decodeMessage(servermsg)
    result=msg.extractBooleanFromPayload()
    return result


def getandaddEncode(title,delta):
    msg=ClientMessage()
    msg.optype=0x0a09
    msg.correlation=128
    msg.partition=1
    newtitle=title.encode("UTF8")
    payload=bytearray(ctypes.c_uint32(len(newtitle)))+newtitle+bytearray(ctypes.c_uint32(delta))
    msg.setPayload(payload)
    return msg

def getandaddDecode(servermsg):
    msg=ClientMessage.decodeMessage(servermsg)
    result=msg.extractLongFromPayload()
    return result

def getandsetEncode(title,new):
    msg=ClientMessage()
    msg.optype=0x0a0a
    msg.correlation=127
    msg.partition=1
    newtitle=title.encode("UTF8")
    payload=bytearray(ctypes.c_uint32(len(newtitle)))+newtitle+bytearray(ctypes.c_uint32(new))
    msg.setPayload(payload)
    return msg

def getandsetDecode(servermsg):
    msg=ClientMessage.decodeMessage(servermsg)
    result=msg.extractLongFromPayload()
    return result

def getandincrementEncode(title):
    msg=ClientMessage()
    msg.optype=0x0a0c
    msg.correlation=129
    msg.setPartition(1)
    newtitle=title.encode("UTF8")
    payload=bytearray(ctypes.c_uint32(len(newtitle)))+newtitle
    msg.setPayload(payload)
    return msg

def getandincrementDecode(servermsg):
    msg=ClientMessage.decodeMessage(servermsg)
    result=msg.extractLongFromPayload()
    return result

def setEncode(title,new):
    msg=ClientMessage()
    msg.optype=0x0a0d
    msg.correlation=134
    msg.partition=1
    newtitle=title.encode("UTF8")
    payload=bytearray(ctypes.c_uint32(len(newtitle)))+newtitle+bytearray(ctypes.c_uint32(new))
    msg.setPayload(payload)
    return msg

def setDecode(servermsg):
    #nothing returned for a setDecode
    return None