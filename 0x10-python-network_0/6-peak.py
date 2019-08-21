#!/usr/bin/python3
# Module that finds the peak of an unsorted list of ints


def find_peak(list_of_integers):
    """ finds the peak of an unsorted list of ints """
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    return rfind(list_of_integers, 0, len(list_of_integers) - 1,
                 len(list_of_integers))


def rfind(ilist, start, end, length):
    """ recursive function to find peak """
    mid = start + (end - start) // 2
    if (mid == 0 or ilist[mid - 1] <= ilist[mid]) and\
       (mid == length - 1 or ilist[mid + 1] <= ilist[mid]):
        return ilist[mid]
    elif (mid > 0 and ilist[mid - 1] > ilist[mid]):
        return rfind(ilist, start, mid - 1, length)
    else:
        return rfind(ilist, mid + 1, end, length)
