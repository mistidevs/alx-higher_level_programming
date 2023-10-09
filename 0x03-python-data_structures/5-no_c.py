#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return
    new_string = ""
    for l in my_string:
        if l != 'c' and l != 'C':
            new_string += l
    return new_string


if __name__ == '__main__':
    no_c()
