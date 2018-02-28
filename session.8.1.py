# importing the module
import tweepy
 
# personal details
consumer_key ="cms5XtceH9bofTg2SgebT7RmE"
consumer_secret ="imgqQqr7w8g1WzEFnCmBu4iPP7KU4vTE5hyvAesMgnnK9LYXuG"
access_token ="966206289339650049-0XqoPVwkMKdYE9YEcXSGcVHI1Et2Rld"
access_token_secret ="v6ryrbdZhYlXvwZwm4MbJPaXbSoflq1jbYwJ66JGRXRlB"

 # authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="hello world")
print("tweeted successfully")
