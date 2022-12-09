import pandas as pd
import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

labels_pred = pd.read_pickle('labels_pred.csv')
labels_test = pd.read_pickle('test_labels_clean.csv')

print('accuracy score: ',accuracy_score(labels_pred, \
                                        labels_test))

mat = confusion_matrix(labels_test,labels_pred)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', \
            cbar=False,xticklabels=['bad','good'], \
            yticklabels=['bad','good'])
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()
