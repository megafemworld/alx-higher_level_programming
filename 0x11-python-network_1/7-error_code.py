#!/usr/bin/python3
""" Python script that takes in a URL,
sends a request to the URL and displays the body of the response."""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        req = requests.get(url)
        req.raise_for_status()

        print(response.text)

    except requests.exception.HTTPerror as e:
        print("Error code: {}".format(e.req.status_code))
