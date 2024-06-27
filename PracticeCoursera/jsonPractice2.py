import json
import urllib.request, urllib.parse, urllib.error
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

address = input('Enter location: ')
address = address.strip()

parms = dict()
parms['q'] = address
url = serviceurl + urllib.parse.urlencode(parms)
print(parms)
uh = urllib.request.urlopen(url,context=ctx)
print('Retrieving', url)

data = uh.read().decode()
#print(data)
jsonData = json.loads(data)
print(jsonData)

plus_code = jsonData['features'][0]['properties']['plus_code']
print(plus_code)

