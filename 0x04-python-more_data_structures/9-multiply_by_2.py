#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return a_dictionary
    new_dict = {}
    for item in a_dictionary:
        new_dict[item] = a_dictionary[item] * 2
    return new_dict


if __name__ == '__main__':
    multiply_by_2()
