import paramiko
import os


def save_to_text_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Результаты сохранены в файл: {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")


def save_to_csv_file(filename, data, headers=None):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            if headers:
                writer.writerow(headers)
            for row in data:
                writer.writerow(row)
        print(f"Результаты сохранены в CSV файл: {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении CSV файла: {e}")


def send_file_via_ssh_with_proxy(proxy_host, proxy_port, proxy_username, proxy_password,
                                 target_host, target_port, target_username, target_password,
                                 local_file, remote_path):
    try:
        proxy_client = paramiko.SSHClient()
        proxy_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        proxy_client.connect(proxy_host, port=proxy_port,
                             username=proxy_username, password=proxy_password)

        transport = proxy_client.get_transport()
        dest_addr = (target_host, target_port)
        local_addr = ('localhost', 0)
        channel = transport.open_channel("direct-tcpip", dest_addr, local_addr)

        target_client = paramiko.SSHClient()
        target_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        target_client.connect(target_host, port=target_port,
                              username=target_username, password=target_password, sock=channel)

        sftp = target_client.open_sftp()
        sftp.put(local_file, os.path.join(
            remote_path, os.path.basename(local_file)))
        print(
            f"Файл {local_file} успешно отправлен на {target_host}:{remote_path}")
        sftp.close()
        target_client.close()
        proxy_client.close()
    except Exception as e:
        print(f"Ошибка при отправке файла по SSH: {e}")


def send_folder_via_ssh_with_proxy(proxy_host, proxy_port, proxy_username, proxy_password,
                                   target_host, target_port, target_username, target_password,
                                   local_folder, remote_path):
    try:
        proxy_client = paramiko.SSHClient()
        proxy_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        proxy_client.connect(proxy_host, port=proxy_port,
                             username=proxy_username, password=proxy_password)

        transport = proxy_client.get_transport()
        dest_addr = (target_host, target_port)
        local_addr = ('localhost', 0)
        channel = transport.open_channel("direct-tcpip", dest_addr, local_addr)

        target_client = paramiko.SSHClient()
        target_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        target_client.connect(target_host, port=target_port,
                              username=target_username, password=target_password, sock=channel)

        sftp = target_client.open_sftp()
        for root, dirs, files in os.walk(local_folder):
            for file in files:
                local_path = os.path.join(root, file)
                remote_file_path = os.path.join(
                    remote_path, os.path.relpath(local_path, local_folder))
                sftp.put(local_path, remote_file_path)
        print(
            f"Папка {local_folder} успешно отправлена на {target_host}:{remote_path}")
        sftp.close()
        target_client.close()
        proxy_client.close()
    except Exception as e:
        print(f"Ошибка при отправке папки по SSH: {e}")


def download_file_via_ssh_with_proxy(proxy_host, proxy_port, proxy_username, proxy_password,
                                     target_host, target_port, target_username, target_password,
                                     remote_file, local_path):
    try:
        proxy_client = paramiko.SSHClient()
        proxy_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        proxy_client.connect(proxy_host, port=proxy_port,
                             username=proxy_username, password=proxy_password)

        transport = proxy_client.get_transport()
        dest_addr = (target_host, target_port)
        local_addr = ('localhost', 0)
        channel = transport.open_channel("direct-tcpip", dest_addr, local_addr)

        target_client = paramiko.SSHClient()
        target_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        target_client.connect(target_host, port=target_port,
                              username=target_username, password=target_password, sock=channel)

        sftp = target_client.open_sftp()
        sftp.get(remote_file, os.path.join(
            local_path, os.path.basename(remote_file)))
        print(
            f"Файл {remote_file} успешно загружен с {target_host} в {local_path}")
        sftp.close()
        target_client.close()
        proxy_client.close()
    except Exception as e:
        print(f"Ошибка при загрузке файла по SSH: {e}")


def download_folder_via_ssh_with_proxy(proxy_host, proxy_port, proxy_username, proxy_password,
                                       target_host, target_port, target_username, target_password,
                                       remote_folder, local_path):
    try:
        proxy_client = paramiko.SSHClient()
        proxy_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        proxy_client.connect(proxy_host, port=proxy_port,
                             username=proxy_username, password=proxy_password)

        transport = proxy_client.get_transport()
        dest_addr = (target_host, target_port)
        local_addr = ('localhost', 0)
        channel = transport.open_channel("direct-tcpip", dest_addr, local_addr)

        target_client = paramiko.SSHClient()
        target_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        target_client.connect(target_host, port=target_port,
                              username=target_username, password=target_password, sock=channel)

        sftp = target_client.open_sftp()
        for file in sftp.listdir(remote_folder):
            remote_file_path = os.path.join(remote_folder, file)
            local_file_path = os.path.join(local_path, file)
            sftp.get(remote_file_path, local_file_path)
        print(
            f"Папка {remote_folder} успешно загружена с {target_host} в {local_path}")
        sftp.close()
        target_client.close()
        proxy_client.close()
    except Exception as e:
        print(f"Ошибка при загрузке папки по SSH: {e}")
