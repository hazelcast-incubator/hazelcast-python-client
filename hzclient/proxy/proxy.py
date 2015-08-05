__author__ = 'Jonathan Brodie'

from hzclient.codec import alongcodec
from hzclient.codec import proxycodec



class ALongProxy(object):
    def __init__(self,title,conn):
        self.title=title
        self.connection=conn
        firstpack=proxycodec.createProxy(self.title,"hz:impl:atomicLongService")
        self.connection.adjustCorrelationId(firstpack)
        self.connection.sendPackage(firstpack.encodeMessage())

        response=self.connection.getPackageWithCorrelationId(firstpack.correlation,True)
        if response is not None:
            print "Initialized and connected proxy!"
        else:
            print "Unable to connect to server."

    def getAndIncrement(self):
        pack=alongcodec.getandincrementEncode(self.title)
        self.connection.adjustCorrelationId(pack)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(pack.correlation,True)
        decoded=alongcodec.getandincrementDecode(response)
        return decoded

    def get(self):
        pack=alongcodec.getEncode(self.title)
        self.connection.adjustCorrelationId(pack)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.getPackageWithCorrelationId(pack.correlation,True)
        decoded=alongcodec.getDecode(response)
        return decoded

    def addAndGet(self,delta):
        pack=alongcodec.addandgetEncode(self.title,delta)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        decoded=alongcodec.addandgetDecode(response)
        return decoded

    def compareAndSet(self,expected,updated):
        pack=alongcodec.compareandsetEncode(self.title,expected,updated)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        decoded=alongcodec.compareandsetDecode(response)
        return decoded

    def getAndAdd(self,delta):
        pack=alongcodec.getandaddEncode(self.title, delta)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        decoded=alongcodec.getandaddDecode(response)
        return decoded

    def getAndSet(self,new):
        pack=alongcodec.getandsetEncode(self.title,new)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        decoded=alongcodec.getandsetDecode(response)
        return decoded

    def incrementAndGet(self):
        pack=alongcodec.incrementandgetEncode(self.title)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        decoded=alongcodec.incrementandgetDecode(response)
        return decoded

    def set(self,new):
        pack=alongcodec.setEncode(self.title,new)
        self.connection.sendPackage(pack.encodeMessage())
        response=self.connection.waitAndGetPackage()
        decoded=alongcodec.setDecode(response)
        return decoded