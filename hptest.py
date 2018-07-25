from netmiko import Netmiko
from getpass import getpass

password = getpass()

device = {
    'host': "192.168.10.182",
    'username': 'manager',
    'password': password,
    'device_type': 'hp_procurve',
}
net_connect = Netmiko(**device)

print(net_connect)
# result = net_connect.find_prompt()
result = net_connect.send_command('show version')

# result += net_connect.send_command('show version')
print(result)
net_connect.disconnect()