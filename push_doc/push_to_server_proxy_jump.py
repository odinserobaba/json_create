import paramiko
import time


def open_ssh_via_proxy(proxy_host, proxy_port, proxy_username, proxy_password,
                       target_host, target_port, target_username, target_password, commands):
    try:
        # Подключаемся к промежуточному серверу (Proxy Server)
        proxy_client = paramiko.SSHClient()
        proxy_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        proxy_client.connect(proxy_host, port=proxy_port,
                             username=proxy_username, password=proxy_password)

        # Открываем транспортный канал через Proxy Server к конечному серверу
        transport = proxy_client.get_transport()
        dest_addr = (target_host, target_port)
        local_addr = ('localhost', 0)
        channel = transport.open_channel("direct-tcpip", dest_addr, local_addr)

        # Подключаемся к конечному серверу через созданный туннель
        target_client = paramiko.SSHClient()
        target_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        target_client.connect(target_host, port=target_port,
                              username=target_username, password=target_password, sock=channel)

        # Открываем виртуальную консоль на конечном сервере
        shell_channel = target_client.invoke_shell()

        # Считываем и выводим начальные данные (баннеры и т.д.)
        time.sleep(1)
        output = shell_channel.recv(65535).decode('utf-8')
        print(output)

        # Выполняем команды по очереди
        for command in commands:
            shell_channel.send(command + '\n')
            time.sleep(1)  # Ждем завершения выполнения команды

            # Считываем и выводим результат выполнения команды
            while shell_channel.recv_ready():
                output = shell_channel.recv(65535).decode('utf-8')
                print(output)

        # Закрываем консоль и соединение
        shell_channel.close()
        target_client.close()
        proxy_client.close()

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    proxy_host = "proxy.example.com"
    proxy_port = 22
    proxy_username = "proxy_user"
    proxy_password = "proxy_password"

    target_host = "target.example.com"
    target_port = 22
    target_username = "target_user"
    target_password = "target_password"

    commands = [
        "echo Hello, World!",
        "ls -la",
        "uname -a"
    ]

    open_ssh_via_proxy(proxy_host, proxy_port, proxy_username, proxy_password,
                       target_host, target_port, target_username, target_password, commands)
