#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0:
        return None
    if idx > (length - 1):
        return None
    for i in my_list:
        if i == idx:
            return my_list[i]


if __name__ == '__main__':
    element_at()
