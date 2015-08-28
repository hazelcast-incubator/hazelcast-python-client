__author__ = 'Jonathan Brodie'

from hzclient.proxy.topicproxy import TopicProxy
from hzclient.proxy.alongproxy import AtomicLongProxy
from hzclient.proxy.mapproxy import MapProxy
from hzclient.proxy.setproxy import SetProxy
from hzclient.proxy.listproxy import ListProxy
from hzclient.proxy.arefproxy import AtomicReferenceProxy
from hzclient.proxy.cacheproxy import CacheProxy
from hzclient.proxy.queueproxy import QueueProxy
from hzclient.proxy.lockproxy import LockProxy


from hzclient.connectmanager import ConnectionManager


class HazelcastClient(object):
    def __init__(self,config):
        self.connection=ConnectionManager(config,smart=True)

    def getAtomicLong(self,title):
        mylong=AtomicLongProxy(title,self.connection)
        return mylong
    def getAtomicReference(self,title):
        return AtomicReferenceProxy(title,self.connection)
    def getCache(self,title):
        return CacheProxy(title,self.connection)
    def getList(self,title):
        list=ListProxy(title,self.connection)
        return list
    def getLock(self,title):
        return LockProxy(title,self.connection)
    def getMap(self,title):
        mylong=MapProxy(title,self.connection)
        return mylong
    def getQueue(self,title):
        return QueueProxy(title,self.connection)
    def getSet(self,title):
        set=SetProxy(title,self.connection)
        return set
    def getTopic(self,title):
        mylong=TopicProxy(title,self.connection)
        return mylong


