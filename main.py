__author__ = 'Jonathan Brodie'
import sys

from util import util
from hzclient.hazelclient import HazelcastClient
def main():
    client=HazelcastClient()
    mytopic=client.getTopic("my-topic")
    update=util.hzstringbytes("Python update on topic")
    mytopic.publish(update)
if __name__ == '__main__':
    main()

