from numconverter import *

def convert_decimal_to_binary(string):
    binary_string = []
    for element in string.split('.'):
        binary_string.append(decimal_to_binary(int(element), 8))
    return '.'.join(binary_string)

def convert_binary_to_decimal(string):
    decimal_string = []
    for element in string.split('.'):
        decimal_string.append(str(binary_to_decimal(element)))
    return '.'.join(decimal_string)

ip = "192.168.0.1"
binary_ip = convert_decimal_to_binary(ip)

# Rewriting of the Netmask
abr_Netmask = 24
list_origin_binary_Netmask = []
for element in range(abr_Netmask):
    list_origin_binary_Netmask.append('1')
for element in range(32 - abr_Netmask):
    list_origin_binary_Netmask.append('0')
list_binary_Netmask = []
counter = 0
for index in range(len(list_origin_binary_Netmask)):
    list_binary_Netmask.append(list_origin_binary_Netmask[index])
    counter += 1
    if counter == 8 and index != 31:
        list_binary_Netmask.append('.')
        counter = 0
binary_Netmask=''.join(list_binary_Netmask)
Netmask=convert_binary_to_decimal(binary_Netmask)

# Calculation of the Network address
list_networkAddress = []
for index in range(len(ip.split('.'))):
    list_networkAddress.append(str(binary_to_decimal(decimal_to_binary(int(ip.split('.')[index]) & int(Netmask.split('.')[index]), 8))))
networkAddress = '.'.join(list_networkAddress)
binary_networkAddress = convert_decimal_to_binary(networkAddress)

# Calculation of the Broadcast address
binary_broadcastAddress = []
for index in range(len(binary_Netmask)):
    if binary_Netmask[index] == '1' or binary_Netmask[index] == '.':
        binary_broadcastAddress.append(binary_ip[index])
    else:
        binary_broadcastAddress.append('1')
binary_broadcastAddress = ''.join(binary_broadcastAddress)
broadcastAddress = convert_binary_to_decimal(binary_broadcastAddress)

# Definition of the number of usable addresses
binary_usableAddresses = []
for element in binary_Netmask:
    if element == '0':
        binary_usableAddresses.append(element)
numberOfUsableAddresses = int(convert_binary_to_decimal(''.join(binary_usableAddresses).replace('0', '1'))) - 1

# Definition of the address range
minimalAddress = networkAddress[:-1] + str(int(networkAddress.split('.')[-1]) + 1)
maximalAddress = broadcastAddress[:-3] + str(int(broadcastAddress.split('.')[-1]) - 1)
addressRange = minimalAddress + " - " + maximalAddress

print(f"Adresse IP\t\t\t{ip}\nMasque de sous-réseaux\t\t{Netmask}\nAdresse du réseau\t\t{networkAddress}\nAdresse de broadcast\t\t{broadcastAddress}\nNombre d'adresses utilisables\t{numberOfUsableAddresses}\nPlage d'adresses\t\t{addressRange}")