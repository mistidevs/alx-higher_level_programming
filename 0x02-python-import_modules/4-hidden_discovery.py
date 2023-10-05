#!/usr/bin/python3
def find():
    hidden = dir("hidden_4.pyc")
    for i in range(len(hidden)):
        if hidden[i][0] != '_':
            print("{}".format(hidden[i]))


if __name__ == '__main__':
    find()
