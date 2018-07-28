#!/usr/bin/env python3


def convert_to_numeral(decimal):
    return __build_result(decimal, '')


def __build_result(remainder, output):
    if remainder < 0:
        raise Exception('Can\'t calculate a negative roman numeral!')

    if remainder == 0:
        return output

    if remainder >= 1000:
        return __build_result(remainder - 1000, output + 'M')
    elif remainder >= 900:
        return __build_result(remainder - 900, output + 'CM')
    elif remainder >= 500:
        return __build_result(remainder - 500, output + 'D')
    elif remainder >= 400:
        return __build_result(remainder - 400, output + 'CD')
    elif remainder >= 100:
        return __build_result(remainder - 100, output + 'C')
    elif remainder >= 90:
        return __build_result(remainder - 90, output + 'XC')
    elif remainder >= 50:
        return __build_result(remainder - 50, output + 'L')
    elif remainder >= 40:
        return __build_result(remainder - 40, output + 'XL')
    elif remainder >= 10:
        return __build_result(remainder - 10, output + 'X')
    elif remainder == 9:
        return __build_result(remainder - 9, output + 'IX')
    elif remainder >= 5:
        return __build_result(remainder - 5, output + 'V')
    elif remainder >= 4:
        return __build_result(remainder - 4, output + 'IV')
    else:
        return __build_result(remainder - 1, output + 'I')