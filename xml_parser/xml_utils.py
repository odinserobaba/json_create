import xml.etree.ElementTree as ET
from lxml import etree as lxml_etree


def create_xml_element(parent, tag, text=None, attributes=None):
    if attributes is None:
        attributes = {}
    element = ET.SubElement(parent, tag, attrib=attributes)
    if text:
        element.text = text
    return element


def generate_xml(data: list[dict[str, str]], root_tag: str = 'people') -> str:
    root = ET.Element(root_tag)
    for person_data in data:
        person_element = ET.SubElement(root, 'person')
        for key, value in person_data.items():
            ET.SubElement(person_element, key).text = value
    return ET.tostring(root, encoding='unicode')


def _generate_xml_recursive(parent, data):
    if isinstance(data, dict):
        for key, value in data.items():
            child = create_xml_element(parent, key)
            _generate_xml_recursive(child, value)
    elif isinstance(data, list):
        for item in data:
            _generate_xml_recursive(parent, item)
    else:
        parent.text = str(data)


def validate_xml(xml_string, xsd_file):
    xml_doc = lxml_etree.fromstring(xml_string)
    schema = lxml_etree.XMLSchema(lxml_etree.parse(xsd_file))
    return schema.validate(xml_doc)


def write_xml_to_file(xml_string, filename):
    with open(filename, 'w') as file:
        file.write(xml_string)


def read_xml_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()
