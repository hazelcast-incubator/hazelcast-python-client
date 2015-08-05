__author__ = 'Jonathan Brodie'

import struct,sys
#murmur hash function to determine partition
#it's important that key is encoded before use
def murmur(key, length, seed):
    c1=0xcc9e2d51
    c2=0x1b873593
    r1=15
    r2=13
    m=5
    n=0xe6546b64

    hash=seed
    delimiter=4
    splitBytes=[key[i:i+delimiter] for i in range(0,len(key),delimiter)]

    for item in splitBytes:
        if not (len(item) == 4):
            break
        k=item
        k=(k << r1) | (k >> (32-r1))
        k=k*c2
        hash=hash ^ k
        hash=(hash << r2) | (hash >> 32-r2)
        hash=hash * m + n
    lastIndex=len(splitBytes)-1

    if len(splitBytes[lastIndex]) != 4:

        remainingBytes=splitBytes[lastIndex]
        endianness=None
        if sys.byteorder is 'big':
            endianness=">"
        else:
            endianness="<"
        remainingBytes=struct.unpack(endianness+"%dC" % len(remainingBytes),remainingBytes)
        remainingBytes=remainingBytes*c1
        remainingBytes=(remainingBytes << r1) | (remainingBytes >> (32 - r1))
        remainingBytes=remainingBytes * c2
        hash=hash ^ remainingBytes

    hash=hash ^ length

    hash=hash ^ (hash >> 16)
    hash=hash*0x85ebca6b
    hash=hash ^ (hash >> 13)
    hash=hash*0xc2b2ae35
    hash=hash ^ (hash >> 16)

    return hash