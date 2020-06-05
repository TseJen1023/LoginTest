#Unit test:

#v1. Test the function that verifies if the credentials match with different test cases.
#v2. Write it using python unittest or pytest.
from selenium import webdriver
from app import login_check
import unittest

class unit(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(login_check('aaaa','aaaa') , 1)

    def test_invalid(self):
        self.assertEqual(login_check('aaaa','aaav') , 1)

    def test_too_long(self):
        self.assertEqual(login_check('aaaaaaaaaaaaaaaaaaaaaaa','aaaaaaaaaaaaaaaaaaaaaaaaa'),1)





if __name__ == '__main__':
    unittest.main()
