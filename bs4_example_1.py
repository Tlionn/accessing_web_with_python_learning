"""
Program to read the anchor tags in a document using Beautiful Soup.
"""

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

#Ignore SSL certificate errors...
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter the URL: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))