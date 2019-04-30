#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of "
num = number % 10
if number < 0:
    num = num * -1
if num > 5:
    print(string + "{} is {} and is greater than 5".format(number, num))
elif num == 0:
    print(string + "{} is {} and is zero".format(number, num))
else:
    print(string + "{} is {} and is less than 6 and not 0".format(number, num))
