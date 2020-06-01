#Api test:

#v1. Test back-end service to see if it responses correctly.
#v2. Write it with python requests module.

import requests

url = "http://127.0.0.1:5000/login"

payload = 'username=aaaa&password=aaaa'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
