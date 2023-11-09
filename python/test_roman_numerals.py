import unittest
from functools import reduce

ROMANS = {
	1000: "M",
    900:"CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}

class RomanNumeralsTest(unittest.TestCase):
    def test_arabic_converts_into_roman_I2VII(self):
        for roman, arabic in  [("I", 1), ("VI", 6), ("VII", 7), ("XX", 20)]:
            actual = convert(arabic)
            self.assertEqual(actual, roman)


def convert(arabic):
    return ROMANS.get(arabic, compose_roman2(arabic))


def compose_roman(num):
    return 'VI'

def compose_roman2(num):
    roman_numerals = ''
    for value in sorted(ROMANS.keys(), reverse=True):
        while num >= value:
            roman_numerals += ROMANS[value]
            num -= value
    return roman_numerals