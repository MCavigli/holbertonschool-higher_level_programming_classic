#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for i in range(len(my_list)):
        if my_list[i] % 2:
            new.append(False)
        else:
            new.append(True)
    return new
