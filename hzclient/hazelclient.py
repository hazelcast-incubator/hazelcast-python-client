__author__ = 'Jonathan Brodie'

from hzclient.proxy.topicproxy import TopicProxy
from hzclient.proxy.proxy import ALongProxy


from hzclient.connectmanager import ConnectionManager


class HazelcastClient(object):
    def __init__(self):
        self.connection=ConnectionManager()
        response=self.connection.getPackageWithCorrelationId(0,True)
        if response is not None:
            print "Connection has been initalized"
        else:
            print "None"

    def getAtomicLong(self,title):
        mylong=ALongProxy(title,self.connection)
        return mylong

    def getTopic(self,title):
        mylong=TopicProxy(title,self.connection)
        return mylong


    def step(self):
        print "TO BE IMPLEMENTED"
