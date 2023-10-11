#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None or search is None or replace is None:
        return my_list
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
    return my_list


if __name__ == '__main__':
    search_replace()
    
