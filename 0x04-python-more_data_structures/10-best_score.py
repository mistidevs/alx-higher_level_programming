#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return a_dictionary
    max_int = 0
    max_key = None
    for item in a_dictionary:
        if max_int < a_dictionary[item]:
            max_int = a_dictionary[item]
            max_key = item
    return max_key


if __name__ == '__main__':
    best_score()
