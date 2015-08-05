__author__ = 'Jonathan Brodie'
import ctypes
from hzclient.clientmessage import ClientMessage

def createProxy(name,service):
    msg=ClientMessage()
    msg.optype=0x5
    newtitle=name.encode("UTF8")

    newbody=service.encode("UTF8")

    payload=bytearray(ctypes.c_uint32(len(newtitle)))+newtitle+bytearray(ctypes.c_uint32(len(newbody)))+newbody
    msg.setPayload(payload)
    return msg
def destroyProxy(name,service):
    msg=ClientMessage()
    msg.optype=0x6
    newtitle=name.encode("UTF8")

    newbody=service.encode("UTF8")
    payload=bytearray(ctypes.c_uint32(len(newtitle)))+newtitle+bytearray(ctypes.c_uint32(len(newbody)))+newbody
    msg.setPayload(payload)
    return msg

