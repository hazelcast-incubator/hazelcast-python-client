__author__ = 'jonathanbrodie'
import struct

'''
To-do: properly decode bytes
'''


def decodeboolean(bytesobject):
    if bool is False:
        return bytearray(ctypes.c_uint8(0))
    else:
        return bytearray(ctypes.c_uint8(bool))
def decodeuint8(target):
    return bytearray(ctypes.c_uint8(target))
def decodeuint16(target):
    return bytearray(ctypes.c_uint16(target))
def decodeuint32(target):
    return bytearray(ctypes.c_uint32(target))
def decodeuint64(target):
    return bytearray(ctypes.c_uint64(target))
def decodeint8(target):
    return bytearray(ctypes.c_int8(target))
def decodeint16(target):
    return bytearray(ctypes.c_int16(target))
def decodeint32(target):
    return bytearray(ctypes.c_int32(target))
def decodeint64(target):
    return bytearray(ctypes.c_int64(target))
def decodefloat(target):
    return bytearray(ctypes.c_float(target))
def decodedouble(target):
    return bytearray(ctypes.c_double(target))
def decodestring(string):
    newstring=string.decode("UTF8")
    return decodeuint32(len(newstring))+newstring
def decodebytes(bytes):
    return decodeuint32(len(bytes))+bytes