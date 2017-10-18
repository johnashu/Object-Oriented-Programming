import re

bin_display = """
#   0 :  0  :  0  :  0  :  0  :  0  : 0  :  0  = 0 (OFF)
#  128  64    32    16     8     4    2     1  = 1 (ON)
"""

hex_input = 'DB91132598CCBF76AE668B4B085176BB192775221FDBB50FCE1C3‌​927C‌​077EAF1E3DAC4C8A‌​8E‌​8028C3F7295EF8157C‌​‌​ED597A36EF1C3BFA4514‌​‌​77BFF32EEB1806C2CC‌​04‌​42585197A2BCD2C4‌​3921‌​47AADB93066D0B‌​A5AB6D‌​BFD3F6FCEB70‌​73AE61A5‌​D4AA8ABCBC‌​FF4EEBD1A1‌​655689BF‌​D7EAB82D77BF‌​7224F7‌​5FBCD323C9B9FA‌​9C0B‌​7D799180878A81D5‌​D0‌​7CF05BE39EEF989B2F‌​‌​C3077997D2C2F1162E5B‌​‌​47D99E4B415BC8CE5C‌​75‌​5476931BD8ED14B5‌​FCEC‌​1C8C654515946A‌​B7860B‌​BBEE7DCCFDAA‌​7AA410FF‌​65352B153B‌​58728D5781‌​4C610F82‌​5286D830C308‌​429BDC‌​F1167887B125EF‌​B2FA‌​34B3DEACD329F576‌​74‌​C071BEF6C9CEAC0C7F‌​‌​ABB587A1D6F8B4D0B53'

binary_string = hex_input.replace(' ', '')

h = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
     '8': '8', '9': '9', 'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}

b = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
     '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

match = re.match('^[_0-1]$', binary_string)
binary_lst = [128, 64, 32, 16, 8, 4, 2, 1]


def n():
    print("\n")


def nl():
    banner = '#' * 50
    print(banner)


nl()

def split_string(string, length):
    """ function to split a string into differnt lengths or chunks"""
    return [string[max(i - length, 0):i] for i in range(len(string), 0, - length)][::-1]


def hex2integer(hex_string_input):
    """ convert from hex string to integers"""
    hex1 = h[hex_string_input[0]]
    hex2 = h[hex_string_input[1]]

    return [str(hex1), str(hex2)]


def hex_int_to_dec(hex1, hex2):
    """ calculates a 2 digit hexadecimal to normal decimal """
    current_digit = int(hex1)
    current_digit1 = int(hex2)
    power = 1
    power1 = 0

    hex_iter = []

    if hex1:
        mul_dig = current_digit * (16 ** power)
        hex_iter.append(mul_dig)

    if hex2:
        mul_dig = current_digit1 * (16 ** power1)
        hex_iter.append(mul_dig)

    return sum(hex_iter)


def decimal2ascii(decimal_num):
    """ converts a decimal number to an ASCII character """
    return chr(decimal_num)


def run_the_show():
    hex_string = split_string(str(hex_input), 2)
    print(hex_string)

    hex_integers = [hex2integer(item) for item in hex_string]

    hex_full_dec = [hex_int_to_dec(item[0], item[1]) for item in hex_integers]

    ascii_msg = [decimal2ascii(item) for item in hex_full_dec]

    print(''.join(map(str, ascii_msg)))


run_the_show()
nl()
