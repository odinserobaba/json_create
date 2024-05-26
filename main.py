import pandas as pd
import json
import os
from datetime import datetime

# Пример преобразования заголовков CSV в ключи JSON


def transform_header(header):
    header_mapping = {
        "Name": "name",
        "Age": "age",
        "City": "city",
        "Phone": "data.phone",
        "Email": "data.email",
        "DateOfBirth": "date_of_birth"
    }
    return header_mapping.get(header, header)

# Функции для форматирования значений


def format_date(date_str):
    # Пример преобразования даты из "YYYY-MM-DD" в "DD-MM-YYYY"
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d-%m-%Y")
    except ValueError:
        return date_str


# Словарь сопоставления ключей JSON с функциями форматирования
formatters = {
    "date_of_birth": format_date
}


def set_nested_value(data, key, value):
    keys = key.split('.')
    for k in keys[:-1]:
        data = data.setdefault(k, {})
    data[keys[-1]] = value

# Преобразование данных CSV в список JSON-объектов


def csv_to_json(csv_file, delimiter, output_mode):
    df = pd.read_csv(csv_file, delimiter=delimiter)

    json_list = []
    for _, row in df.iterrows():
        json_record = {}
        for col in df.columns:
            json_key = transform_header(col)
            value = row[col]
            if json_key in formatters:
                value = formatters[json_key](value)
            set_nested_value(json_record, json_key, value)
        json_list.append(json_record)

    if output_mode == 'single':
        output_file = 'output.json'
        with open(output_file, 'w') as f:
            json.dump(json_list, f, indent=4)
        print(f'JSON данные успешно сохранены в файл {output_file}')
    elif output_mode == 'multiple':
        output_dir = 'output_jsons'
        os.makedirs(output_dir, exist_ok=True)
        for i, json_record in enumerate(json_list):
            output_file = os.path.join(output_dir, f'record_{i + 1}.json')
            with open(output_file, 'w') as f:
                json.dump(json_record, f, indent=4)
        print(f'JSON данные успешно сохранены в папку {output_dir}')


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Convert CSV to JSON.')
    parser.add_argument('csv_file', type=str, help='Path to the CSV file.')
    parser.add_argument('--delimiter', type=str, default=',',
                        help='CSV delimiter (default is ",").')
    parser.add_argument('--output_mode', type=str, choices=['single', 'multiple'], default='single',
                        help='Output mode: "single" for one JSON file, "multiple" for separate JSON files (default is "single").')

    args = parser.parse_args()
    csv_to_json(args.csv_file, args.delimiter, args.output_mode)
