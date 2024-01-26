#!/usr/bin/python3
"""
Fetching the body of a link
"""
import requests


if __name__ == '__main__':
    html = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))
