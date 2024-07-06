#!/usr/bin/python3
""" takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8) """

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = sys.argv[2]
    email = {"email": value}
    data = urllib.parse.urlencode(email).encode("ascii")

    request = url.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
