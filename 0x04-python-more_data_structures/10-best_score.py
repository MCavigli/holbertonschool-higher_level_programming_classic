#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max = 0
    best = ''
    for key, val in a_dictionary.items():
        if val > max:
            max = val
            best = key
    return best
