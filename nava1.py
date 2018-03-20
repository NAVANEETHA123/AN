import os
import time
import tweepy
consumer_key ="zQRMoTIlyVUV0Pxeex9YoCzYS"
consumer_secret ="PYwcSMzvgeT5yLAZkQtnMnj0BbotCR7ee0G2Ykz3CrtkUKgYxv"
access_token ="968078089912766464-Zvw0xtO8C5hNFSRkdQYBcwY3hMWUfFa"
access_token_secret ="aXExcoNfbWtf8kVitCqCnw3aKMDDGpAhPGDH0M2oUBFqK"
   


auth = tweepy. OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy. API(auth)
b=1
a=0
while a<=2 :
    img="/home/cs2017a119/Desktop/img.jpg"
    cmd="fswebcam -f 3 --fps 20 -r 800*600 /home/cs2017a119/Desktop/img.jpg"
    os.system(cmd)
    print("pic taken")
    api. update_with_media(img, status="nice one")
    print("wait for 5 seconds for selfie")
    time.sleep(5)
    a+=1
    b+=1
    print("success")
