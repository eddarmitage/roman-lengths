#!/usr/bin/env python3

from romanlengths.roman_conversion import convert_to_numeral


def calculate_length(decimal):
    return len(convert_to_numeral(decimal))
