__author__ = 'Jonathan Brodie'
import sys,datetime

from util import util
from util import encode
from hzclient.hazelclient import HazelcastClient
import messagehandler
myglobal=0
class MyEntryHandler():
    def handle(self,key,value, oldValue, mergingValue, eventType, uuid, numberOfAffectedEntries):
        print numberOfAffectedEntries
        print "were affected in this event update"


def demo1():
    client=HazelcastClient()
    list=client.getList("my-list")
    while list.Size().response > 0:
        list.RemoveWithIndex(0)
    print "All items from my-list have been removed"

def main():
    client=HazelcastClient()
    set=client.getList("my-list")
    print "Start time"
    print datetime.datetime.now()
    for i in range(100):
        set.Get(i)
    print datetime.datetime.now()

    sys.exit()
if __name__ == '__main__':
    main()