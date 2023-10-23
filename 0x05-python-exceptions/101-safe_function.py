#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
    


if __name__ == '__main__':
    safe_function()
