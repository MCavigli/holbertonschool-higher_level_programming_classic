#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of "
if number < 0:
    num = number * -1
    num = num % 10
else:
    num = number % 10

if num > 5:
    print(string + "{} is {} and is greater than 5".format(number, num))
elif num == 0:
    print(string + "{} is {} and is 0".format(number, num))
elif num < 6 and num != 0:
    print(string + "{} is {} and is less than 6 and not 0".format(number, num))
