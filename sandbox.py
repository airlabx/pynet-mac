# import random
# def randomNetwork(network_var='10.10.10.'):
#     octet = random.randint(1, 254)
#     print(network_var + str(octet))

# randomNetwork(network_var='1.1.1.1.')

import pdb

def normalize(mac_addr, case='u'):
  
    if mac_addr[4:5] == '.':
        mac_addr = mac_addr.split('.')
    elif mac_addr[2:3] == '-':
        mac_addr = mac_addr.split('-')
    elif mac_addr[1:2] and mac_addr[3:4] == ':':
        mac_addr = mac_addr.split(':')

        # aces = ["a" + suit for suit in suits]
        ## https://stackoverflow.com/questions/15738267/add-a-character-to-each-item-in-a-list
        mac_addr = ["0" + mac_addr for mac_addr in mac_addr]
        # for char in mac_addr:
        #     #need to select the firt on the list char[1] or mac_addr[char]
        #     mac_addr.append(str(0) + char)
        pdb.set_trace()   


    
    mac_addr = "".join(mac_addr)

    # check and see if the user wants upercase or lower case - default is upper
    if case == 'u':
        mac_addr = mac_addr.upper()
    elif case == 'l':
        mac_addr = mac_addr.lower()
    # Process two hex digits at a time
    new_mac = []
    while len(mac_addr) > 0:
        entry = mac_addr[:2]
        mac_addr = mac_addr[2:]
        new_mac.append(entry)

    # Reunite MAC address using a colon
    new_mac = ":".join(new_mac)
    return new_mac

mac = normalize('a:b:c:d:e:f')
print(mac)
mac = normalize('00-00-aa-li-ne-s1')
print(mac)
mac = normalize('0000.AAAA.noth')
print(mac)
mac = normalize('0000.AAAA.BBBB', 'l')
print(mac)
mac = normalize('0000.aaaa.bbbb', 'u')
print(mac)