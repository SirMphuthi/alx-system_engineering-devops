#!/usr/bin/python3

"""
a function that queries Reddit API and prints titles
of first 10 hot posts given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries Reddit API
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            data = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
