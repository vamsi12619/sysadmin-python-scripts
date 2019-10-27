#! /usr/local/bin/python3

import praw, os, urllib

# Initialize reddit using your credentials http://www.storybench.org/how-to-scrape-reddit-with-python/
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_APP_NAME',
                     username='YOUR_USERNAME',
                     password='YOUR_PASSWORD')

DOWNLOADS_DIR = 'reddit-wallpapers/'
url = []

hot_subreddit = reddit.subreddit('EarthPorn').top('month', limit=50)

for post in hot_subreddit:
    url.append(post.url) # each link from each post is appended to a list

# https://stackoverflow.com/a/3173388
for value in url:
    name = os.path.basename(value) # taking only the value after '/' from the url as name
    
    os.makedirs(os.path.dirname(DOWNLOADS_DIR), exist_ok=True) # makes the directory where the photos are saved if it doesn't exist https://stackoverflow.com/a/12517490
    
    filename = os.path.join(DOWNLOADS_DIR, name) # combine the name and the downloads directory to get the local filename
    
    if not os.path.isfile(filename):
        urllib.request.urlretrieve(value, filename) # if the file doesn't exist, it gets downloaded
