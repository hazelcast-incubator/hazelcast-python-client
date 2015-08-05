__author__ = 'jonathanbrodie'
import unittest,ctypes
import hzclient.codec.mapcodec
import util.encode
class MapCodecTests(unittest.TestCase):

    def testRequest(self):
        testname="map"
        testkey="key"
        testvalue="value"
        testthreadid=10
        testttl=5
        newname=util.encode.encodestring(testname)
        newkey=util.encode.encodestring(testkey)
        newvalue=util.encode.encodestring(testvalue)
        newthreadid=util.encode.encodeint64(testthreadid)
        newttl=util.encode.encodeint64(testttl)
        msg=hzclient.codec.mapcodec.MapPutCodec.encodeRequest(newname,newkey,newvalue,newthreadid,newttl)
        params=hzclient.codec.mapcodec.MapPutCodec.decodeRequest(msg)
        print params.name
        self.assertEqual(params.name,testname)

if __name__ == '__main__':
    unittest.main()