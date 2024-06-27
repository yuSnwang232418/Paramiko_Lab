import time
import paramiko
import getpass

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# password = getpass.getpass('Enter password:')
# ssh_client.connect(hostname='10.1.1.10', port=22, username='u1', password='cisco',
#                    look_for_keys=False, allow_agent=False)

router = {'hostname': '192.168.229.20', 'port': '22', 'username': 'wyx', 'password': 'wyx'}
print(f"Connecting to router {router['hostname']}")
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)
print(ssh_client.get_transport().is_active())

shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send("show version\n")
time.sleep(1)

output = shell.recv(10000)
output = output.decode('utf-8')
print(output)
#
shell.send('enable\n')
shell.send('232418\n')
# shell.send('conf t\n')
# shell.send('router ospf 1\n')
# shell.send('net 0.0.0.0 0.0.0.0 area 1\n')
# shell.send('end\n')
shell.send('terminal length 0\n')
shell.send('sh ip route\n')
time.sleep(2)
output = shell.recv(10000).decode('utf-8')
print(output)

if ssh_client.get_transport().is_active():
    print('Closing connection')
    ssh_client.close()