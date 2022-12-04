from wordcloud import WordCloud
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

tweets_df = pd.read_csv('my_tweets_cleaned.csv')

long_string = ','.join(list(tweets_df['Tweets'].values))
stopwords = set(STOPWORDS)
stopwords.update(["thing", "u", "https", "co", "t", "m", "one", "s", \
                  "know","want","things"])
wordcloud = WordCloud(stopwords=stopwords).generate(long_string)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
