#Testcase
import unittest

from conversion_functions import *
from util import *

class TestHelperFunctions(unittest.TestCase):

    test_number = Number("18009493582")

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


    # Test that phone_format() works with empty input
    def test_format_empty(self):
        data = ""
        result = self.test_number.phone_format(data)
        self.assertEqual(result.lower(),"")


    # Test that phone_format() returns pattern for unusual number formats
    def test_format_number(self):
        data = "1800-8-8.5  4    2-895/47"
        result = self.test_number.phone_format(data)
        self.assertEqual(result.lower(),"1-800-885-428-9547")


class TestMainFunctions(unittest.TestCase):

    test_number = NumberConverter("18009456741")


    # Test that words_to_number() returns correct pattern removing non alphanumeric characters
    def test_words2num(self):
        self.test_number.num.phone_number = "18#!0\ 0\"-P8y*th(on)"
        result = self.test_number.words_to_number()
        self.assertEqual(result,"1-800-789-8466")


    # Test checks if words_to_number() works with pure digit input
    def test_words2num_digits(self):
        self.test_number.set_number("1800-0015-424")
        result = self.test_number.words_to_number()
        self.assertEqual(result,"1-800-001-5424")


    # Test checks if words_to_number() works with empty input
    def test_words2num_empty(self):
        self.test_number.set_number("")
        result = self.test_number.words_to_number()
        self.assertEqual(result,"")


    # Test checks if all_wordifications() works with empty input
    def test_allword_empty(self):
        self.test_number.set_number(None)
        result1, result2 = self.test_number.all_wordifications()
        self.assertEqual(result1,[])
        self.assertEqual(result1,[])

    # Test checks if all_wordifications() works with number set with only letters
    def test_allword_letters(self):
        self.test_number.set_number("racecar")
        result1,result2 = self.test_number.all_wordifications()
        self.assertTrue(len(result1)>1)
    # #
    #
    # # Test checks if words_to_number() works with empty input
    # def test_words2num_empty(self):
    #     self.test_number.phone_number = ""
    #     result = self.test_number.words_to_number()
    #     self.assertEqual(result,"")






if __name__ == 'main':
    unittest.main()
