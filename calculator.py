import math


def dec_in_bin(number: int):
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

