import json
import urllib.request, urllib.parse, urllib.error
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#while True:
url = "http://py4e-data.dr-chuck.net/comments_1992321.json"
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())

info = json.loads(data)
print(info)

comments = info['comments']
#print(comments[0]['name'])

sum = 0

for item in comments:
    #print('Name', item['name'])
    #print('Count', item['count'])
    sum = sum + item['count']

print(sum)
   