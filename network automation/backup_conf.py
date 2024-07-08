import myparamiko
import getpass
from datetime import datetime
import threading


def backup(router):
    client = myparamiko.connect(**router)
    shell = myparamiko.get_shell(client)

    myparamiko.send_shell_command(shell, 'enable')
    myparamiko.send_shell_command(shell, '232418')
    myparamiko.send_shell_command(shell, 'terminal length 0')
    myparamiko.send_shell_command(shell, 'sh run')

    output = myparamiko.show(shell)
    print(output)
    # only keep the useful information
    output_list = output.splitlines()
    output_list = output_list[11:-1]
    my_output = "\n".join(output_list)

    now = datetime.now()
    year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute
    file_name = f"{router['server_ip']}_{year}-{month}-{day}-{hour}-{minute}.txt"
    with open(file_name, 'w') as f:
        f.write(my_output)

    myparamiko.close(client)


# password = getpass.getpass('Enter password:')
router1 = {'server_ip': '192.168.229.20', 'server_port': '22', 'username': 'wyx', 'password': 'wyx'}
# router2 = {'server_ip': '10.1.1.20', 'server_port': '22', 'username': 'u1', 'password': 'password'}
# router3 = {'server_ip': '10.1.1.30', 'server_port': '22', 'username': 'u1', 'password': 'password'}
routers = [router1]
threads = list()
for router in routers:
    th = threading.Thread(target=backup, args=(router,))
    threads.append(th)

for th in threads:
    th.start()

# wait for each thread to finish
for th in threads:
    th.join()

