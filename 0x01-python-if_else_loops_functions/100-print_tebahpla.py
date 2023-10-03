#!/usr/bin/python3
flag = 0
for i in range(122, 96, -1):
    if flag == 0:
        w = chr(i)
        flag = 1
    else:
        w = chr(i - 32)
        flag = 0
    print("{}".format(w), end="")
