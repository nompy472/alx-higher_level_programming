#!/usr/bin/python3
"""
Module that fetch and display the body of the response
from https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()
        content = body.decode('utf-8')

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", content)
