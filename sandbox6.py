from netmiko import Netmiko
from getpass import getpass

net_conn = Netmiko(host='xxx.xxx.xxx.xxx', username='admin', password=getpass(), device_type='cisco_ios')

print(net_conn.find_prompt())