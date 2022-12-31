# project Basic calculator
'''
- Ask the user their name TICK
- Have the user provide three numbers TICK
- Add the first two numbers together, then multiply the result with the third number TICK
- Output the result in a long sentence that includes the user's name, the numbers they chose, and the following result TICK
'''
user_name = input("Hi, what's your name? ")
print("Please enter three numbers")
num_one = int(input("Please choose your first number: "))
num_two = int(input("Please choose your second number: "))
num_three = int(input("Please choose your third number: "))
result = (num_one+num_two) * num_three
print("Hello, {}. You chose {}, {} and {} as your numbers. {} is your result".format(user_name, num_one,num_two,num_three,result))

# Weight convertor
'''
Create a programme that converts Pounds to Kg
- Allows the user to input a weight in Pounds, and outputs the weight in Kg 
'''
'''
- Create a variable that is the multiplier for Pounds to Kg (Need to research) TICK
- Input for user (Pounds) TICK
- Output for user (Kg) TICK
'''
conversion_multiplier = 0.45359237
user_pounds = int(input('Enter the amount of Pounds to convert to Kg'))
converted_kg = user_pounds * conversion_multiplier
print('You entered: '+str(user_pounds)+'. This converts to : '+str(converted_kg)+' pounds')

# DIce Simulator
'''
- Create a program that simulates two dice being rolled
- In the program give a message to the user saying what the two dice values are and their combined total
'''
'''
- import random module TICK
- Generate two numbers that are random and between 1-6 TICK
- Print the two numbers and their sum
'''
from random import randint
num_one = randint(1,6)
num_two = randint(1,6)
dice_total = num_one + num_two
print("Dice simulation complete! Num one: {}, num two: {}. The total is: {}".format(num_one, num_two, dice_total))