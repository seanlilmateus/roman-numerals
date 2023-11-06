import unittest


class RomanNumeralsTest(unittest.TestCase):
    def test_arabic_1_converts_to_roman_I(self):
        actual = convert(1)
        self.assertEqual(actual, "I")


def convert(arabic):
    return "I"
