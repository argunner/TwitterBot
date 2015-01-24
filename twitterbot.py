#code for @jessgarsonbot

import tweepy, time, sys
 
argfile = str(sys.argv[1])

CONSUMER_KEY = 'My Consumer Key (API Key)'
CONSUMER_SECRET = 'My Consumer Secret (API Secret)'
ACCESS_KEY = 'My Access Token'
ACCESS_SECRET = 'My Access Token Secret'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

with open(argfile,'r') as f:
 for line in f.readlines():
  api.update_status(line)
  time.sleep(900) #This tweets every 15 minutes 
