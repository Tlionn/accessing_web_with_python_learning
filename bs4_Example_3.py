"""
Bad code to go into links defined at a particular position, a given number of times.  
Enough at the time, but can make the recursive calling into a function and call it a given number of times. 
"""

from urllib import parse, request, error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

position = input("Enter position:")
count = input("enter count:")

url = "http://py4e-data.dr-chuck.net/known_by_Nayan.html"
html = request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

for i in range(int(count-1)):
    tags = soup('a')
    url = tags[int(position)].get('href',None)
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
print(tags[int(position)].text)