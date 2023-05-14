import torch
import pandas as pd
from tweet_classifier import tweet_classifier
import sys

tweets = pd.read_csv("tweets_as_vecs.csv")
X_test = torch.load("X_test.pt").int()
y_test = torch.load("y_test.pt")
num_sents = y_test.shape[0]

batch_size = 20
vec_dim = 100
sent_len = X_test.shape[1]
num_heads = 4
depth = 3
seq_length = sent_len
num_words = int(tweets.max().max())+1
num_classes = 2
model = tweet_classifier(vec_dim,num_heads,depth,seq_length, \
                         num_words,num_classes)
model.load_state_dict(torch.load('model_weights.pth'))
X_test = X_test.view(batch_size,int(X_test.shape[0]/batch_size), \
                     X_test.shape[1]).int()
y_test = y_test.view(batch_size,int(y_test.shape[0]/batch_size))
num_correct = 0
for i in range(batch_size):
    outputs = model(X_test[i])
    outputs = torch.exp(outputs).round().int().argmax(axis=1)

    targets = y_test[i]
    num_correct += (outputs==targets).sum().item()
    print(i)

frac_correct = num_correct/num_sents
print("percent correct OOS: ",frac_correct*100)
