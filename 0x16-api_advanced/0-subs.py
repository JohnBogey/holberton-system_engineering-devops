#!/usr/bin/python3
'''
Gets sub count of subreddit
'''
import requests


def number_of_subscribers(subreddit):
    ''' gets subscriber count '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent':
               'Python:sub.counter:v0.1 (by /u/01100100011011110111)'}

    res = requests.get(url, headers=headers, allow_redirects=False)
    try:
        return res.json()['data']['subscribers']
    except Exception as e:
        return 0
