#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""

import urllib.request
import sys

if __name__ == "__main__":
    ur = sys.argv[1]
    url = urllib.request.Request(ur)
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
