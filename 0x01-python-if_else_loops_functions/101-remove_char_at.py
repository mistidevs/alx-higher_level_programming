#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        n_str = str[:n] + str[n+1:]
        return n_str
    else:
        return str
