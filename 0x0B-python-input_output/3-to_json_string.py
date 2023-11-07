#!/usr/bin/python3
""" Converting to JSON object """
import json


def to_json_string(my_obj):
    """ Returning the JSON representation of a string """
    return json.dumps(my_obj)


if __name__ == '__main__':
    to_json_string()
