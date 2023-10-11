#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return 0
    set_list = []
    res = 0
    for i in range(len(my_list)):
        if my_list[i] not in set_list:
            res += my_list[i]
        set_list.append(my_list[i])
    return res


if __name__ == '__main__':
    uniq_add()
