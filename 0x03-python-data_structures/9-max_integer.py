#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    for i in range(len(my_list)):
        swapped = False
        for j in range(len(my_list) - i - 1):
            if my_list[j] < my_list[i + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
                swapped = True
        if not swapped:
            break

    return my_list[0]
