#!/usr/bin/python3
"""
Getting a header value of X-Request-Id
"""
import urllib.request
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.getheader('X-Request-Id'))
