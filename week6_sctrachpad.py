from netmiko import Netmiko
from getpass import getpass

net_conn = Netmiko(host='10.10.1.200', username=username, password=getpass(), device_type= device_type)

print(net_conn.find_prompt())