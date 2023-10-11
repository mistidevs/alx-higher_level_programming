#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None or key is None or value is None:
        return a_dictionary
    a_dictionary[key] = value
    return a_dictionary


if __name__ == '__main__':
    update_dictionary()
