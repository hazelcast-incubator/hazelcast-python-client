__author__ = 'Jonathan Brodie'
import sys

from util import util
from util import encode
from hzclient.hazelclient import HazelcastClient
import messagehandler
myglobal=0
class MyEntryHandler():
    def handle(self,key,value, oldValue, mergingValue, eventType, uuid, numberOfAffectedEntries):
        print numberOfAffectedEntries
        print "were affected in this event update"

def main():
    client=HazelcastClient()
    set=client.getSet("my-set")
    testval=util.hzstringbytes("a")
    boolean=set.Contains(testval)
    if boolean.response:
        print "Contains the value!"
    else:
        print "Doesn't contain the value"
    sys.exit()
if __name__ == '__main__':
    main()