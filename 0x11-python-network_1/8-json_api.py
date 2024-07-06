#!/usr/bin/python3
""" script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user with
the letter as a parameter."""

import requests
import sys

if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    load = {"q": q}
    try:
        r = requests.post("http://0.0.0.0:5000/search_user", data=load)
        resp_json = r.json()
        if resp_json != {}:
            print("[{}] {}".format(resp_json.get("id"), resp_json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
