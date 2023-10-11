#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_sort = []
    dict_sort[:] = sorted(a_dictionary)
    for item in dict_sort:
        print("{}: {}".format(item, a_dictionary[item]))
    return dict_sort


if __name__ == '__main__':
    print_sorted_dictionary()
