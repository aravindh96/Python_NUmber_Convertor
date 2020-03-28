
import re
from nltk.corpus import words
class Number:

    def __init__(self, phone_number, word_set=None, phone_pad=None, keypad=None):
        """
        Initializing instance variables
        """
        self.phone_number = phone_number
        if word_set is None:
            word_set = set(words.words())
        self.word_set = word_set
        if phone_pad is None:
            phone_pad = {'0': [],
                         '1': [],
                         '2': ['A', 'B', 'C'],
                         '3': ['D', 'E', 'F'],
                         '4': ['G', 'H', 'I'],
                         '5': ['J', 'K', 'L'],
                         '6': ['M', 'N', 'O'],
                         '7': ['P', 'Q', 'R', 'S'],
                         '8': ['T', 'U', 'V'],
                         '9': ['W', 'X', 'Y', 'Z']}
        self.phone_pad = phone_pad
        if keypad is None:
            keypad = {}
        self.keypad = keypad
        for key, value in phone_pad.items():
            keypad.update(dict.fromkeys(value, key))

    def strip_number(self,number):
        """
        Input: Phone Number  - type:str
        Function: Removes all characters other than digits and alphabets
        """
        strip_num = re.sub('[^A-Za-z0-9]+', '', str(number))
        return strip_num

    def valid_word(self,number):
        """
        Input: Phone Number - type:str
        Function: Returns a valid english word in the given number
        """
        p = re.compile('[^A-Za-z]')
        word_list = p.split(str(number))
        word_list = list(filter(None, word_list))

        for word in word_list:
            if(word.lower() in self.word_set and len(word) > 2):
                return word
        return ""

    def phone_format(self,number):
        """
        Input: Phone Number - type: str
        Function: Returns formated number into following pattern
                  (d-ddd-ddd-dddd) or (ddd-lll-ddd) where d-digit; l-letter
        """
        clean_phone_number = self.strip_number(number)
        if not clean_phone_number:
            return clean_phone_number

        word = self.valid_word(number)

        if word:
            p = re.compile('(' + word + ')')
            num_list = p.split(clean_phone_number)
            num_list = list(filter(None, num_list))
            formatted_num = ""
            for i in range(len(num_list)):
                if i != len(num_list)-1:
                    formatted_num += num_list[i] + "-"
            formatted_num += num_list[-1]
            return formatted_num

        # Formats the number to the desired pattern using regex
        formatted_phone_number = (re.sub("(\w)(?=(\w{3})+(?!\w))", r"\1-", "%s" %
                                 str(clean_phone_number[:-1])) + clean_phone_number[-1])
        return formatted_phone_number
