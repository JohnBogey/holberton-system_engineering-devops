#!/usr/bin/python3
'''
Gets top 10 hot posts of subreddit
'''
import requests


def top_ten(subreddit):
    ''' prints top 10 hot poist of subreddit '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent':
               'Python:sub.counter:v0.1 (by /u/01100100011011110111)'}
    payload = {'limit': 10}
    res = requests.get(url, headers=headers, allow_redirects=False,
                       params=payload)

    try:
        for post in res.json()['data']['children']:
            print(post['data']['title'])
    except Exception as e:
        print(None)
