# Number Guessing Game
# The Name Of The Developer Of This Game => Moein Heshmati

# Library
import os
import random
from datetime import datetime
from pyfiglet import figlet_format
from termcolor2 import colored


# Clear Terminal
os.system('clear')

# Welcome
print(colored(
    '==================================================================', color='blue'))
print(colored(figlet_format('Welcome'), color='cyan'))
print(colored(
    '==================================================================', color='blue'))
print(colored('Welcome To Moein Number Guessing Game', color='cyan'))
print(colored('Start Working With The Number Guessing Game', color='white'))
time = datetime.now()
print(f'Your Date Of Use Of The Number Guessing Game program ===> {time}')
print(colored(
    '==================================================================', color='blue'))

# Value Input
number = range(0, 101)
number_guess = random.choice(number)

# Try For Program
try:

    # While
    while True:

        # User Input
        user_guess = int(input('Enter Your Guess ===> '))

        # IF
        if user_guess > 100:
            print(
                colored('=========================================', color='yellow'))
            print(colored('Available Range ===> 0 To 100', color='red'))

        elif user_guess < 0:
            print(
                colored('==========================================', color='yellow'))
            print(colored('Available Range ===> 0 To 100', color='red'))

        elif user_guess > number_guess:
            print(
                colored('=========================================', color='yellow'))
            print(colored(figlet_format('False'), color='red'))
            print(
                colored('Your Guess Is More Than System Number, Please reduce It', color='red'))

        elif user_guess < number_guess:
            print(
                colored('=========================================', color='yellow'))
            print(colored(figlet_format('False'), color='red'))
            print(colored(
                'Your Guess Is Less Than System Number, Please Make It More', color='red'))

        elif user_guess == number_guess:
            print(
                colored('==========================================', color='yellow'))
            print(colored(figlet_format('True'), color='green'))
            print(colored('Your Guess Is TRUE', color='green'))
            break

# Except For Try
except:
    print(colored('Please Try Again', color='red'))


# Finish
# Create By Moein Heshmati
