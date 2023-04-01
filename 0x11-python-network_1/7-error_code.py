#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response.
"""


import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if (r.status_code == requests.codes.ok):
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
