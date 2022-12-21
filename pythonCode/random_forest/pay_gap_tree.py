import pandas as pd
import graphviz
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

pay_gap = pd.read_csv('pay_gap_cleaned.csv')
y = pay_gap['hrwage']
X = pay_gap.drop(['hrwage'],axis=1)

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,train_size=0.5)
model = RandomForestRegressor(max_depth=3)
model.fit(Xtrain,ytrain)
ypred = model.predict(Xtest)
print('r2_score: ',r2_score(ytest,ypred))

estimator = model.estimators_[5]

dot_data = tree.export_graphviz(estimator, out_file=None,
                                feature_names=X.columns,
                                filled=True,rounded=True)

graph = graphviz.Source(dot_data, format="png")
graph.render("decision_tree_graphviz")
img = mpimg.imread('decision_tree_graphviz.png')
plt.axis('off')
plt.imshow(img)
plt.show()
