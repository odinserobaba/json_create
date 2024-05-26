import paramiko
import time


def open_ssh_connection(host, port, username, password, commands):
    try:
        # Подключаемся к конечному серверу
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, port=port, username=username, password=password)

        # Открываем виртуальную консоль на конечном сервере
        shell_channel = client.invoke_shell()

        # Считываем и выводим начальные данные (баннеры и т.д.)
        time.sleep(1)
        output = shell_channel.recv(65535).decode('utf-8')
        print(output)

        # Выполняем команды по очереди
        for command in commands:
            attempts = 3  # Количество попыток выполнения команды
            while attempts > 0:
                try:
                    # Отправка команды с символом новой строки (Enter)
                    shell_channel.send(command + '\n')
                    time.sleep(1)  # Ждем выполнения команды

                    # Считываем и выводим результат выполнения команды
                    while shell_channel.recv_ready():
                        output = shell_channel.recv(65535).decode('utf-8')
                        print(output)
                    break  # Если команда выполнена успешно, выходим из цикла попыток
                except Exception as e:
                    print(f"Ошибка при выполнении команды: {e}")
                    attempts -= 1  # Уменьшаем количество оставшихся попыток
                    if attempts == 0:
                        print(f"Не удалось выполнить команду: {command}")

        # Закрываем консоль и соединение
        shell_channel.close()
        client.close()

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    host = "example.com"
    port = 22
    username = "your_username"
    password = "your_password"

    commands = [
        "echo Hello, World!",
        "ls -la",
        "uname -a"
    ]

    open_ssh_connection(host, port, username, password, commands)
