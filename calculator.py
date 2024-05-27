import math


def dec_in_bin(number: int) -> str:
    """Преобразует десятичное число в двоичное"""
    remain_number = number
    binary_number = ''
    max_power = int(math.floor(math.log(number, 2)))
    for i in range(max_power, -1, -1):
        if remain_number - (2 ** i) >= 0:
            binary_number += '1'
            remain_number -= (2 ** i)
            bit = 1
        else:
            binary_number += '0'
            bit = 0
        print("{pow} степень - {bit} {dec}".format(pow=i, bit=bit, dec=2**i*bit))
    print("{} в двоичном виде: {}, длина {}".format(number, binary_number, len(binary_number)))
    return binary_number


def bin_in_dec(bin_number: str) -> int:
    """Преобразует двоичное число в десятичное"""
    dec_number = 0
    res = ''
    resDecimal = ''
    for i in range(len(bin_number)):
        if bin_number[i] == '1':
            dec_number += 2 ** (len(bin_number) - i - 1)
            res += '2^{}+'.format(len(bin_number) - i - 1)
            resDecimal += '{}+'.format(2**(len(bin_number) - i - 1))
    print('{} = {} = {}'.format(res[0:-1], resDecimal[0:-1], dec_number))
    return dec_number


class Mask:
    def __init__(self, mask: str):
        self.octets = mask.split('.')
        self.mask = mask
        print(self.octets, self.mask)

    def __str__(self):
        return self.mask


class IPv4:
    def __init__(self, iPv4_address: str, mask: str):
        self.octets = iPv4_address.split('.')
        self.address = iPv4_address
        self.mask = Mask(mask)
        print(self.octets, self.address)

    def __str__(self):
        return '{}::{}'.format(self.address, self.mask)




ip = IPv4('192.168.16.1', '255.255.255.0')