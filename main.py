import sys

from matplotlib import pyplot

from romanlengths.roman_lengths import calculate_length


def main():
    # TODO: Proper argument processing and error handling
    argument = sys.argv[1]
    if argument == 'plot':
        values = range(1, int(sys.argv[2]))
        pyplot.plot([x for x in values], [calculate_length(x) for x in values], 'ro')
        pyplot.plot([x for x in values], [len(str(x)) for x in values], linestyle='-')
        pyplot.show()
    else:
        print(calculate_length(int(argument)))


if __name__ == "__main__":
    main()
