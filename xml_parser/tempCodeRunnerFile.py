
import unittest
import os
import xml_parser.xml_parser as xml_parser


class TestXMLUtils(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"name": "Alice", "age": 30, "city": "New York"},
            {"name": "Bob", "age": 35, "city": "Los Angeles"}
        ]

    def test_generate_xml(self):
        xml_string = xml_parser.generate_xml(self.data, root_tag='people')
        self.assertIsInstance(xml_string, str)
        self.assertTrue(xml_string.startswith("<people>"))
        self.assertTrue(xml_string.endswith("</people>"))

    def test_validate_xml_valid(self):
        example_xml = """<people><person><name>Alice</name><age>30</age><city>New York</city></person><person><name>Bob</name><age>35</age><city>Los Angeles</city></person></people>"""
        is_valid = xml_parser.validate_xml(example_xml, 'schema.xsd')
        self.assertTrue(is_valid)

    def test_validate_xml_invalid(self):
        invalid_xml = """<people><person><name>Alice</name><age>thirty</age><city>New York</city></person><person><name>Bob</name><age>35</age><city>Los Angeles</city></person></people>"""
        is_valid = xml_parser.validate_xml(invalid_xml, 'schema.xsd')
        self.assertFalse(is_valid)

    def test_read_xml_from_file(self):
        xml_string = xml_parser.read_xml_from_file('example.xml')
        self.assertIsInstance(xml_string, str)
        self.assertTrue(xml_string.startswith("<people>"))
        self.assertTrue(xml_string.endswith("</people>"))

    def test_write_xml_to_file(self):
        xml_string = xml_parser.generate_xml(self.data, root_tag='people')
        xml_parser.write_xml_to_file(xml_string, 'test.xml')
        self.assertTrue(os.path.exists('test.xml'))
        os.remove('test.xml')


if __name__ == '__main__':
    unittest.main()
