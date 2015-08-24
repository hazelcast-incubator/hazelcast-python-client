__author__ = 'Jonathan Brodie'

import unittest,ctypes

from util import murmurhash
class HashTests(unittest.TestCase):
    def testHash(self):
        print murmurhash.murmur("a231213")
if __name__ == '__main__':
    unittest.main()