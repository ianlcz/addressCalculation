from numconverter import *


def rewrite_netmask(CIDR):
    '''
    This function allows to rewrite CIDR Netmask.
    '''
    list_origin_binary_Netmask = []
    for element in range(int(CIDR)):
        list_origin_binary_Netmask.append('1')
    for element in range(32 - int(CIDR)):
        list_origin_binary_Netmask.append('0')
    list_binary_Netmask = []
    counter = 0
    for index in range(len(list_origin_binary_Netmask)):
        list_binary_Netmask.append(list_origin_binary_Netmask[index])
        counter += 1
        if counter == 8 and index != 31:
            list_binary_Netmask.append('.')
            counter = 0
    return ''.join(list_binary_Netmask), convert_binary_to_decimal(
        ''.join(list_binary_Netmask))


def determine_networkAddress(ip, Netmask):
    '''
    This function determines the network address from the IPv4 and Netmask address.
    '''
    list_networkAddress = []
    for index in range(len(ip.split('.'))):
        list_networkAddress.append(str(binary_to_decimal(decimal_to_binary(
            int(ip.split('.')[index]) & int(Netmask.split('.')[index]), 8))))
    return convert_decimal_to_binary(
        '.'.join(list_networkAddress)), '.'.join(list_networkAddress)


def determine_broadcastAddress(binary_ip, binary_Netmask):
    '''
    This function determines the broadcast address.
    '''
    binary_broadcastAddress = []
    for index in range(len(binary_Netmask)):
        if binary_Netmask[index] == '1' or binary_Netmask[index] == '.':
            binary_broadcastAddress.append(binary_ip[index])
        else:
            binary_broadcastAddress.append('1')
    return ''.join(binary_broadcastAddress), convert_binary_to_decimal(
        ''.join(binary_broadcastAddress))


def determine_address_range(address, isBroadcast=False):
    '''
    This function determines the address range.
    '''
    address = address.split('.')
    last = address.pop(-1)
    copyAddress = address
    if isBroadcast:
        copyAddress.append(str(int(last) - 1))
    else:
        copyAddress.append(str(int(last) + 1))
    return ('.'.join(copyAddress))
