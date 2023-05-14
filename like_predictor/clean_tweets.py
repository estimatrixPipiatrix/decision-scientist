import pandas as pd
import re
import sys

tweets_df = pd.read_csv("my_tweets.csv")

#remove all columns except those containing tweets
tweets_df = tweets_df.drop(columns=['Date Created', \
            'Source of Tweet'],axis=1).sample(4000)
tweets_df.drop(['Unnamed: 0'],axis=1,inplace=True)

# remove punctuation
tweets_df['Tweets'] = \
    tweets_df['Tweets'].map(lambda x: \
    re.sub('[,\.!?]','', x))

# remove all the mentions (@)
tweets_df['Tweets'] = \
    tweets_df['Tweets'].map(lambda x: \
    re.sub('@([a-zA-Z0-9_]{1,50})', '', x))

# convert the titles to lowercase
tweets_df['Tweets'] = \
    tweets_df['Tweets'].map(lambda x: x.lower())

tweets_df.to_csv("my_tweets_cleaned.csv",index=False)
