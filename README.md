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

# Push Doc

# push_to_server_proxy_jump

# отправка по ssh с proxy jump

```
# Данные для подключения к промежуточному серверу (Proxy Server)
proxy_host = "proxy.example.com"
proxy_port = 22
proxy_username = "proxy_user"
proxy_password = "proxy_password"

# Данные для подключения к конечному серверу (Target Server)
target_host = "target.example.com"
target_port = 22
target_username = "target_user"
target_password = "target_password"

# Команды, которые необходимо выполнить на конечном сервере
commands = [
    "echo Hello, World!",
    "ls -la",
    "uname -a"
]
```

# Вызываем функцию open_ssh_via_proxy с использованием ProxyJump

```
open_ssh_via_proxy(proxy_host, proxy_port, proxy_username, proxy_password,
                   target_host, target_port, target_username, target_password, commands)
# push_to_server
# отправка по ssh
# Данные для подключения к конечному серверу (Target Server)
host = "target.example.com"
port = 22
username = "target_user"
password = "target_password"

# Команды, которые необходимо выполнить на конечном сервере
commands = [
    "echo Hello, World!",
    "ls -la",
    "uname -a"
]

# Вызываем функцию open_ssh_connection без использования ProxyJump
open_ssh_connection(host, port, username, password, commands)
```
