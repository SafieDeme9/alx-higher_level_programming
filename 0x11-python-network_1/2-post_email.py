#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    mail = urllib.parse.urlencode(email).encode('ascii')
    req = urllib.request.Request(url, mail)
    with urllib.request.urlopen(req) as rep:
        print(rep.read().decode('utf-8'))
