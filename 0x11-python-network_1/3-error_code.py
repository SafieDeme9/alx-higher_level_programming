#!/usr/bin/python3
"""
 sends a request to the URL and
 displays the body of the response (decoded in utf-8).
"""


import sys
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except URLError as e:
        print("Error code: {}".format(e.code))
