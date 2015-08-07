__author__ = 'Jonathan Brodie'
import sys

from util import util
from util import encode
from hzclient.hazelclient import HazelcastClient
import messagehandler
class MyEntryHandler():
    def handle(self,key,value, oldValue, mergingValue, eventType, uuid, numberOfAffectedEntries):
        print "EVENT UPDATE: "
        print eventType
        print "\n"
        print numberOfAffectedEntries
        print "were affected in this event update"

def main():
    client=HazelcastClient()
    mymap=client.getMap("my-map")
    mymap.AddEntryListener(encode.encodeboolean(True), MyEntryHandler())
    while mymap.Size().response < 100:
        print mymap.Size().response
    print "we made it?"
    sys.exit()
if __name__ == '__main__':
    main()