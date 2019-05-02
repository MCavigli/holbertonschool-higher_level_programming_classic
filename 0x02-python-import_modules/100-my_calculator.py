#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)

    op = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif op == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
