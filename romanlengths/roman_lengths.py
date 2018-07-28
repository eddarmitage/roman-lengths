#!/usr/bin/env python3
import sys

from romanlengths.roman_conversion import convert_to_numeral


def calculate_length(decimal):
    return len(convert_to_numeral(decimal))


def main():
    # TODO: Proper argument processing and error handling
    decimal = int(sys.argv[1])
    print(calculate_length(decimal))


if __name__ == "__main__":
    main()