import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

model = make_pipeline(TfidfVectorizer(),MultinomialNB())

train  = pd.read_pickle('train_clean.csv')
test   = pd.read_pickle('test_clean.csv')
labels_train = pd.read_pickle('train_labels_clean.csv')

model.fit(train['review_text'],labels_train)
labels_pred = model.predict(test['review_text'])
labels_pred = pd.DataFrame(labels_pred,columns=['rating'])

labels_pred.to_pickle('labels_pred.csv')
