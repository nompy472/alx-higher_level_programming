#!/usr/bin/python3
"""
Takes a URL as input, sends a request to the URL
Displays the body of the response (decoded in utf-8).
It handles urllib.error.HTTPError exceptions
Prints the HTTP status code in case of an error.
"""

import urllib.request
import urllib.error
import sys


def fetch_url_body(url):
    """
    Fetches the body of the response from the given URL and prints it.
    If an HTTPError occurs, prints "Error code:" and the HTTP status code.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url_body(url)
