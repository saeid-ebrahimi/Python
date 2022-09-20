# Program to read JSON file
# and generate its XML file

# Importing json module and xml
# module provided by python
import json as JS
import xml.etree.ElementTree as ET

with open("myfile3.json", "r") as json_file:
    # loading json file
    # to variable data
    data = JS.load(json_file)

    # building the root element
    # of the xml file
    root = ET.Element("quiz")

    # Building the sub root elements
    # we don't add text since the value
    # associated with subelement is a python dictionary

    Maths = ET.SubElement(root, "maths")

    # Building subelement of maths as q1
    Q1 = ET.SubElement(Maths, "q1")
    ET.SubElement(Q1, "question")
    text = data["quiz"]["maths"]["q1"]["question"]
    # Building multiple subelements with name options to hold different values
    # Xml elements cannot hold integer values so we need to
    # convert them to string
    ET.SubElement(Q1, "options").text = str(data["quiz"]["maths"]["q1"]["options"][0])
    ET.SubElement ( Q1 , "options" ).text = str ( data [ "quiz" ]
                                                  [ "maths" ] [ "q1" ]
                                                  [ "options" ] [ 1 ] )

    ET.SubElement ( Q1 , "options" ).text = str ( data [ "quiz" ]
                                                  [ "maths" ] [ "q1" ]
                                                  [ "options" ] [ 2 ] )

    ET.SubElement ( Q1 , "options" ).text = str ( data [ "quiz" ]
                                                  [ "maths" ] [ "q1" ]
                                                  [ "options" ] [ 3 ] )
    ET.SubElement ( Q1 , "answer" ).text = str ( data [ "quiz" ]
                                                 [ "maths" ] [ "q1" ]
                                                 [ "answer" ] )

    # Building subelement of maths as q2
    Q2 = ET.SubElement ( Maths , "q2" )
    ET.SubElement( Q2 , "question" ).text = data[ "quiz" ][ "maths" ] [ "q2" ] [ "question" ]

    # Building multiple subelements
    # with name options to hold
    # different values
    ET.SubElement ( Q2 , "options" ).text = str ( data [ "quiz" ]
                                                  [ "maths" ]
                                                  [ "q2" ]
                                                  [ "options" ] [ 0 ] )

    ET.SubElement ( Q2 , "options" ).text = str ( data [ "quiz" ]
                                                  [ "maths" ]
                                                  [ "q2" ]
                                                  [ "options" ] [ 1 ] )

    ET.SubElement ( Q2 , "options" ).text = str ( data [ "quiz" ]
                                                  [ "maths" ] [ "q2" ]
                                                  [ "options" ] [ 2 ] )

    ET.SubElement ( Q2 , "options" ).text = str ( data [ "quiz" ]
                                                  [ "maths" ] [ "q2" ]
                                                  [ "options" ] [ 3 ] )

    ET.SubElement ( Q2 , "answer" ).text = str ( data [ "quiz" ]
                                                 [ "maths" ] [ "q2" ]
                                                 [ "answer" ] )

    # Building the tree of the xml
    # elements using the root element
    tree = ET.ElementTree ( root )

    # Writing the xml to output file
    tree.write("quiz.xml")
