#!/usr/bin/python3
""" From JSON string to PyObject """
import json


def from_json_string(my_str):
    """ Converting from JSON to PyObject """
    return json.loads(my_str)


if __name__ == '__main__':
    from_json_string()
