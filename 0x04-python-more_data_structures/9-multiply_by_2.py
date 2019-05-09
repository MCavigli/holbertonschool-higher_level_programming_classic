#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = dict(a_dictionary)
    for key, val in new.items():
        val *= 2
        new[key] = val
    return new
