#!/usr/bin/python3
"""
Querying Github credentials to get id
"""
import requests
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    token = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, token))
    if r.status_code == 200:
        print(r.json().get('id'))
    else:
        print(None)
