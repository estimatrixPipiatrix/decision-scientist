from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import pandas as pd

mushrooms = pd.read_csv('mushrooms_clean.csv')

model = SVC(kernel='rbf',C=1000)

y = mushrooms['class']
#X = mushrooms.drop(['class'],axis=1)
X = mushrooms[['cap-shape','cap-surface','cap-color','gill-color']]
#X = mushrooms[['cap-shape','cap-surface']]
X_train, X_test, y_train, y_test = \
        train_test_split(X,y,train_size=0.5)

model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('accuracy score: ',accuracy_score(y_test,y_pred))

mat = confusion_matrix(y_test,y_pred)
sns.heatmap(mat.T, square=True,annot=True, \
            xticklabels=['edible','poisonous'], \
            yticklabels=['edible','poisonous'])
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()
