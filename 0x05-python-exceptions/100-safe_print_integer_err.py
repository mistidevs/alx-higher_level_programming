#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as ve:
        print("Exception: {}".format(ve), file=sys.stderr)
        return False


if __name__ == '__main__':
    safe_print_integer_err()
