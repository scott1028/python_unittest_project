# coding:utf-8

import unittest
import cookielib, urllib2, urllib


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1),urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22')]


class NewTests(unittest.TestCase):
    def test_get(self):
        tmp=opener.open("http://127.0.0.1:3333/api/login/",urllib.urlencode( {'username':'88695581521','password':'88695581521'}))
        self.assertEqual(tmp.getcode(), 200)
        body=tmp.read()
        import pdb; pdb.set_trace()

if __name__ == '__main__':
    unittest.main()
