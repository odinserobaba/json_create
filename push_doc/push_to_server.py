import paramiko
import time


def open_ssh_console(host, port, username, password, commands):
    # Создаем SSH-клиент
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Подключаемся к удаленному хосту
        ssh.connect(host, port=port, username=username, password=password)

        # Открываем виртуальную консоль
        channel = ssh.invoke_shell()

        # Выводим начальные данные (баннеры и т.д.)
        time.sleep(1)
        output = channel.recv(65535).decode('utf-8')
        print(output)

        # Выполняем команды по очереди
        for command in commands:
            channel.send(command + '\n')
            time.sleep(1)  # Ждем завершения выполнения команды

            # Считываем и выводим результат выполнения команды
            while channel.recv_ready():
                output = channel.recv(65535).decode('utf-8')
                print(output)

        # Закрываем консоль и соединение
        channel.close()
        ssh.close()

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    host = "192.168.0.131"
    username = "nuanred"
    password = "nuclear123F"
    port = 22
    commands = [
        "echo Hello, World!",
        "ls -la",
        "uname -a"
    ]

    open_ssh_console(host, port, username, password, commands)
