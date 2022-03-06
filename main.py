import json
import praw
import asyncio

subr = 'testing' #define subreddit
credentials = 'client_secrets.json' #define creds/validate login

with open(credentials) as f: #open creds and load json
    creds = json.load(f)

reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     user_agent=creds['user_agent'],
                     redirect_uri=creds['redirect_uri'],
                     refresh_token=creds['refresh_token'])

subreddit = reddit.subreddit(subr) #define subreddit in praw

title0='test'
selftext0 = '''test'''


async def main():    #main, use async and set delay to 50-1000 for each post.
    reddit.validate_on_submit = True
    subreddit.submit(title1, selftext=selftext1)
    await asyncio.sleep(500)
    subreddit.submit(title2, selftext=selftext2)
    await asyncio.sleep(500)
    subreddit.submit(title3, selftext=selftext3)
    await asyncio.sleep(500)
    subreddit.submit(title4, selftext=selftext4)
    await asyncio.sleep(500)
asyncio.run(main())
