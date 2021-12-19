# Set up
pip install tweepy
import tweepy

Auth details:


client = tweepy.Client(bearer_token = bearer_token, consumer_key = consumer_key, consumer_secret = consumer_secret)

for id in tweepy.Paginator(client.get_users_following, id = 515600557, max_results = 100).flatten(limit = 5) :
                           print(id)
