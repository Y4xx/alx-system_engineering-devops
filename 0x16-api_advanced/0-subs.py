#!/usr/bin/python3
""" Exporting csv files"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """
    number of subscribers method
    """

    headers = {'user-agent': '/u/Superstonk API Python for Holberton School'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    client = requests.session()
    client.headers = headers
    r = client.get(url, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()["data"]["subscribers"])
    else:
        return(0)
