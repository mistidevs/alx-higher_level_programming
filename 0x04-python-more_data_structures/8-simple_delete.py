#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None or key is None:
        return a_dictionary
    keys = []
    keys[:] = [item for item in a_dictionary]
    for item in keys:
        if item == key:
            del a_dictionary[key]
    return a_dictionary


if __name__ == '__main__':
    simple_delete()
