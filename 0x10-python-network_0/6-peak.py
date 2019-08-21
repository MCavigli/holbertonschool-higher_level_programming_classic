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


def rfind(list_of_integers, start, end):
    """ recursive function to find peak """
    if start == end:
        return (list_of_integers[end])
    mid = (start + end) // 2
    if mid == len(list_of_integers) - 1 or mid == 0:
        return list_of_integers[mid]

    elif list_of_integers[mid] > list_of_integers[mid + 1]:
        return rfind(list_of_integers, start, mid)
    return rfind(list_of_integers, mid + 1, end)
