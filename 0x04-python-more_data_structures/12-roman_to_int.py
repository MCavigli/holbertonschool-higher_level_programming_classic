#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for key, val in num.items():
        for i in range(len(roman_string)):
            if key == roman_string[i]:
                total += val
    return total


"""
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    length = len(roman_string) + 1
    total = 0
    for key, val in num.items():
        for i in range(length):
            try:
                num.keys()[key + 1]
            except IndexError:
                total += val
                break
            if (roman_string[i] == key &
            roman_string[i + 1] == num.keys()[key + 1]):
                total += num.values()[key + 1] - val
                break
            try:
                num.keys()[key + 1]
            except IndexError:
                total += val
                break
            if (roman_string[i] == num.keys()[key] &
            roman_string[i + 1] == num.keys()[key + 2]):
                total += num.values()[key + 2] - val
                break
            if key == roman_string[i]:
                total += val
    return total
"""

"""
    total = {}
    for i in range(len(roman_string)):
        if roman_string[i] == "I":
            if roman_string[i + 1] == "V":
"""

"""
    num = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10,
           'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'D': 500}
    dig = 0
    for key, val in num.items():
        for i in roman_string:
            if roman_string[i] == 'I' & roman_string[i + 1] == 'V':
                dig += num['IV']
                i += 1
                break
            if i == 'I' & i + 1 == 'X':
                dig += num['IX']
                i += 1
                break
            if i == 'X' & i + 1 == 'L':
                dig += num['XL']
                i += 1
                break

            if key == roman_string:
                dig += val
    return dig
"""
