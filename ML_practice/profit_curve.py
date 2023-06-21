# we use the results from the naive-bayes predictor to generate
# profit curves for different classification thresholds

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

pred = pd.read_csv("bayes_pred.csv").to_numpy()
ytest = pd.read_csv("bayes_ytest.csv").to_numpy()

# set utilities associated with each square of the confusion
# matrix. a false positive is classifying a flimsy widget as 
# durable, and a false negative is classifying a durable widget as 
# flimsy. let's say each widget costs $10 to make and sells for 
# $30. for simplicity, let's say that all the durable widgets sell 
# but the flimsy ones get returned and lose $10 worth of bad 
# publicity. packaging and distribution costs $5, so correctly 
# identified flimsy widgets save us $5
true_pos = 15.0
true_neg = -10.0
false_pos = -25.0
false_neg = -10.0
utils = np.array([true_pos,true_neg,false_pos,false_neg])

# we also need to calculate the probabilities of each of these
# events according to our model and given a threshold
def confusion_square_probs(pred,ytest,threshold):
    true_pos = ((pred>threshold)&(ytest==1)).sum()/len(ytest)
    true_neg = ((pred<=threshold)&(ytest==0)).sum()/len(ytest)
    false_pos = ((pred>threshold)&(ytest==0)).sum()/len(ytest)
    false_neg = ((pred<=threshold)&(ytest==1)).sum()/len(ytest)
    return np.array([true_pos,true_neg,false_pos,false_neg])

# now we can use those probabilities together with the utilities
# to calculate expected value given a threshold
def expected_value(pred,ytest,utils,threshold):
    conf_probs = confusion_square_probs(pred,ytest,threshold)
    return np.dot(conf_probs,utils)

thresholds = np.linspace(0,1,100)
expected_vals = np.zeros(100)
for i,thresh in enumerate(thresholds):
    expected_vals[i] = expected_value(pred,ytest,utils,thresh)


plt.plot(thresholds,expected_vals)
plt.ylabel('expected value')
plt.xlabel('probability threshold')
plt.show()
