__author__ = 'jonathanbrodie'
import ctypes
'''
Helper module to be used with codecs to make sure Python stuff gets explicitly converted to certain data types
'''



def encodeboolean(bool):
    if bool is False:
        return bytearray(ctypes.c_uint8(0))
    else:
        return bytearray(ctypes.c_uint8(bool))
def encodeuint8(target):
    return bytearray(ctypes.c_uint8(target))
def encodeuint16(target):
    return bytearray(ctypes.c_uint16(target))
def encodeuint32(target):
    return bytearray(ctypes.c_uint32(target))
def encodeuint64(target):
    return bytearray(ctypes.c_uint64(target))
def encodeint8(target):
    return bytearray(ctypes.c_int8(target))
def encodeint16(target):
    return bytearray(ctypes.c_int16(target))
def encodeint32(target):
    return bytearray(ctypes.c_int32(target))
def encodeint64(target):
    return bytearray(ctypes.c_int64(target))
def encodefloat(target):
    return bytearray(ctypes.c_float(target))
def encodedouble(target):
    return bytearray(ctypes.c_double(target))
def encodestring(string):
    newstring=string.encode("UTF8")
    return encodeuint32(len(newstring))+newstring
def encodebytes(bytes):
    return encodeuint32(len(bytes))+bytes

