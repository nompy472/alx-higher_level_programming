#!/usr/bin/python3
"""
Sends a request to a given URL and display the body of the response.
"""

import requests
import sys


def fetch_url(url):
    """
    Sends a request to the URL and display the body of the response.
    :param url: The URL to send the request to.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as errh:
        print(f"Error code: {errh.response.status_code}")
    except requests.exceptions.RequestException as err:
        print(f"Request failed: {err}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url(url)
