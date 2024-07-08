import myparamiko
from datetime import datetime

router = {'server_ip': '192.168.217.5', 'server_port': '22', 'username': 'wyx'}

# routers = [router1]

# Open connect
client = myparamiko.connect(**router)

# Open shell to send command
shell = myparamiko.get_shell(client)

myparamiko.send_shell_command(shell, 'enable')
myparamiko.send_shell_command(shell, 'terminal length 0')
myparamiko.send_shell_command(shell, 'sh users')
output = myparamiko.show(shell)
# remove the \n
output_list = output.splitlines()
my_output = "\n".join(output_list)
print(output_list)
# print(output)
now = datetime.now()
year, month, day, hour, minute = now.year, now.month, now.day, now.hour, now.minute
file_name = f"{router['server_ip']}_{year}-{month}-{day}-{hour}-{minute}.txt"
with open(file_name, 'w') as f:
    f.write(my_output)


myparamiko.close(client)