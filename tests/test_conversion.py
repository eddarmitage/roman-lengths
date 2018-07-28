#!/usr/bin/env python3
import pytest
import yaml

from romanlengths.roman_conversion import convert_to_numeral

numerals = yaml.load(open("tests/roman-numerals.yml", 'r'))


@pytest.mark.parametrize('value', range(1, 4999))
def test_conversion(value):
    assert convert_to_numeral(value) == numerals[value]
