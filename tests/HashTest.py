__author__ = 'Jonathan Brodie'

import unittest,ctypes

from util import murmurhash
class HashTests(unittest.TestCase):
    def testHash(self):
        murmurhash.murmur("fookljfadsjfdsjjkdsfjlgsdijasdgiiadgsiosdgii9wg9i9wipweiopiewiopewop")
if __name__ == '__main__':
    unittest.main()