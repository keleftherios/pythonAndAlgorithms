"""
Functions to convert Between Different Bases
"""

def convert_to_decimal(number, base):
    """
    Function below converts a number in any base,
    smaller than 10 to the decimal base.
    """
    reverted_num_str, result = str(number)[::-1], 0
    for i in range(len(reverted_num_str)):
        if reverted_num_str[i] != "0":
            result += (base**i) * int(reverted_num_str[i])
    return result

def convert_from_decimal(number, base):
    """
    Function that converts from a decimal number,
    to another number (2 <= base <= 10)
    """
    remainder = ''
    while number > 0:
        remainder = str(number % base) + remainder
        number //= base
    return int(remainder)


########################################################################################################################

def convert_to_decimal_v2(number, base):
    """
    Book solution
    """
    multiplier, result = 1, 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number = number // 10
    return result

def convert_from_decimal_v2(number, base):
    """
    Book solution
    """
    multiplier, result = 1, 0
    while number > 0:
        result += number % base * multiplier
        multiplier *= 10
        number //= base
    return result

########################################################################################################################

def convert_from_decimal_to_larger_bases(number, base):
    """
    Convert an integer to a string in any base
    """
    strings, result = '0123456789ABCDEF', ''
    while number > 0:
        digit = number % base
        result = strings[digit] + result
        number //= base
    return result

def convert_dec_to_any_base(number, base):
    """
    Convert an integer to a string in any base
    """
    convertString = '0123456789ABCDEF'
    if number < base:
        return convertString[number]
    else:
        return convert_dec_to_any_base(number // base, base) + convertString[number % base]



if __name__ == "__main__":

    R1 = convert_to_decimal(1101, 2)
    print(R1)
    assert R1 == 13, "Wrong result..."

    R2 = convert_to_decimal(1001, 2)
    print(R2)
    assert R2 == 9, "Wrong result..."

    R3 = convert_to_decimal(107, 8)
    print(R3)
    assert R3 == 71, "Wrong result...."

    R4 = convert_from_decimal(9, 2)
    print(R4)
    assert R4 == 1001, "Wrong result..."

    R5 = convert_from_decimal(13, 2)
    print(R5)
    assert R5 == 1101, "Wrong result..."

    R6 = convert_from_decimal(71, 8)
    print(R6)
    assert R6 == 107, "Wrong result..."

    R7 = convert_from_decimal_to_larger_bases(31, 16)
    print(R7)
    assert R7 == '1F', "Wrong result..."

    R8 = convert_dec_to_any_base(9, 2)
    print(R8)
    assert R8 == '1001', "Wrong result..."
