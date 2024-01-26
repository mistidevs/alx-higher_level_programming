#!/usr/bin/python3
"""
Getting commits
"""
import sys
import requests


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')

    if r.status_code == 200:
        commits = r.json()
        for commit in commits[:10]:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
