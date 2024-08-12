"""
Simple program to show the basic structure of JSON and play with the same. 
"""

import json
data = """{
"name":"Tejas",
"phone":{
"type": "intl",
"number": "+91 123 567"},
"email":{"hide":"yes"}
}
"""

info = json.loads(data)
print("Name: ", info["name"])
print("Hide: ", info["email"]["hide"])