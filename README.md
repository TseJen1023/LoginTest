# LoginTest

## Structure

A simple login web page. **Front-end** written in HTML and **Back-end** implemented by flask framework.

According to test automation pyramid, 3 different types of tests : **Unit Test**, **Api Test** and **UI Test**.

![](https://i.imgur.com/45JBCX0.png)


## [Front-end](https://github.com/TseJen1023/LoginTest/tree/master/templates)
1. A web page for user to enter user name, password and a button to login.
2. Sends an HTTP web request when login button is pressed.
3. Display login success or failed message after getting response from back-end.
4. Write it in html.
## [Back-end](https://github.com/TseJen1023/LoginTest/blob/master/app.py)
1. Gets requests from front-end and verify if the credentials match.
2. Response match or not to front-end.
3. Write it with python and flask framework.
## [Unit Test](https://github.com/TseJen1023/LoginTest/blob/master/unitTest.py)
1. Test the function that verifies if the credentials match with different test cases.
2. Write it using python unittest or pytest.
## [Api Test](https://github.com/TseJen1023/LoginTest/blob/master/apiTest.py)
1. Test back-end service to see if it responses correctly.
2. Write it with python requests module.
## [UI Test](https://github.com/TseJen1023/LoginTest/blob/master/pycharm/first/TestCases/TC_001.robot)
 1. End to end tests to see if the whole feature works.
2. Write it using python Robot framework.
