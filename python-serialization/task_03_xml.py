#!/usr/bin/python3
"""
XML ser and deser..
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """ serialization function"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """deserialization function"""
    tree = ET.parse(filename)
    root = tree.getroot()
    
    data = {}
    for child in root:
        data[child.tag] = child.text
    
    return data
