# Модуль xml_utils

## Функции

### `generate_xml(data, root_tag='root')`

```python
xml_string = xml_utils.generate_xml(data, root_tag='people')
```

Генерирует XML строку из словаря или списка данных.

### `validate_xml(xml_string, xsd_file)`

```python
is_valid = xml_utils.validate_xml(xml_string, 'test_xml/schema.xsd')
```

Проверяет XML строку на соответствие XSD схеме.

### `write_xml_to_file(xml_string, filename)`

```python
xml_utils.write_xml_to_file(xml_string, 'out_xml/generated_xml.xml')
```

Записывает XML строку в файл.

### `read_xml_from_file(filename)`

```python
xml_string = xml_utils.read_xml_from_file('test_xml/example.xml')
```

Считывает XML строку из файла.

## Тестирование

В папке `test_data` содержится файл `data.csv` с тестовыми данными, которые можно использовать для генерации XML.

В папке `test_xml` содержатся файлы `example.xml` (пример XML документа) и `schema.xsd` (XSD схема), которые можно использовать для проверки XML.

```bash
python -m unittest xml_test.py
```
