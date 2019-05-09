#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
#    new = dict(a_dictionary)
    for key, val in sorted(a_dictionary.items()):
        print("{}: {}".format(key, val))
