__author__ = 'Jonathan Brodie'


from hzclient.clientmessage import ClientMessage
from hzclient.clientmessage import AuthenticationMessage


import unittest,ctypes
from util import util

class UtilTests(unittest.TestCase):

    def testDecodeEncode(self):
        mystring="dad"
        bytestuff=util.hzstringbytes(mystring)
        newstring=util.decodehzstring(bytestuff)
        self.assertEqual(mystring,newstring)
if __name__ == '__main__':
    unittest.main()

