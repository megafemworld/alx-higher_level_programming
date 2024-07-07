#!/usr/bin/python3
"""display github id"""

import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com.user"

    r = requests.get(url, auth=(username, token))
    user_data = r.json()
    print(user_data.get("id"))

