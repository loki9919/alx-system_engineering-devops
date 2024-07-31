#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""


    try:
        headers = {"User-Agent": "/u/Feisty-Musician7531"}
        with requests.get(
            "https://www.reddit.com/r/{}/about.json".format(subreddit),
            timeout=30,
            headers=headers,
            allow_redirects=False,
        ) as r:
            if r.status_code == 200:

                return r.json().get("data").get("subscribers")
            else:
                return 0
    except requests.RequestException:
        return 0
