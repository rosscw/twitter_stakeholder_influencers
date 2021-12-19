# Set up
pip install tweepy
import tweepy
from auth_tokens import * 

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Define authorised client call
client = tweepy.Client(bearer_token = bearer_token, consumer_key = consumer_key, consumer_secret = consumer_secret)

# Extract handles for each account being followed by stk_id
stk_id = 515600557 #tara_flores as test case
for id in tweepy.Paginator(client.get_users_following, id = stk_id, max_results = 100).flatten(limit = 5) :
                           print(id)
