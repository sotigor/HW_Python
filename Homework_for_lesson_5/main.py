# Homework for lesson 5

# Task №1. The Guessing Game.

import random

# Guessing the random integer number from 1 to 10

random.number = random.randint(1, 10)
counter = 0
while True:
    player_number = input('Enter the integer number from 1 to 10: ')
    counter += 1
    if player_number.isnumeric() and 1 <= int(player_number) <= 10:
        if int(player_number) > random.number:
            print('Try a little less')
        elif int(player_number) < random.number:
            print('Try a little greater')
        elif int(player_number) == random.number and counter < 3:
            print('You won!\nYou guessed the number using only 1 attempt!!!')
            break
        else:
            print('You won using {} attempt!'.format(counter))
            break
    else:
        print('Your data is incorrect. You lost. ')
        break

# Task №2. The birthday greeting program.

name = input('Enter your name: ')
age = input('Enter your age: ')
print('Hello {}, on your next birthday you will be {} years!'.format(name.lower().capitalize(), int(age) + 1))

# Task №3. Words combination.

import random

# Creating new strings from the characters of inputed string

user_word = input('Enter the any string you like: ')
counter = 1
print('The original string is: {}'.format(user_word))
while counter <= 5:
    word_length = len(user_word)
    random_word = ""
    cutting_word = user_word
    while word_length > 0:
        random_character = random.choice(cutting_word)
        random_character_index = cutting_word.rfind(random_character)
        cutting_word = cutting_word[:random_character_index] + cutting_word[random_character_index + 1:]
        random_word += random_character
        word_length -= 1
    print('The string made from random characters of string "{}" is: {}'.format(user_word, random_word))
    counter += 1

# Task №4. The math quiz program.

import random

# Solving mathematical expression

signs_raw = '+-*/'
number_1 = random.choice(range(1, 11))
number_2 = random.choice(range(1, 11))
sign = random.choice(signs_raw)
user_answer = input('Solve the expression: {}{}{} = '.format(number_1, sign, number_2))
if sign == "+":
    if number_1 + number_2 == int(user_answer):
        print('Answer is correct! You are the best!')
    else:
        print('The answer is incorrect! You need to renew your knowledge of mathematics')
elif sign == "-":
    if number_1 - number_2 == int(user_answer):
        print('Answer is correct! You are the best!')
    else:
        print('The answer is incorrect! You need to renew your knowledge of mathematics')
elif sign == "*":
    if number_1 * number_2 == int(user_answer):
        print('Answer is correct! You are the best!')
    else:
        print('The answer is incorrect! You need to renew your knowledge of mathematics')
elif sign == "/":
    if number_1 / number_2 == round(float(user_answer), 2):
        print('Answer is correct! You are the best!')
    else:
        print('The answer is incorrect! You need to renew your knowledge of mathematics')

#Task №5.

from Converter import get_rgb
print('RGB is', get_rgb.red, 'for red')
print('RGB is', get_rgb.green, 'for green')
print('RGB is', get_rgb.blue, 'for blue')

