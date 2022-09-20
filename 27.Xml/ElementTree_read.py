import xml.etree.ElementTree as ET

tree = ET.parse("movies.xml")

root = tree.getroot()
print(root)

print(root[0].attrib)
print(root[2][1].text)