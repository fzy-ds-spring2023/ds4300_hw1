"""
Felix Yang, Ayushi Shirke
Run API calls to insert into database and retrieve home timelines
Using Python time library to record time
"""
from dotenv import load_dotenv
import os
from tweet_api import TwitterAPI
from tweet_object import Tweet
import pandas as pd
import random
import time

load_dotenv()

def main():

    # Authenticate
    api = TwitterAPI(os.environ["MYSQL_USER"], os.environ["MYSQL_PASS"], "twitterdb")
    
    # generate follows table
    follow = pd.read_csv("data/follows.csv")
    api.generate_follows_from_dataframe(follow)
    
    # insert tweets (1,000,000 / time --> inserts/sec)
    start = time.time()
    df_tweet = pd.read_csv("data/tweet.csv")
    
    # get Tweet object from row
    for _, row in df_tweet.iterrows():
        api.post_tweet(Tweet(user=row[0], ts=None, text=row[1]))
    print(f'Time = {round(time.time()-start, 4)} seconds')
    
    # get distinct users
    users = api.get_users()

    # get timelines (100 / time --> timelines/sec)
    timelines = []
    before = time.time()
    for _ in range(100):
        user = random.choice(users) # randomize from distinct user list, then call api
        timelines.append(api.get_user_timeline(user))
    print(f'Time = {round(time.time()-before, 4)} seconds')

if __name__ == '__main__':
    main()