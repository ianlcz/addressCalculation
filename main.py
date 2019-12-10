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

# Rewriting of the Subnet mask
abr_subnetMask = 24
list_origin_binary_subnetMask = []
for element in range(abr_subnetMask):
    list_origin_binary_subnetMask.append('1')
for element in range(32 - abr_subnetMask):
    list_origin_binary_subnetMask.append('0')
list_binary_subnetMask = []
counter = 0
for index in range(len(list_origin_binary_subnetMask)):
    list_binary_subnetMask.append(list_origin_binary_subnetMask[index])
    counter += 1
    if counter == 8 and index != 31:
        list_binary_subnetMask.append('.')
        counter = 0
binary_subnetMask=''.join(list_binary_subnetMask)
subnetMask=convert_binary_to_decimal(binary_subnetMask)

# Calculation of the Network address
list_networkAddress = []
for index in range(len(ip.split('.'))):
    list_networkAddress.append(str(binary_to_decimal(decimal_to_binary(int(ip.split('.')[index]) & int(subnetMask.split('.')[index]), 8))))
networkAddress = '.'.join(list_networkAddress)
binary_networkAddress = convert_decimal_to_binary(networkAddress)

# Calculation of the Broadcast address
binary_broadcastAddress = []
for index in range(len(binary_subnetMask)):
    if binary_subnetMask[index] == '1' or binary_subnetMask[index] == '.':
        binary_broadcastAddress.append(binary_ip[index])
    else:
        binary_broadcastAddress.append('1')
binary_broadcastAddress = ''.join(binary_broadcastAddress)
broadcastAddress = convert_binary_to_decimal(binary_broadcastAddress)

#print(f"DÉCIMAL\t\tBINAIRE\n{ip}\t{binary_ip}\n{subnetMask}\t{binary_subnetMask}\n{networkAddress}\t{binary_networkAddress}\n{broadcastAddress}\t{binary_broadcastAddress}")
print(f"Adresse IP\t\t{ip}\nMasque de sous-réseaux\t{subnetMask}\nAdresse du réseau\t{networkAddress}\nAdresse de broadcast\t{broadcastAddress}")