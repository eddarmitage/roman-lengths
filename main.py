import sys

from romanlengths.roman_lengths import calculate_length


def main():
    # TODO: Proper argument processing and error handling
    decimal = int(sys.argv[1])
    print(calculate_length(decimal))


if __name__ == "__main__":
    main()
