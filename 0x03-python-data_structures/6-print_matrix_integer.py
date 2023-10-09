#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for i in matrix:
        for elem in range(0, len(i)):
            print("{:d}".format(i[elem]), end="")
            if elem != (len(i) - 1):
                print(" ", end="")
        print("")


if __name__ == '__main__':
    print_matrix_integer()
