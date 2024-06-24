
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


serviceurl = ' http://py4e-data.dr-chuck.net/comments_1992320.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(serviceurl, context=ctx)
data = uh.read()
#print(type(data))
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)

sum = 0

comments = tree.find('comments')

for comment in comments.findall('comment'):
    sum = sum + int(comment.find('count').text)

print(sum)


