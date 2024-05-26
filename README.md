# json_create

## Сохранение в один файл JSON:

```
python csv_to_json.py your_file.csv --delimiter ',' --output_mode single

```

## Сохранение каждого JSON в отдельный файл:

```
python csv_to_json.py your_file.csv --delimiter ',' --output_mode multiple


```

```
Аргументы командной строки:

csv_file: Путь к CSV-файлу.
--delimiter: Разделитель CSV (по умолчанию ,).
--output_mode: Режим вывода: single для одного файла JSON, multiple для отдельных файлов JSON.
```

python csv_to_json.py test_data/example.csv --delimiter ',' --output_mode single

# Тесты функций преобразования:

```
test_transform_header проверяет правильность преобразования заголовков CSV в ключи JSON.
test_format_date проверяет правильность преобразования даты.
test_set_nested_value проверяет установку вложенных значений в JSON-объекте.
```

# Тесты основной функции:

```
test_csv_to_json_single проверяет преобразование данных из CSV в один JSON-файл.
test_csv_to_json_multiple проверяет преобразование данных из CSV в несколько JSON-файлов.
```

```
python test_csv_to_json.py

```
