# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url)< 1:
    url = " http://py4e-data.dr-chuck.net/comments_1992318.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all the span tags and pull the numbers from the span tags
tags = soup('span')
sum = 0
count = 0
for tag in tags:
    data = tag.decode()
    number = re.findall('<span .+?>([0-9][0-9]?).+>', data)
    value = int(number[0])
    count += 1
    sum= sum+ value
    '''print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)'''

print(sum, count)

#print(sumOfTags)
