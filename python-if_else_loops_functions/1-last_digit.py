#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = number % -10 if number < 0 else number % 10
if number2 > 5:
    print(f"Last digit of {number} is {number2} and is greater than 5")
elif number2 == 0:
    print(f"Last digit of {number} is {number2} and is 0")
elif number2 < 6 and number2 != 0:
    print(f"Last digit of {number} is {number2} and is less than 6 and not 0")
