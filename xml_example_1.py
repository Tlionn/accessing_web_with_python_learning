"""
Basic program to use ElementTree
"""
import xml.etree.ElementTree as ET

data = """<person>
    <name>Tejas</name>
    <phone type="intl">+91 754 233</phone>
    <email hide="yes"/>
</person>

"""

tree = ET.fromstring(data)
print("Name: ", tree.find("name").text)
print("Attr: ", tree.find("email").get("hide"))