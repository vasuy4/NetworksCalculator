import math
import time
from typing import List


def dec_in_bin(number: int) -> str:
    """Преобразует десятичное число в двоичное"""
    if number == 0:
        # print("0 в двоичном виде 0")
        return "0"
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
        # print("{pow} степень - {bit} {dec}".format(pow=i, bit=bit, dec=2**i*bit))
    # print("{} в двоичном виде: {}, длина {}".format(number, binary_number, len(binary_number)))
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
    # print('{} = {} = {}'.format(res[0:-1], resDecimal[0:-1], dec_number))
    return dec_number


def ip_address_bin_in_dec(ip_address: str) -> str:
    """Преобразует целый двоичный ip-адрес в десятичное число"""
    decIp = ''
    octetsList = ip_address.split('.')
    for octet in octetsList:
        decOctet = bin_in_dec(octet)
        decIp += str(decOctet) + "."
    return decIp[0:-1]


def ip_address_dec_in_bin(ip_address: str) -> str:
    """Преобразует десятичный ip-адрес в двоичный"""
    binIp = ''
    octetsList = ip_address.split('.')
    for octet in octetsList:
        binOctet = dec_in_bin(int(octet))
        binIp += binOctet + "."
    return binIp[0:-1]


class AddressNetwork:
    def __init__(self, fourHexadecimal: str):
        self.fourHexadecimal = fourHexadecimal
        self.octets = list(map(int, fourHexadecimal.split('.')))
        self.bin_octets = self.calc_bin_octets()

    def fillingZeros(self, octets: List[str]) -> List[str]:
        i_octet = 0
        for octet in octets:
            while len(octet)<8:
                octet = "0" + octet
            octets[i_octet] = octet
            i_octet += 1
        return octets

    def calc_bin_octets(self) -> List[str]:
        bin_octets = []
        for octet in self.octets:
            bin_octet = dec_in_bin(octet)
            if bin_octet == "0":
                bin_octet *= 8
            bin_octets.append(bin_octet)
        return bin_octets

    def __and__(self, other) -> str:
        if isinstance(other, AddressNetwork):
            new_octets = ''
            for i in range(4):
                octet1 = self.bin_octets[i]
                octet2 = other.bin_octets[i]
                new_octet = ''
                for j in range(len(octet1)):
                    if octet1[j] == '1' and octet2[j] == '1':
                        new_octet += "1"
                    else:
                        new_octet += '0'
                new_octets += new_octet + "."
            return new_octets[0:-1]
        else:
            print("Нельзя это складывать!")


class Mask(AddressNetwork):
    def __init__(self, mask: str):
        super().__init__(mask)

        self.octets = list(map(int, mask.split('.')))
        self.bin_octets = self.fillingZeros(self.calc_bin_octets())

        self.mask = mask
        self.bin_mask = "{}.{}.{}.{}".format(self.bin_octets[0], self.bin_octets[1], self.bin_octets[2], self.bin_octets[3])
        self.prefix = self.calc_prefix()
        self.prefix_int = int(self.prefix[1:])

    def calc_prefix(self) -> str:
        summ_bit = 0
        for i_bit in self.bin_mask:
            if i_bit == "1":
                summ_bit += 1
        return "/{}".format(summ_bit)

    def __str__(self):
        return self.mask


class IPv4(AddressNetwork):
    def __init__(self, iPv4_address: str, mask: str):
        super().__init__(iPv4_address)

        self.octets = list(map(int, iPv4_address.split('.')))
        self.bin_octets = self.fillingZeros(self.calc_bin_octets())

        self.ipv4_address = iPv4_address
        self.bin_ipv4_address = "{}.{}.{}.{}".format(self.bin_octets[0], self.bin_octets[1], self.bin_octets[2],
                                             self.bin_octets[3])
        self.mask = Mask(mask)

        self.num_addresses_subnet = 2**(32-self.mask.prefix_int)
        self.num_nodes_subnet = self.num_addresses_subnet - 2

        self.binIPv4Subnet = self&self.mask
        self.ipv4Subnet = ip_address_bin_in_dec(self.binIPv4Subnet)

    def print_all_info(self):
        all_info = self.list_all_info()
        for info in all_info:
            print(info)

    def list_all_info(self):
        all_info = ["IPv4 адрес - {}, {}".format(self.ipv4_address, self.bin_ipv4_address),
                    "Маска подсети - {}, {}".format(self.mask, self.mask.bin_mask),
                    "Префикс маски - {}".format(self.mask.prefix),
                    "Число адресов в подсети - {}".format(self.num_addresses_subnet),
                    "Число узлов в подсети - {}".format(self.num_nodes_subnet),
                    "IPv4 адрес подсети - {}, {}".format(self.ipv4Subnet, self.bin_ipv4_address),]
        return all_info

    def __str__(self):
        return '{}::{}'.format(self.ipv4_address, self.mask)


def calculate_for_ui(ipv4, mask):
    ip = IPv4(ipv4, mask)
    ip.print_all_info()
    return ip.list_all_info()


if __name__ == "__main__":
    ip = IPv4('192.168.209.1', '255.255.128.0')
    ip.print_all_info()