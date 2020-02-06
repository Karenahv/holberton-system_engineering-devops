#!/usr/bin/python3
""" all posts recursively"""

import requests


base_url = 'http://reddit.com/r/{}/hot.json'


def recurse(subreddit, hot_list=[]):
    """all posts recursively"""
    after = ""
    headers = {'User-agent': 'karenahv'}
    params = {'t': all, 'after': after}
    req = requests.get(base_url.format(subreddit), headers=headers,
                       params=params)
    if not req or req.status_code != 200:
        return None
    info = req.json()
    for hot in info['data']['children']:
        hot_list.append(hot['data']['title'])
    after = info.get('after')
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list
