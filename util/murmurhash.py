__author__ = 'Jonathan Brodie'

import struct,sys
#murmur hash function to determine partition
def bytes_to_long(bytes):
    assert len(bytes) == 8
    return sum((b << (k * 8) for k, b in enumerate(bytes)))

def murmur(key, seed=19820125):
    m=0xc6a4a7935bd1e995
    r=47
    MASK=2**64 -1
    #convert the key to bytes
    key=bytearray(key)
    hash=seed ^ ((m * len(key)) & MASK)



    offset=len(key)/8*8
    for i in range(0,offset,8):
        currentbyte=key[i:i+8]
        num=bytes_to_long(currentbyte)
        num=(num*m) & MASK
        num=num^ ((num>> r) & MASK)
        num=(num*m)&MASK
        hash=(hash^num)
        hash=(hash^m) & MASK

    remainder=len(key) & 7
    if remainder > 0:

        hash=hash ^ (key[offset+remainder-1] << ((remainder-1)*8))

    hash=hash ^ ((hash >> r) & MASK)
    hash=(hash * m) & MASK
    hash=hash ^ ((hash >> r) & MASK)

    return hash