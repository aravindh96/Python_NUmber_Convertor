
"""
Main.py when run on terminal requests input from the user
and runs the appropriate function.
"""

from conversion_functions import NumberConverter
from util import Number

testnum = NumberConverter("1800-Painter")
flag = True
while(flag):

    number = input("Please enter the phone number: ")

    option = input(" Please enter the OPTION NUMBER:\n \
            1. words_to_number()\n \
            2. number_to_words()\n \
            3. all_wordifications()\n \
            OPTION NUM: ")

    testnum.set_number(str(number))
    if option == "1":
        print("\n" + testnum.words_to_number())

    elif option == "2":
        print("\n" + testnum.number_to_words())

    elif option == "3":
        num_list, eng_list = testnum.all_wordifications()
        print("\n" ,num_list)
        print("\n List of possible english words", eng_list)

    else:
        print("Invalid Input")

    cont = input("\n Do you want to continue (Y/N) :")
    if (cont.upper() == "N" ):
        flag = False
