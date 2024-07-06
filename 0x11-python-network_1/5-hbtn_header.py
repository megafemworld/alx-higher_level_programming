#!/usr/bin/python3
""" script that takes in a URL,
sends a request to the URL and displays the
value of the variable X-Request-Id"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    resp = requests.get(url)
    x_r_id = resp.headers.get('X-Request-Id')
    print(x_r_id)
