#Testcase
import unittest

from conversion_functions import *

class TestHelper(unittest.TestCase):

    test_number = NumberConverter("18009493582")

    # Test that strip_number() can remove all non alphanumeric characters
    def test_strip_num(self):
        data = "_&^12#@!()34ab$*:\"\\,./?fe"
        result = self.test_number.strip_number(data)
        self.assertEqual(result,"1234abfe")


    # Test that strip_number() works for empty string
    def test_strip_empty(self):
        data = ""
        result = self.test_number.strip_number(data)
        self.assertEqual(result,"")


    # Test that strip_number() works for non strings
    def test_strip_int(self):
        data = 4585
        result = self.test_number.strip_number(data)
        self.assertEqual(result,"4585")


    # Test that valid_word() works for non strings
    def test_valid_int(self):
        data = 45859451
        result = self.test_number.valid_word(data)
        self.assertEqual(result,"")


    # Test that valid_word() can remove all non alphabets &
    # test for finding mixed case words - 'HeLlO'
    def test_valid_characters(self):
        data = "_&^12#@!()34ab$*:\"HeLlO\\,./?fe"
        result = self.test_number.valid_word(data)
        self.assertEqual(result.lower(),"hello")


    # Test that valid_word() returns first word in multi-word input
    def test_valid_multiple(self):
        data = "12ringing-bells"
        result = self.test_number.valid_word(data)
        self.assertEqual(result.lower(),"ringing")


    # Test that phone_format() works well with '-' character
    def test_format_pattern(self):
        data = "12ringing-bells"
        result = self.test_number.phone_format(data)
        self.assertEqual(result.lower(),"12-ringing-bells")


    # Test that phone_format() doesnt split callocated words
    def test_format_split(self):
        data = "RaceCar12"
        result = self.test_number.phone_format(data)
        self.assertEqual(result.lower(),"ra-cec-ar12")


    # Test that phone_format() returns pattern for unusual number formats
    def test_format_number(self):
        data = "1800-8-8.5  4    2-895/47"
        result = self.test_number.phone_format(data)
        self.assertEqual(result.lower(),"1-800-885-428-9547")








if __name__ == 'main':
    unittest.main()
