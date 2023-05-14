import pandas as pd

tweets = pd.read_csv("my_tweets_cleaned.csv")

threshold = 3
good_tweets = (tweets['Number of Likes']>threshold).astype(int)
bad_tweets  = (tweets['Number of Likes']<=threshold).astype(int)

tweets.drop(['Number of Likes'],axis=1,inplace=True)
tweets['good'] = good_tweets
tweets['bad']  = bad_tweets

tweets.to_csv('labeled_tweets.csv',index=False)
