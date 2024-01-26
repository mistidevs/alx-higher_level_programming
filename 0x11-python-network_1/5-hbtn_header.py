#!/usr/bin/python3
"""
Fetching the body of a link
"""
import requests
import sys


if __name__ == '__main__':
    html = requests.get(sys.argv[1])
    print(html.headers.get('X-Request-Id'))
