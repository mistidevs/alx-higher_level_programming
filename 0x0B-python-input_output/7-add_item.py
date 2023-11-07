#!/usr/bin/python3
""" Adding all args to a PyList """
import sys
import json


def add_item():
    """ Adding item(s) to a JSON file """
    load = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    try:
        my_obj = load("add_item.json")
    except FileNotFoundError:
        my_obj = []

    for i in range(1, len(sys.argv)):
        my_obj.append(sys.argv[i])

    save_to_json_file(my_obj, "add_item.json")


if __name__ == '__main__':
    add_item()
