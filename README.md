# Pickle Robotics - Python Coding Exercise
Python Coding Exercise implementing functions that converts Phone Numbers to possible word combinations and vice-versa.
Only valid english words are returned as number combinations, this is achieved using the nltk corpus of english words.
Testcases have been implemented with 97% code coverage.

## Install

```
$ pip install nltk
$ python
```
In python before running main.py please download the wordset for the first time.
```
>>> import nltk
>>> nltk.download('words')
```
To run the application in terminal:
```
$ python main.py
```

To run the test cases:
```
$ python -m unittest discover
```

## Implementing the Following functions:
1. number_to_words() - Converts Phone number to wordified number
2. words_to_number() - Converts a number with a word to a pure phone number
3. all_wordifications() - Outputs all possible combination of English words in a given number

## Structure:
1. The 3 main functions are implemented as class methods in **conversion_functions.py**. 
2. Some variables such as the phone number and phone pad mapping along with helper functions to format the number are         implemented as methods in a class in **util.py**.
3. **main.py** creates objects of the classes and provides a user input interface when run on the command line.
4. **test_functions.py** contain some testcases for both helper and main functions.

## Assumptions
1. Valid english words are returned using a corpus of words from nltk. Other languages can be implemented by downloading similar wordsets.
2. Only one word is recognised in any given phone number. For ex. '1800-GOT-MONEY' will not be returned since it has two seperate words. 'GOT' & 'MONEY' will be returned with individual combinations. 
3. Callocations are not recognised in the nltk wordset, for ex 'racecar' will not be recognised.

## References
1. https://www.mobilefish.com/services/phonenumber_words/phonenumber_words.php
2. https://dev.to/petercour/swap-keys-and-values-in-a-python-dictionary-1njn
3. https://stackoverflow.com/questions/7058120/whats-the-best-way-to-format-a-phone-number-in-python
4. https://www.pythonforbeginners.com/regex/regular-expressions-in-python
5. https://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python
