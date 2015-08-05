__author__ = 'Jonathan Brodie'
import unittest,ctypes
from hzclient.hazelclient import HazelcastClient
from util import murmurhash
class ALongTests(unittest.TestCase):

    def testset(self):
        client=HazelcastClient()
        newLong=client.getAtomicLong("counter")
        newLong.set(0)
        self.assertEqual(0,newLong.get())

    def testset2(self):
        client=HazelcastClient()
        newLong=client.getAtomicLong("counter")
        newLong.set(0)
        self.assertEqual(1,newLong.incrementAndGet())

    def testset3(self):
        client=HazelcastClient()
        newLong=client.getAtomicLong("counter")
        newLong.set(0)
        self.assertEqual(0,newLong.getAndIncrement())



if __name__ == '__main__':
    unittest.main()
