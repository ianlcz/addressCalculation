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

ip = "172.128.10.5"
binary_ip = convert_decimal_to_binary(ip)

# Rewriting of the Subnet mask
abr_subnetMask = 18
list_binary_subnetMask = []
for element in range(abr_subnetMask):
    list_binary_subnetMask.append('1')
for element in range(32 - abr_subnetMask):
    list_binary_subnetMask.append('0')
for index in range(len(list_binary_subnetMask)):
    if index != 0 and index % 8 == 0:
        list_binary_subnetMask.pop(index)
        if index != 24:
            list_binary_subnetMask.insert(index,'.1')
        else:
            list_binary_subnetMask.insert(index,'.')
binary_subnetMask = ''.join(list_binary_subnetMask)
subnetMask = convert_binary_to_decimal(binary_subnetMask)

# Calculation of the Network address
list_networkAddress = []
for index in range(len(ip.split('.'))):
    list_networkAddress.append(str(binary_to_decimal(decimal_to_binary(int(ip.split('.')[index]) & int(subnetMask.split('.')[index]), 8))))
networkAddress = '.'.join(list_networkAddress)
binary_networkAddress = convert_decimal_to_binary(networkAddress)

#print(f"DÉCIMAL\t\tBINAIRE\n{ip}\t{binary_ip}\n{subnetMask}\t{binary_subnetMask}\n{networkAddress}\t{binary_networkAddress}")
print(f"Adresse IP\t\t{ip}\nMasque de sous-réseaux\t{subnetMask}\nAdresse de réseau\t{networkAddress}")