import unittest
import os
import json
from datetime import datetime
from json_create.csv_to_json import transform_header, format_date, set_nested_value, csv_to_json


class TestCSVToJson(unittest.TestCase):

    def test_transform_header(self):
        self.assertEqual(transform_header("Name"), "name")
        self.assertEqual(transform_header("Phone"), "data.phone")
        self.assertEqual(transform_header("Unknown"), "Unknown")

    def test_format_date(self):
        self.assertEqual(format_date("1993-01-15"), "15-01-1993")
        self.assertEqual(format_date("invalid-date"), "invalid-date")

    def test_set_nested_value(self):
        data = {}
        set_nested_value(data, "data.phone", "123-456-7890")
        self.assertEqual(data, {"data": {"phone": "123-456-7890"}})
        set_nested_value(data, "data.email", "example@example.com")
        self.assertEqual(
            data, {"data": {"phone": "123-456-7890", "email": "example@example.com"}})

    def test_csv_to_json_single(self):
        csv_content = """Name,Age,City,Phone,Email,DateOfBirth
Alice,30,New York,123-456-7890,alice@example.com,1993-01-15
Bob,25,Los Angeles,987-654-3210,bob@example.com,1998-05-23
Charlie,35,Chicago,555-555-5555,u9G5h@example.com,1988-10-10"""

        csv_file = 'test.csv'
        with open(csv_file, 'w') as f:
            f.write(csv_content)

        csv_to_json(csv_file, ',', 'single')

        with open('output.json', 'r') as f:
            json_data = json.load(f)
            expected_data = [
                {
                    "name": "Alice",
                    "age": 30,
                    "city": "New York",
                    "data": {
                        "phone": "123-456-7890",
                        "email": "alice@example.com"
                    },
                    "date_of_birth": "15-01-1993"
                },
                {
                    "name": "Bob",
                    "age": 25,
                    "city": "Los Angeles",
                    "data": {
                        "phone": "987-654-3210",
                        "email": "bob@example.com"
                    },
                    "date_of_birth": "23-05-1998"
                },
                {
                    "name": "Charlie",
                    "age": 35,
                    "city": "Chicago",
                    "data": {
                        "phone": "555-555-5555",
                        "email": "u9G5h@example.com"
                    },
                    "date_of_birth": "10-10-1988"
                }
            ]
            self.assertEqual(json_data, expected_data)

        os.remove(csv_file)
        os.remove('output.json')

    def test_csv_to_json_multiple(self):
        csv_content = """Name,Age,City,Phone,Email,DateOfBirth
Alice,30,New York,123-456-7890,alice@example.com,1993-01-15
Bob,25,Los Angeles,987-654-3210,bob@example.com,1998-05-23
Charlie,35,Chicago,555-555-5555,u9G5h@example.com,1988-10-10"""

        csv_file = 'test.csv'
        with open(csv_file, 'w') as f:
            f.write(csv_content)

        csv_to_json(csv_file, ',', 'multiple')

        expected_files = [
            'output_jsons/record_1.json',
            'output_jsons/record_2.json',
            'output_jsons/record_3.json'
        ]

        for i, expected_file in enumerate(expected_files):
            with open(expected_file, 'r') as f:
                json_data = json.load(f)
                expected_data = [
                    {
                        "name": "Alice",
                        "age": 30,
                        "city": "New York",
                        "data": {
                            "phone": "123-456-7890",
                            "email": "alice@example.com"
                        },
                        "date_of_birth": "15-01-1993"
                    },
                    {
                        "name": "Bob",
                        "age": 25,
                        "city": "Los Angeles",
                        "data": {
                            "phone": "987-654-3210",
                            "email": "bob@example.com"
                        },
                        "date_of_birth": "23-05-1998"
                    },
                    {
                        "name": "Charlie",
                        "age": 35,
                        "city": "Chicago",
                        "data": {
                            "phone": "555-555-5555",
                            "email": "u9G5h@example.com"
                        },
                        "date_of_birth": "10-10-1988"
                    }
                ]
                self.assertEqual(json_data, expected_data[i])

        os.remove(csv_file)
        for expected_file in expected_files:
            os.remove(expected_file)
        os.rmdir('output_jsons')


if __name__ == '__main__':
    unittest.main()
