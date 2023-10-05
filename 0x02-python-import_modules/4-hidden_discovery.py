#!/usr/bin/python3
def find():
    hidden = __import__("hidden_4")
    for name in dir(hidden):
        if name[0] != '_':
            print(name)


if __name__ == '__main__':
    find()
