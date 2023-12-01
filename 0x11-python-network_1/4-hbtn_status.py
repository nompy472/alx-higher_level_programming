#!/usr/bin/python3
"""
Fetches the status of https://alx-intranet.hbtn.io
using the requests package.
"""

import requests


def fetch_alx_status():
    """
    Fetches and prints the status of https://alx-intranet.hbtn.io.
    """
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    # Accessing dictionary value by key using get
    status = response.json().get("status")

    print("Status:", status)


if __name__ == "__main__":
    fetch_alx_status()
