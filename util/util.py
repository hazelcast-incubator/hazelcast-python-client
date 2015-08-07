__author__ = 'Jonathan Brodie'

import ctypes,struct
import encode

def raiseNotDefined():
    raise NotImplementedError("This method has not been defined.")

def hzstringbytes(str):
    length=len(str)
    constant=bytearray([0xff,0xff,0xff,0xf5])
    first=struct.pack("!h",length)
    second=struct.pack("!i",length)

    final=constant+bytearray([0x00,0x00])+second+second+first+str.encode("UTF8")
    return encode.encodeuint32(len(final))+final

def decodehzstring(byteobject):

    #we should really use a decoder here but screw it
    byteobject=byteobject[14:]
    size=struct.unpack("!i",byteobject[:4])
    byteobject=byteobject[4:]
    size2=struct.unpack("!h",byteobject[:2])
    byteobject=byteobject[2:]

    mystr=byteobject.decode("UTF8")
    return mystr