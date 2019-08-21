#!/usr/bin/python3
# Module that finds the peak of an unsorted list of ints


def find_peak(list_of_integers):
    """ finds the peak of an unsorted list of ints """
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    end = len(list_of_integers) - 1
    start = 0
    return rfind(list_of_integers, start, end)


def rfind(list_of_integers, start, end):
    """ recursive function to find peak """
    if start == end:
        return (list_of_integers[end])
    mid = (start + end) // 2
    if list_of_integers[mid] > list_of_integers[mid + 1]:
        return rfind(list_of_integers, start, mid)
    return rfind(list_of_integers, mid + 1, end)
