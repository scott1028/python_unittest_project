# coding:utf-8

import unittest
import cookielib, urllib2, urllib


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1),urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22')]


class NewTests(unittest.TestCase):
    def test_get(self):
        try:
            tmp0 = opener.open('http://127.0.0.1:3333/api/ssd/subscriber/88695581521/nation/?format=json')
        except Exception as e:
            self.assertEqual(e.getcode(), 401)

        tmp1 = opener.open("http://127.0.0.1:3333/api/login/",urllib.urlencode({
            'username':'88695581521',
            'password':'88695581521'
        }))

        self.assertEqual(tmp1.getcode(), 200)
        body1 = tmp1.read()

        tmp2 = opener.open('http://127.0.0.1:3333/api/ssd/subscriber/88695581521/nation/?format=json')
        self.assertEqual(tmp2.getcode(), 200)
        body2 = tmp2.read()

if __name__ == '__main__':
    unittest.main()
