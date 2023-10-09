import numpy as np
import pandas as pd
from sklearn import tree
import graphviz
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import ConfusionMatrixDisplay,accuracy_score
import seaborn as sns; sns.set()

part_data = pd.read_csv('part_data.csv')
X = part_data.iloc[:,0:6]
y = part_data.iloc[:,7]

max_depth = 1
max_depth_best = 1
max_max_depth = 10
best_score = -np.inf
for i in range(max_max_depth):
    Xtrain,Xtest,ytrain,ytest = train_test_split(X,y)
    model = DecisionTreeClassifier(max_depth=max_depth)
    scores = cross_val_score(estimator=model, \
                             X = Xtrain, \
                             y = ytrain, \
                             cv = 10,     \
                             n_jobs = 3)
    mean_score = scores.mean()
    if mean_score>best_score:
        best_score = mean_score
        max_depth_best = max_depth
    max_depth += 1

print('best model has depth: ',max_depth_best)
print('with avg val score: ',best_score)

#max_depth_best = 2
model = DecisionTreeClassifier(max_depth=max_depth_best)
model.fit(Xtrain,ytrain)

# plot decision tree
dot_data = tree.export_graphviz(model, out_file=None,
                                feature_names=X.columns,
                                filled=True,rounded=True,class_names=True)
graph = graphviz.Source(dot_data, format="png")
graph.render("decision_tree_graphviz")
img = mpimg.imread('decision_tree_graphviz.png')
plt.rcParams["figure.autolayout"] = True
plt.axis('off')
plt.imshow(img)
plt.show()

ypred = model.predict(Xtest)
accuracy = accuracy_score(ypred,ytest)
print('percent accurate OOS: ',accuracy*100.0)
disp = ConfusionMatrixDisplay.from_estimator(model,Xtest,ytest)
plt.grid(False)
plt.show()
