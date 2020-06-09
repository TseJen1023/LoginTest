#Api test:

#v1. Test back-end service to see if it responses correctly.
#v2. Write it with python requests module.

import requests
import unittest
class api(unittest.TestCase):
    def test_valid_1(self):
        url = "http://127.0.0.1:5000/login"
        payload = 'username=aaaa&password=aaaa'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data = payload)

        #print(response.text.find('right'))
        #print(response.text.find('error'))
        self.assertEqual(response.text.find('right'), 100)
        self.assertEqual(response.status_code ,200)

    def test_invalid_2(self):
        url = "http://127.0.0.1:5000/login"
        payload = 'username=tttt&password=aaada'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data = payload)

        #print(response.text)
        self.assertEqual(response.text.find('error'), 100)
        self.assertEqual(response.status_code ,200)

if __name__ == '__main__':
    unittest.main()
