import csv
from xml_utils import generate_xml, validate_xml, write_xml_to_file

# Чтение данных из CSV файла
data = []
with open('test_data/data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Генерация XML строки из данных
xml_string = generate_xml(data, root_tag='people')

# Запись XML строки в файл
write_xml_to_file(xml_string, 'out_xml/generated_xml.xml')

# Проверка XML строки на соответствие XSD схеме
is_valid = validate_xml(xml_string, 'test_xml/schema.xsd')
if is_valid:
    print("XML соответствует XSD схеме.")
else:
    print("XML не соответствует XSD схеме.")
