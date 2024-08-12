import urllib.request
import json

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2036927.json'

uh = urllib.request.urlopen(url)
data = uh.read()
js = json.loads(data)

summed = 0
for item in js["comments"]:
    summed+=item["count"]

print(summed)