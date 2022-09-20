import xml.etree.ElementTree as ET

data = ET.Element("collection")
element1 = ET.SubElement(data, "transformers_movie")
element1.set("title", "Transformers")
element1.set("tomato", "89")
sub_elem1 = ET.SubElement(element1, "type")
sub_elem2 = ET.SubElement(element1, "format")
sub_elem3 = ET.SubElement(element1, "description")
sub_elem1.text = "Anime, sci-fic"
sub_elem2.text = "DVD"
sub_elem3.text = "A scientific fiction"

xml_file = ET.tostring(data)

with open("film1.xml", 'wb') as file1:
    file1.write(xml_file)