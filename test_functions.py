
import unittest

from conversion_functions import NumberConverter
from util import Number

class TestHelperFunctions(unittest.TestCase):

    test_number = Number("18009493582")

    def test_strip_num(self):
        # Test that strip_number() can remove all non alphanumeric characters
        data = "_&^12#@!()34ab$*:\"\\,./?fe"
        result = self.test_number.strip_number(data)
        self.assertEqual(result, "1234abfe")

    def test_strip_empty(self):
        # Test that strip_number() works for empty string
        data = ""
        result = self.test_number.strip_number(data)
        self.assertEqual(result, "")

    def test_strip_int(self):
        # Test that strip_number() works for non strings
        data = 4585
        result = self.test_number.strip_number(data)
        self.assertEqual(result, "4585")

    def test_valid_int(self):
        # Test that valid_word() works for non strings
        data = 45859451
        result = self.test_number.valid_word(data)
        self.assertEqual(result, "")

    def test_valid_characters(self):
        # Test that valid_word() can remove all non alphabets &
        # test for finding mixed case words - 'HeLlO'
        data = "_&^12#@!()34ab$*:\"HeLlO\\,./?fe"
        result = self.test_number.valid_word(data)
        self.assertEqual(result.lower(), "hello")

    def test_valid_multiple(self):
        # Test that valid_word() returns first word in multi-word input
        data = "12ringing-bells"
        result = self.test_number.valid_word(data)
        self.assertEqual(result.lower(), "ringing")

    def test_format_pattern(self):
        # Test that phone_format() works well with '-' character
        data = "12ringing-bells"
        result = self.test_number.phone_format(data)
        self.assertEqual(result.lower(), "12-ringing-bells")

    def test_format_empty(self):
        # Test that phone_format() works with empty input
        data = ""
        result = self.test_number.phone_format(data)
        self.assertEqual(result.lower(), "")

    def test_format_number(self):
        # Test that phone_format() returns pattern for unusual number formats
        data = "1800-8-8.5  4    2-895/47"
        result = self.test_number.phone_format(data)
        self.assertEqual(result.lower(), "1-800-885-428-9547")


class TestMainFunctions(unittest.TestCase):

    test_number = NumberConverter("18009456741")

    def test_words2num(self):
        # Test that words_to_number() returns correct pattern removing non alphanumeric characters
        self.test_number.num.phone_number = "18#!0\ 0\"-P8y*th(on)"
        result = self.test_number.words_to_number()
        self.assertEqual(result, "1-800-789-8466")

    def test_words2num_digits(self):
        # Test checks if words_to_number() works with pure digit input
        self.test_number.set_number("1800-0015-424")
        result = self.test_number.words_to_number()
        self.assertEqual(result, "1-800-001-5424")

    def test_words2num_empty(self):
        # Test checks if words_to_number() works with empty input
        self.test_number.set_number("")
        result = self.test_number.words_to_number()
        self.assertEqual(result, "")

    def test_allword_empty(self):
        # Test checks if all_wordifications() works with empty input
        self.test_number.set_number("")
        result1, result2 = self.test_number.all_wordifications()
        self.assertEqual(result1, [])
        self.assertEqual(result1, [])

    def test_allword_letters(self):
        # Test checks if all_wordifications() works with number set with only letters
        self.test_number.set_number("racecar")
        result1,result2 = self.test_number.all_wordifications()
        self.assertTrue(len(result1)>1)

    def test_number2word_empty(self):
        # Test checks if number_to_word() works with empty string
        self.test_number.set_number("")
        result1, result2= self.test_number.all_wordifications()
        result3 = self.test_number.number_to_words()
        self.assertIn(result3, "")

    def test_number2word_special_char(self):
        # Test checks if number_to_word() works with all non alpha numeric input
        self.test_number.set_number("^%&^@(*#@)")
        result1, result2= self.test_number.all_wordifications()
        result3 = self.test_number.number_to_words()
        self.assertIn(result3, "")

    def test_number2word_letter(self):
        # Test checks if number_to_word() works with both number and letters
        self.test_number.set_number("1800-%You_hI")
        result1, result2= self.test_number.all_wordifications()
        result3 = self.test_number.number_to_words()
        self.assertIn(result3, result1)


if __name__ == 'main':
    unittest.main()
