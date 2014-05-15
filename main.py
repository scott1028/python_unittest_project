# coding:utf-8

import unittest
import cookielib, urllib2, urllib


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1),urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22')]


class NewTests(unittest.TestCase):
    def test_get(self):
        try:
            request = urllib2.Request(url='http://127.0.0.1:3333/api/ssd/subscriber/88695581521/nation/?format=json')
            tmp0 = opener.open(request)
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

        request = urllib2.Request(url='http://127.0.0.1:3333/api/change_password/', data=urllib.urlencode({
            'old_password': '88695581521',
            'new_password': '1234567'
        }))
        request.get_method = lambda: 'POST'
        tmp3 = opener.open(request)
        self.assertEqual(tmp3.getcode(), 202)

        request = urllib2.Request(url='http://127.0.0.1:3333/api/change_password/', data=urllib.urlencode({
            'old_password': '1234567',
            'new_password': '88695581521'
        }))
        request.get_method = lambda: 'POST'
        tmp3 = opener.open(request)
        self.assertEqual(tmp3.getcode(), 202)

if __name__ == '__main__':
    unittest.main()
