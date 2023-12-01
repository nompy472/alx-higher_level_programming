#!/usr/bin/python3
"""
Display GitHub user id using GitHub API.
"""

import requests
import sys


def get_github_id(username, password):
    """
    Retrieves GitHub user id using GitHub API.
    :param username: GitHub username
    :param password: Personal access token as password
    :return: GitHub user id
    """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=(username, password))
    data = response.json()
    user_id = data.get('id')
    return user_id


if __name__ == "__main__":
    github_username = nompy472
    github_password = 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

    user_id = get_github_id(github_username, github_password)
    print(f"GitHub User ID: {user_id}")
