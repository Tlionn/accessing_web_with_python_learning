"""
A program to understand the use of the findall and find methods. 
"""

import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2036926.xml'
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

tags = tree.findall("comments/comment")
count = 0
for tag in tags:
    count+=int(str(tag.find("count").text))
print(count)