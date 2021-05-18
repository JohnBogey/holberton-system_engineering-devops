#!/usr/bin/python3
'''
Creates list of hot post titles
'''
import requests
import time


def recurse(subreddit, hot_list=[], after="NULL"):
    ''' creates list of hot post titles recursively '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent':
               'Python:sub.counter:v0.1 (by /u/01100100011011110111)'}
    payload = {'after': after}
    res = requests.get(url, headers=headers, allow_redirects=False,
                       params=payload)
    try:
        for post in res.json()['data']['children']:
            hot_list.append(post['data']['title'])
    except Exception as e:
        return None
    after = res.json()['data']['after']
    if after not in [None, 'None', 'NULL']:    
        return recurse(subreddit, hot_list, after)
    return hot_list
