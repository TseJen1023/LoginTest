#Unit test:

#v1. Test the function that verifies if the credentials match with different test cases.
#v2. Write it using python unittest or pytest.
from selenium import webdriver
import unittest

class unit(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/home/yang/Desktop/Selenium/chromedriver")

    def testcorrect(self):
        url = 'http://localhost:5000/login'
        self.browser.get(url)

        usernameinput = self.browser.find_element_by_id("username")
        usernameinput.send_keys("aaaa")

        passwordinput = self.browser.find_element_by_id("password")
        passwordinput.send_keys("aaaa")

        buttonclick = self.browser.find_element_by_id("button")
        buttonclick.click()

        checkUrl = 'http://localhost:5000/right/aaaa'
        if self.browser.current_url == checkUrl :
            print("test is correct")
        else:
            print("test is failed")

    def testfailed(self):
        url = 'http://localhost:5000/login'
        self.browser.get(url)

        usernameinput = self.browser.find_element_by_id("username")
        usernameinput.send_keys("aaaa")

        passwordinput = self.browser.find_element_by_id("password")
        passwordinput.send_keys("1234")

        buttonclick = self.browser.find_element_by_id("button")
        buttonclick.click()

        checkUrl = 'http://localhost:5000/right/aaaa'
        if self.browser.current_url == checkUrl :
            print("test is correct")
        else:
            print("test is failed")


    def tearDown(self):
        self.browser.quit()



if __name__ == '__main__':
    unittest.main()
