#!/usr/bin/python3
"""
Sends a request to a given URL
and display the value of the X-Request-Id variable
"""

import urllib.request
import sys


def fetch_x_request_id(url):
    """
    Sends a request to the specified URL and
    display the X-Request-Id value
    :param url: The URL to send the request to
    """
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            if x_request_id:
                print(x_request_id)
    except urllib.error.URLError as e:
        print(f"Error accessing the URL: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)
