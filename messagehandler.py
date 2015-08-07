__author__ = 'jonathanbrodie'

from abc import ABCMeta, abstractmethod
from util import util
class MessageHandler(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def handle(self,item,publishtime,uuid):
        pass

class MyMessageHandler(MessageHandler):
    def handle(self,item,publishtime,uuid):
        newitem=util.decodehzstring(item)
        print newitem