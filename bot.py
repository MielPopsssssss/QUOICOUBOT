import re
import tweepy

# Replace the values with your own Twitter API credentials
consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 

# Authentication with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create a class inheriting from the StreamListener class provided by Tweepy
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweet_text = status.text
        # Use regular expressions to match different variations of "quoi"
        if re.search(r"(?i)quoi+[!?]*\s*", tweet_text):
            api.retweet(status.id)
            print("Retweeted a tweet:", tweet_text)
            self.reply_to_tweet(status)

    def reply_to_tweet(self, tweet):
        reply_text = "Quoicoubeh !"
        username = tweet.user.screen_name
        tweet_id = tweet.id
        api.update_status(f"@{username} {reply_text}", in_reply_to_status_id=tweet_id)

# Create an instance of the StreamListener class
my_stream_listener = MyStreamListener()

# Create a Stream object using the authentication and StreamListener
my_stream = tweepy.Stream(auth=api.auth, listener=my_stream_listener)

# Filter the stream to track specific keywords
my_stream.filter(track=["quoi"])

# Let the script run indefinitely to listen for new tweets and retweet if necessary
print("Bot is running. Listening for tweets...")
while True:
    try:
        pass
    except KeyboardInterrupt:
        my_stream.disconnect()
        break
