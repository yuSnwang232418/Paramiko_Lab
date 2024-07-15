import myparamiko
from datetime import datetime
import threading


def my_work(router):
    # Open connect
    client = myparamiko.connect(**router)
    my_config_name = router['config']

    # Open shell to send command
    shell = myparamiko.get_shell(client)

    # myparamiko.send_shell_command(shell, 'enable')
    # myparamiko.send_shell_command(shell, 'terminal length 0')
    # # myparamiko.send_shell_command(shell, 'sh users')
    # myparamiko.send_shell_command(shell, 'show run')
    with open(my_config_name, 'r') as f:
        cur_config = f.read().splitlines()

    for cmd in cur_config:
        myparamiko.send_shell_command(shell, cmd)

    output = myparamiko.show(shell)
    # remove the \n
    output_list = output.splitlines()
    my_output = "\n".join(output_list)
    print(output_list)
    print(my_output)

    # Output to file
    file_name = myparamiko.get_name(router['server_ip'])
    with open(file_name, 'w') as f:
        f.write(my_output)


    # close the ssh connection
    myparamiko.close(client)


router1 = {'server_ip': '192.168.217.5', 'server_port': '22', 'username': 'wyx', 'config': 'R1.txt'}
router2 = {'server_ip': '192.168.217.6', 'server_port': '22', 'username': 'wyx', 'config': 'R2.txt'}
router3 = {'server_ip': '192.168.217.7', 'server_port': '22', 'username': 'wyx', 'config': 'R3.txt'}
routers = [router1, router2, router3]
# for router in routers:
#     my_work(router)

threads = list()
for router in routers:
    th = threading.Thread(target=my_work, args=(router,))
    threads.append(th)

for th in threads:
    th.start()

# wait for each thread to finish
for th in threads:
    th.join()