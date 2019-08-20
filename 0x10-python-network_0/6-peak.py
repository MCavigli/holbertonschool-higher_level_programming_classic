#!/usr/bin/python3
# Module that finds the peak of an unsorted list of ints


def find_peak(list_of_integers):
    """ finds the peak of an unsorted list of ints """
    if not list_of_integers:
        return None
    length = len(list_of_integers)
    sp = length // 2
    if length == 1:
        return list_of_integers[sp]
    if length == 2:
        if list_of_integers[sp] > list_of_integers[sp - 1]:
            return list_of_integers[sp]
        else:
            return list_of_integers[sp - 1]

    while ((list_of_integers[sp] < list_of_integers[sp - 1] or
            list_of_integers[sp] < list_of_integers[sp + 1]) and
           (sp != 0) and (sp != length)):
        if list_of_integers[sp] < list_of_integers[sp + 1]:
            sp += 1
            continue
        elif list_of_integers[sp] < list_of_integers[sp - 1]:
            sp -= 1
            continue
    return list_of_integers[sp]
