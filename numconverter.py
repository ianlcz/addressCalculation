import string


def decimal_to_binary(number, length=4):
    '''
    Converts a decimal number into a binary number.
    >>> decimal_to_binary(1996)
    '11111001100'
    '''
    result = ''

    while number != 0:
        result += str(number % 2)
        number //= 2

    while len(result) < length:
        result += '0'

    return result[::-1]


def decimal_to_hexadecimal(number):
    '''
    Converts a decimal number to a hexadecimal number.
    >>> decimal_to_hexadecimal(1996)
    '7CC'
    '''
    result = ''

    if number != 0:
        while number != 0:
            if number % 16 >= 10 and number % 16 <= 15:
                result += string.ascii_uppercase[(number % 16) - 10]
            else:
                result += str(number % 16)
            number //= 16
        return result[::-1]
    else:
        return '0'


def binary_to_decimal(number):
    '''
    Converts a binary number to a decimal number.
    >>> binary_to_decimal('11111001100')
    1996
    '''
    result = 0

    for weight, bit in enumerate(number[::-1]):
        result += int(bit) * pow(2, weight)

    return result


def binary_to_hexadecimal(number):
    '''
    Converts a binary number to a hexadecimal number.
    >>> binary_to_hexadecimal('11111001100')
    '7CC'
    '''
    return decimal_to_hexadecimal(binary_to_decimal(number))


def hexadecimal_to_decimal(number):
    '''
    Converts a hexadecimal number to a decimal number.
    >>> hexadecimal_to_decimal('7CC')
    1996
    '''
    result = 0

    for weight, bit in enumerate(number[::-1]):
        if bit not in string.digits:
            for counter, letter in enumerate(string.ascii_uppercase):
                if letter == str(bit).upper():
                    bit = counter + 10
        result += int(bit) * pow(16, weight)

    return result


def hexadecimal_to_binary(number):
    '''
    Converts a hexadecimal number to a binary number.
    >>> hexadecimal_to_binary('7CC')
    '11111001100'
    '''
    return decimal_to_binary(hexadecimal_to_decimal(number))


def convert_decimal_to_binary(string):
    '''
    Converts each decimal numbers in a string into binary.
    >>> convert_decimal_to_binary('192.168.0.45')
    '11000000.10101000.00000000.00101101'
    '''
    binary_string = []
    for element in string.split('.'):
        binary_string.append(decimal_to_binary(int(element), 8))
    return '.'.join(binary_string)


def convert_binary_to_decimal(string):
    '''
    Converts each binary numbers in a string into decimal.
    >>> convert_binary_to_decimal('11000000.10101000.00000000.00101101')
    '192.168.0.45'
    '''
    decimal_string = []
    for element in string.split('.'):
        decimal_string.append(str(binary_to_decimal(element)))
    return '.'.join(decimal_string)
