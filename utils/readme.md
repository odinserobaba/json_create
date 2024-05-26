# Модуль utils

## Функции

### `save_to_text_file(filename, content)`

```python
utils.save_to_text_file("example.txt", "Hello, World!")
```

### `save_to_csv_file(filename, data, headers=None)`

```python
data = [
    ["Name", "Age"],
    ["Alice", 25],
    ["Bob", 30]
]
utils.save_to_csv_file("example.csv", data)
```

### `send_file_via_ssh_with_proxy(...)`

```python
utils.send_file_via_ssh_with_proxy(proxy_host, proxy_port, proxy_username, proxy_password,
                                   target_host, target_port, target_username, target_password,
                                   local_file, remote_path)
```

### `send_folder_via_ssh_with_proxy(...)`

```python
utils.send_folder_via_ssh_with_proxy(proxy_host, proxy_port, proxy_username, proxy_password,
                                     target_host, target_port, target_username, target_password,
                                     local_folder, remote_path)
```

### `download_file_via_ssh_with_proxy(...)`

```python
utils.download_file_via_ssh_with_proxy(proxy_host, proxy_port, proxy_username, proxy_password,
                                       target_host, target_port, target_username, target_password,
                                       remote_file, local_path)
```

### `download_folder_via_ssh_with_proxy(...)`

```python
utils.download_folder_via_ssh_with_proxy(proxy_host, proxy_port, proxy_username, proxy_password,
                                         target_host, target_port, target_username, target_password,
                                         remote_folder, local_path)
```
