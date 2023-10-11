#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None or value is None:
        return a_dictionary
    keys = []
    keys[:] = [items for items in a_dictionary]
    for item in keys:
        if a_dictionary[item] == value:
            del a_dictionary[item]
    return a_dictionary


if __name__ == '__main__':
    complex_delete()
