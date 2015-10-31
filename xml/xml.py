import xml.etree.ElementTree as ET
from urllib.request import urlopen

#example 1
url = "http://webapi.legistar.com/v1/seattle/matters"
import xml.etree.ElementTree as ET
tree = ET.parse('matters.xml')
root = tree.getroot()
print(root)
for child in root:
    for matter in child:
        print(matter.tag, matter.text)

#example 2
import xml.etree.ElementTree as ET
tree = ET.parse('matters.xml')
root = tree.getroot()
print(root)
for child in root:
    for matter in child:
        print(matter.tag, matter.text)

