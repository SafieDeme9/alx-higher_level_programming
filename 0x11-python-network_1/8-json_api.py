#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": q}
    r = requests.post(url, data=payload)
    try:
        rep = r.json()
        if (rep == {}):
            print("No result")
        else:
            print("[{}] {}".format(rep.get("id"), rep.get("name")))
    except ValueError:
        print("Not a valid JSON")
