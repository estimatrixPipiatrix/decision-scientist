import torch
import numpy as np
import pandas as pd
import sys
import pickle

tweets = pd.read_csv('labeled_tweets.csv')

# convert each word into a number; covert each tweet into a
# vector with a predefined length. empty positions will be
# set to zero

# build up a set containing all the tweet words; also find the
# maximum tweet length
vocab = set()
max_len = 0
for i in range(tweets.shape[0]):
    word_list = tweets.iloc[i,0].split()
    if len(word_list)>max_len:
        max_len = len(word_list)
    vocab = vocab.union(set(word_list))

# make a dictionary pairing words to integers
words_to_nums = {word:index for index,word in enumerate(vocab)}

# save the dictionary to a file
with open('words_to_nums.pkl', 'wb') as fp:
    pickle.dump(words_to_nums, fp)
    print('dictionary saved to file!')

tweets_as_vecs = np.zeros((tweets.shape[0],max_len))
for i in range(tweets.shape[0]):
    word_list = tweets.iloc[i,0].split()
    tweet_vec = [words_to_nums[word] for word in word_list]
    tweets_as_vecs[i,0:len(tweet_vec)]=tweet_vec

tweets_as_vecs = pd.DataFrame(tweets_as_vecs)
tweets_as_vecs.to_csv('tweets_as_vecs.csv',index=False)

# convert the tweet_labels such that 0 = bad tweet, 
# 1 = good tweet, and there is a single integer label for each
# tweet
tweet_labels = tweets.iloc[:,1:3]
true_class = np.zeros((1,tweet_labels.shape[0]))
true_class = pd.Series(true_class.ravel())
for i in range(tweet_labels.shape[0]):
    true_class[i] = 1 - tweet_labels.iloc[i].argmax()
true_class = true_class.astype(int)
true_class.to_csv('tweet_labels.csv',index=False)
