import torch
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tweet_classifier import tweet_classifier
import torch.nn as nn
from torch import optim
import sys

tweets = pd.read_csv("tweets_as_vecs.csv")
labels = pd.read_csv("tweet_labels.csv")

# create the training and test sets
X_train, X_test, y_train, y_test = \
    train_test_split(tweets,labels,test_size=0.33)

X_train = np.array(X_train)
X_test  = np.array(X_test)
y_train = np.array(y_train)
y_test  = np.array(y_test)
X_train = torch.tensor(X_train)
X_test  = torch.tensor(X_test)
y_train = torch.tensor(y_train)
y_test  = torch.tensor(y_test)

batch_size = 20
vec_dim = 100
sent_len = X_train.shape[1]
num_heads = 4
depth = 3
seq_length = sent_len
num_words = int(tweets.max().max())+1
num_classes = 2
learning_rate = 0.1
err_tol = 0.1
max_epoch = 1000
epoch = 0
err = 1.e5
X_train = X_train.view(batch_size,int(X_train.shape[0]/batch_size), \
                       X_train.shape[1]).int()
y_train = y_train.view(batch_size,int(y_train.shape[0]/batch_size))
model = tweet_classifier(vec_dim,num_heads,depth,seq_length, \
                         num_words,num_classes)
loss_func = nn.NLLLoss()
optimizer = optim.SGD(model.parameters(),learning_rate)
while ((epoch<max_epoch)&(err>err_tol)):
    err = 0.0
    for i in range(batch_size):
        outputs = model(X_train[i])
        targets = y_train[i]
        loss = loss_func(outputs,targets)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        err += loss.item()

    err /= batch_size
    epoch += 1
    if (epoch%10==0):
        print("epoch: %d, loss: %f" % (epoch, err))

if (epoch<=max_epoch):
    print("converged at epoch: ",epoch)
    print("with error: ",err)

torch.save(model.state_dict(), 'model_weights.pth')
torch.save(X_test,"X_test.pt")
torch.save(y_test,"y_test.pt")
