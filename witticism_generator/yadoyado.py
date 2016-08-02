# coding:utf-8
# Tweet something like a witticism every 30 minutes.

from MakeSentence import generateString
import time
import logging
import twitpic
import tweepy

# key should be encrypted
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

def imgUpload(file, message = ""):
    """Upload image to twitpic"""
    SERVICE_KEY = "a4b65c3eb11eae8a6799d0ee6d650e34"
    twit = twitpic.TwitPicOAuthClient(consumer_key = CONSUMER_KEY,
                                      consumer_secret = CONSUMER_SECRET,
                                      service_key = SERVICE_KEY,
                                      access_token = "oauth_token=%s&oauth_token_secret=%s" % (ACCESS_KEY, ACCESS_SECRET)
                                      )
    # image upload
    response = twit.create("upload", { 'message':message, 'media':file})
    return response["url"]

def post(message):
    """Post message"""
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(message)

if __name__ == "__main__":
    # url = imgUpload("img/XP.jpg")
    # post(url + "\n" + "poyo")
    # time.sleep(30)
    # logging.basicConfig(filename = 'yadoyado.log', level = logging.INFO, format = '%(asctime)s %(message)s')
    while True:
        s = generateString()
        print s
        # logging.info(s)
        # post(s)
        # time.sleep(30 * 60)
