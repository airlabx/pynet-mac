from netmiko import Netmiko
from getpass import getpass

# password = getpass()
# cisco1 = {
# 	'host': "10.10.1.200",
# 	'username':'admin',
# 	'password': password,
# 	'device_type': "cisco_ios"
# }

# cisco2 = {
# 	'host': "10.10.1.201",
# 	'username':'admin',
# 	'password': password,
# 	'device_type': "cisco_ios"
# }

# for device in(cisco1, cisco2):
# 	net_conn = Netmiko(**device)

# 	#print(net_conn.find_prompt())
# 	print("this is the {}".format(device['host']))
# 	output = net_conn.send_command("show arp")
# 	print(output)
# 	# output = net_conn.send_command("ip int br")
# 	# print(output)
# 	net_conn.disconnect()

# try:
#     host = raw_input("Enter host to connect to: ")
# except NameError:
#     host = input("Enter host to connect to: ")

# password = getpass()
device = {
    'host': "10.10.1.200",
    'username': 'admin',
    'password': 'p@ssw0rd',
    'device_type': 'cisco_ios',
}

filename = 'somefile'
command = 'delete flash0:{}'.format(filename)

net_connect = Netmiko(**device)
output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False)
if 'somefile' in output:
    # I don't confirm the file delete.
    output += net_connect.send_command_timing('n', strip_prompt=False, strip_command=False)
else:
    raise ValueError("Expected confirm message in output")

print()
print('-' * 80)
print(output)
print('-' * 80)
print()
