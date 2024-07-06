#!/usr/bin/python3
""" takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8) """

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email).encode()
    request = url.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
