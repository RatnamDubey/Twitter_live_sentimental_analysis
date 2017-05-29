# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:52:36 2017

@author: dubey
"""

import tweepy
import json
#import pandas as pd 
#from nltk.corpus import stopwords
from textblob import TextBlob
#rom wordcloud import WordCloud,STOPWORDS
#import matplotlib.pyplot as plt
import re
import os

try:
    os.remove("D:\\twitter-out.txt")
    os.remove("D:\\positive.txt")
    os.remove("D:\\negative.txt")
    os.remove("D:\\neutral.txt")
except OSError:
    pass


rat=[]

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'hofBwCjlrjAUVwZ9EeBDNJwPS'
consumer_secret = 'XTZm9hRl1mZN7NvVImz7OzueaxD4CPoZgiWwYcB1U5RoNUulBu'
access_token = '823229807886561280-PWZVubV3RgeWE0Iabt5uaeURZkrsIDS'
access_token_secret = 'QNjVl13jewWGgdzJbs76zeGc9kDLNPneNAKLchCuSgb00'

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)
        #print(decoded)
        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        krm = decoded['text']
        toke = TextBlob(krm)
        k = toke.polarity
        r = toke.subjectivity
        if k < -0.25 and r > 0.5:
            value = 'negetive'
            output = open("D:\\twitter-out.txt","a")
            output.write(value)
            output.write('\n')
            output.close()
            worddoc1 = re.sub('[^a-zA-Z\n\.]', ' ', krm)
            output1 = open("D:\\positive.txt","a")
            output1.write(worddoc1)
            output1.write('\n')
            output1.close()
        elif k > 0.25 and r > 0.5:
            value = 'positive'
            output = open("D:\\twitter-out.txt","a")
            output.write(value)
            output.write('\n')
            output.close()
            worddoc2 = re.sub('[^a-zA-Z\n\.]', ' ', krm)
            output1 = open("D:\\negative.txt","a")
            output1.write(worddoc2)
            output1.write('\n')
            output1.close()
        else:
            value = 'neutral'
            output = open("D:\\twitter-out.txt","a")
            output.write(value)
            output.write('\n')
            output.close()
            worddoc3 = re.sub('[^a-zA-Z\n\.]', ' ', krm)
            output1 = open("D:\\neutral.txt","a")
            output1.write(worddoc3)
            output1.write('\n')
            output1.close()
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)


stream = tweepy.Stream(auth, l)
stream.filter(track=['India'])