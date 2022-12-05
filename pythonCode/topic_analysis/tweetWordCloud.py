from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

tweets_df = pd.read_csv('my_tweets_cleaned.csv')

long_string = ','.join(list(tweets_df['Tweets'].values))
stopwords = set(STOPWORDS)
stopwords.update(["thing", "u", "https", "co", "t", "m", "one", "s", \
                  "know","want","things","like","would","think", \
                  "something","good","get","yeah","really","yes", \
                  "also","much","time","could","say","even","way", \
                  "need","guy","ok","bad","oh","make","seems", \
                  "well","fr","thanks","someone","tco","lot"])
wordcloud = WordCloud(stopwords=stopwords).generate(long_string)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
