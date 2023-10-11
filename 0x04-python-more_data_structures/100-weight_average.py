#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weight_score = 0
    weight = 0
    for item in my_list:
        weight_score += item[0] * item[1]
        weight += item[1]
    avg = weight_score / weight
    return avg


if __name__ == '__main__':
    weight_average()
