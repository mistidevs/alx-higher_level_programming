#!/usr/bin/python3
"""
API Search with JSON
"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    try:
        response = requests.post('http://0.0.0.0:5000/search_user',
                                 data={'q': q})
        json_response = response.json()
        if 'id' in json_response and 'name' in json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
