"""
Read a page that consists of a table, add all the numebrs and print the sum. 
"""

from urllib import parse, request, error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_2036924.html"
html = request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('span')
summed = 0
for tag in tags:
    number = str(tag.text)
    summed+=int(number)
print(summed)