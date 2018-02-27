# importing the module
import tweepy
 
# personal details
consumer_key ="zQRMoTIlyVUV0Pxeex9YoCzYS"
consumer_secret ="PYwcSMzvgeT5yLAZkQtnMnj0BbotCR7ee0G2Ykz3CrtkUKgYxv"
access_token ="968078089912766464-Zvw0xtO8C5hNFSRkdQYBcwY3hMWUfFa"
access_token_secret ="aXExcoNfbWtf8kVitCqCnw3aKMDDGpAhPGDH0M2oUBFqK"
  
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 
# update the status
api.update_status(status ="Hello Everyone !")
