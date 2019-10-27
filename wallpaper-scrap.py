#! /usr/local/bin/python3

import praw, os, urllib

reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_APP_NAME',
                     username='YOUR_USERNAME',
                     password='YOUR_PASSWORD')

DOWNLOADS_DIR = 'reddit-wallpapers/'
url = []

hot_subreddit = reddit.subreddit('EarthPorn').top('month', limit=50)

for post in hot_subreddit:
    url.append(post.url)

for value in url:
    name = os.path.basename(value)
    
    os.makedirs(os.path.dirname(DOWNLOADS_DIR), exist_ok=True)
    
    filename = os.path.join(DOWNLOADS_DIR, name)
    
    if not os.path.isfile(filename):
        urllib.request.urlretrieve(value, filename)
