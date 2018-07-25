from netmiko import Netmiko
from getpass import getpass

password = getpass()
cisco1 = {
	'host': "10.10.1.200",
	'username':'admin',
	'password': password,
	'device_type': "cisco_ios"
}

cisco2 = {
	'host': "10.10.1.201",
	'username':'admin',
	'password': password,
	'device_type': "cisco_ios"
}

for device in(cisco1, cisco2):
	net_conn = Netmiko(**device)

	#print(net_conn.find_prompt())
	print("this is the {}".format(host))
	output = net_conn.send_command("show arp")
	print(output)
	output = net_conn.send_command("ip int br")
	print(output)
net_conn.disconnect
