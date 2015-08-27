__author__ = 'Jonathan Brodie'
import sys,datetime,time

from util import util
from util import encode
from hzclient.hazelclient import HazelcastClient
from hzclient.config import Config
import messagehandler


class MyEntryHandler():
    def __init__(self):
        self.count=0
    def handle(self, key, value, oldValue, mergingValue, eventType, uuid, numberOfAffectedEntries):
        print str(numberOfAffectedEntries)+" were affected in this event update"



def demo1():
    config=Config()
    config.set_username("dev")
    config.set_password("dev-pass")
    client=HazelcastClient(config)
    list=client.getList("my-list")
    i=0
    while list.Size() > 0:
        list.RemoveWithIndex(0)
    print "All items from my-list have been removed"
    sys.exit()
def demo2():
    config=Config()
    config.set_username("dev")
    config.set_password("dev-pass")
    client=HazelcastClient(config)
    topic=client.getTopic("my-topic")
    string="Alert published by a Python client!"
    topic.publish(util.hzstringbytes(string))
    sys.exit()
def demo3():
    print "uh"
    config=Config()
    config.set_username("dev")
    config.set_password("dev-pass")
    client=HazelcastClient(config)
    print "uh"
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
        time.sleep(0.5)

def main():
    config=Config()
    config.set_username("dev")
    config.set_password("dev-pass")
    client=HazelcastClient(config)
    set=client.getList("my-list")
    print "Start time"
    start=datetime.datetime.now()
    print datetime.datetime.now()
    for i in range(1000):
        print i
        set.Get(i)
    print "finish"
    print start
    print datetime.datetime.now()

    sys.exit()
if __name__ == '__main__':
    demo3()