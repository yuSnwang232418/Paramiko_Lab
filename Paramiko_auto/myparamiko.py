import paramiko
import time
import getpass
from datetime import datetime


def connect(server_ip, server_port, username, config):
    password = 'wyx'
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {server_ip}')
    ssh_client.connect(hostname=server_ip, port=server_port, username=username, password=password,
                       look_for_keys=False, allow_agent=False)
    return ssh_client


def get_shell(ssh_client):
    shell = ssh_client.invoke_shell()
    return shell


def send_shell_command(shell, command, timeout=1):
    print(f'Sending command: {command}')
    shell.send(command + '\n')
    time.sleep(timeout)


def show(shell, n=10000):
    output = shell.recv(n).decode('utf-8')
    return output


def close(ssh_client):
    if ssh_client.get_transport().is_active():
        print('Closing connection')
        ssh_client.close()


def get_name(router_ip):
    now = datetime.now()
    year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute
    file_name = f"{router_ip}_{year}-{month}-{day}-{hour}-{minute}.txt"
    return file_name


if __name__ == '__main__':
    password = getpass.getpass('Enter password:')
    router = {'server_ip': '10.1.1.10', 'server_port': '22', 'username': 'u1', 'password': password}
    client = connect(**router)
    # client = connect('10.1.1.10', 22, 'u1', 'cisco')
    shell = get_shell(client)

    send_shell_command(shell, 'enable')
    send_shell_command(shell, 'cisco')
    send_shell_command(shell, 'terminal length 0')
    send_shell_command(shell, 'sh version')

    output = show(shell)
    print(output)