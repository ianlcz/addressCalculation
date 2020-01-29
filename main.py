import sys
from addresscalculation import *


def verify_string(address, minimun, maximum, minimum_length, maximum_length):
    if not address or len(address) < minimum_length or len(
            address) > maximum_length:
        return True
    for element in address:
        if element not in string.digits + '.':
            return True
    for element in address.split('.'):
        if int(element) < minimun or int(element) > maximum:
            return True


ip = input("> Entrez une adresse IPv4: ")
while verify_string(ip, 0, 255, 7, 15):
    ip = input("> ")
binary_ip = convert_decimal_to_binary(ip)

# Rewriting of the CIDR netmask into decimal address
CIDR = input("> Entrez le masque de sous-réseaux (CIDR): /")
while verify_string(CIDR, 0, 32, 1, 2):
    CIDR = input("> /")
binary_Netmask, Netmask = rewrite_netmask(CIDR)

# Call of the function determine_networkAddress()
binary_networkAddress, networkAddress = determine_networkAddress(ip, Netmask)

# Call of the function determine_broadcastAddress()
binary_broadcastAddress, broadcastAddress = determine_broadcastAddress(
    binary_ip, binary_Netmask)

# Calculation of the number of usable addresses
numberOfUsableAddresses = pow(2, 32 - int(CIDR)) - 2

# Definition of the address range
addressRange = determine_address_range(
    networkAddress) + " - " + determine_address_range(broadcastAddress, True)

if CIDR == '32':
    print(
        f"\nAdresse IP\t\t\t\t\t{ip}\nMasque de sous-réseaux\t\t\t\t{Netmask} (/{CIDR})")
elif CIDR == '31':
    print(
        f"\nPlage d'adresses\t\t\t\t{networkAddress} - {broadcastAddress}\nMasque de sous-réseaux\t\t\t\t{Netmask} (/{CIDR})")
else:
    print(f"\nAdresse IP\t\t\t\t\t{ip}\nMasque de sous-réseaux\t\t\t\t{Netmask} (/{CIDR})\nAdresse du réseau\t\t\t\t{networkAddress}\nAdresse de broadcast\t\t\t\t{broadcastAddress}\nNombre d'adresses utilisables\t\t\t{numberOfUsableAddresses}\nPlage d'adresses utilisables\t\t\t{addressRange}")

ChoiceOfContinue = input(
    "\nVoulez-vous effectuer des calculs de sous-réseaux ? [O/N]\n> ")
while ChoiceOfContinue.upper() != 'O' and ChoiceOfContinue.upper() != 'N':
    ChoiceOfContinue = input('> ')
if ChoiceOfContinue.upper() == 'O':
    ChoiceOfOption = input("Voulez-vous savoir le nombre de sous-réseaux que vous pouvez mettre dans ce réseau ? [O/N]\n> ")
    while ChoiceOfOption.upper() != 'O' and ChoiceOfOption.upper() != 'N':
        ChoiceOfOption = input('> ')
    if ChoiceOfOption.upper() == 'O':
        new_CIDR = input("> Entrez le nouveau masque de sous-réseaux: /")
        while verify_string(new_CIDR, 0, 32, 1, 2) or int(new_CIDR) <= int(CIDR):
            new_CIDR = input("> /")
        numberSubnet = pow(2, int(new_CIDR) - int(CIDR))
        print(f"\nNombre de sous-réseaux dans {networkAddress}/{CIDR}\t{numberSubnet}")
    else:
        index = 0
        numberSubnet = input("> Entrez le nombre de sous-réseaux que vous souhaitez dans votre réseau: ")
        while not numberSubnet or not numberSubnet.isdigit():
            numberSubnet = input("> ")
        # Determination of the new CIDR
        while int(numberSubnet) >= pow(2, index):
            index += 1
        new_CIDR = int(CIDR) + index
        # Rewriting of the new CIDR netmask into decimal address
        binary_new_Netmask, new_Netmask = rewrite_netmask(new_CIDR)
        print(f"\nMasque de sous-réseaux\t\t\t\t{new_Netmask} (/{new_CIDR})\nNombre de sous-réseaux disponibles\t\t{pow(2, index)} (+{str(pow(2, index) - int(numberSubnet))})")
else:
    # Exit of the program
    sys.exit