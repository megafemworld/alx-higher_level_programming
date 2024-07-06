#!/usr/bin/python3

""" Send a request to the URL and handle Error """

import urllib.request
import urllib.error
import sys


if __name__ = "__main__":
    url = sys.argv[1]

    try:
        url = urllib.request.Response(url)
        with urllib.request.urlopen() as responsde:
            print(response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        print(f"Error code: (e.code)")
