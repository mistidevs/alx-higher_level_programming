#!/usr/bin/python3
"""
Send an email as a parameter
"""
import urllib.request
import sys
import urllib.parse


if __name__ == '__main__':
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]

        values = {'email': email}
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii')

        req = urllib.request.Request(url, data)

        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
