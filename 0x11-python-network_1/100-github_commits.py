#!/usr/bin/python3
"""Print all commits by: `<sha>: <author name>` (one by line)"""

import requests
import sys

repo = sys.argv[1]
owner = sys.argv[2]

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(repo, owner)
    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                    commits[i].get("sha"),
                    commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
