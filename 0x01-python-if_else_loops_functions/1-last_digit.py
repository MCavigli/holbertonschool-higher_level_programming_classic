#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
if number < 0:
    num = num * -1
if num > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, num))
elif num == 0:
    print("Last digit of {} is {} and is zero".format(number, num))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,num))
