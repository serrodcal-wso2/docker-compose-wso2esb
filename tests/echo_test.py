import http.client

headers = {"Content-type": "application/json"}

c = http.client.HTTPConnection('localhost', 8280)
c.request('POST', '/echo/wiremock', None, headers)
response = c.getresponse()
data = response.read()
c.close()

data = data.decode('utf-8')

if response.status == 200 and data == u'Hello world!':
    print("Test passed")
else:
    print("Test failed")
