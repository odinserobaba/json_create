import unittest
import xml_utils
import xml.etree.ElementTree as ET


class TestXMLUtils(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"name": "Alice", "age": "30", "city": "New York"},
            {"name": "Bob", "age": "35", "city": "Los Angeles"}
        ]

    def test_generate_xml(self):
        xml_string = xml_utils.generate_xml(self.data, root_tag='people')
        self.assertTrue(xml_string.startswith("<people>"))
        self.assertTrue(xml_string.endswith("</people>"))

    def test_validate_xml_invalid(self):
        # Создаем недействительный XML документ
        root = ET.Element("people")
        person = ET.SubElement(root, "person")
        name = ET.SubElement(person, "name")
        name.text = "Alice"
        # Отсутствует обязательный элемент age
        xml_string = ET.tostring(root, encoding="unicode")
        is_valid = xml_utils.validate_xml(xml_string, 'test_xml/schema.xsd')
        self.assertFalse(is_valid)

    # Остальные тесты оставляем без изменений

    def test_read_xml_from_file(self):
        xml_string = xml_utils.read_xml_from_file('test_xml/example.xml')
        self.assertTrue(xml_string.startswith("<people>"))
        self.assertTrue(xml_string.endswith("</people>"))

    def test_write_xml_to_file(self):
        xml_string = xml_utils.generate_xml(self.data, root_tag='people')
        xml_utils.write_xml_to_file(xml_string, 'out_xml/generated_xml.xml')
        with open('out_xml/generated_xml.xml', 'r') as f:
            written_xml = f.read()
        self.assertEqual(xml_string, written_xml)


if __name__ == '__main__':
    unittest.main()
