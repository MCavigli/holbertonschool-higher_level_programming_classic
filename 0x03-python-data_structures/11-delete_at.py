#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
