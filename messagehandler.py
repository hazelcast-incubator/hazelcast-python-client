__author__ = 'jonathanbrodie'

from abc import ABCMeta, abstractmethod
from util import util
class MessageHandler(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def handle(self,item,publishtime,uuid):
        pass

class EntryHandler(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def handle(self,key,value, oldValue, mergingValue, eventType, uuid, numberOfAffectedEntries):
        pass

class MyMessageHandler(MessageHandler):
    def handle(self,item,publishtime,uuid):
        newitem=util.decodehzstring(item)
        print newitem
class MyEntryHandler(EntryHandler):
    def handle(self,key,value, oldValue, mergingValue, eventType, uuid, numberOfAffectedEntries):
        print "EVENT UPDATE"