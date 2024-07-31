#!/usr/bin/python3
"""
    function top_ten
"""
from sys import argv
import requests


def top_ten(subreddit):
    """
        returns the top ten posts for a given subreddit
    """
    user = {'User-Agent': 'Feisty-Musician7531'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
