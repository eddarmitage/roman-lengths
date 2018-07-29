Roman Lengths
=============

A simple tool for looking at the lengths of numbers when represented as roman numerals.

Can be run as follows:

    ➜ pip install -r requirements.txt
    ➜ python main.py 2302 
    7
    ➜

Graphs can produced using the following (for all values up to 527):

    ➜ pip install -r requirements.txt
    ➜ python main.py plot 527

Tests can be run as follows:

    ➜ pip install -r requirements.txt
    ➜ pytest

Because of [complicated reasons](https://matplotlib.org/faq/osx_framework.html), macOS
users may find it simplest to ensure they have a `~/.matplotlib/matplotlibrc` file
containing the following line:

    backend: TkAgg
