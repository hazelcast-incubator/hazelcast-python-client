__author__ = 'Jonathan Brodie'
import sys,datetime,time

from util import util
from util import encode
from hzclient.hazelclient import HazelcastClient
import messagehandler
myglobal=0
class MyEntryHandler():
    def handle(self, key, value, oldValue, mergingValue, eventType, uuid, numberOfAffectedEntries):
        if mergingValue != oldValue:
            print "Value in map has been replaced!"
        print numberOfAffectedEntries
        print "were affected in this event update"


def demo1():
    client=HazelcastClient()
    list=client.getList("my-list")
    while list.Size().response > 0:
        list.RemoveWithIndex(0)
    print "All items from my-list have been removed"
    sys.exit()
def demo2():
    client=HazelcastClient()
    topic=client.getTopic("my-topic")
    string="Alert published by a Python client!"
    topic.publish(util.hzstringbytes(string))
    sys.exit()
def demo3():
    client=HazelcastClient()
    map=client.getMap("my-map")
    registrationId=map.AddEntryListener(True,MyEntryHandler()).response

    while map.Size().response < 50:
        print "Map size is less than 50"
        time.sleep(0.1)

    print "Map size is greater than 50"
    sys.exit()


def demo4():
    client=HazelcastClient()
    list=client.getList("my-list")

    while list.Size().response < 20:
        print "kotor 2 m4-78"
        time.sleep(0.5)

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
    demo1()