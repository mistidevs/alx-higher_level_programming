#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0:
        return my_list
    if idx > (length - 1):
        return my_list
    for i in my_list:
        if i == idx:
            my_list[i] = element
            return my_list


if __name__ == '__main__':
    replace_in_list()
