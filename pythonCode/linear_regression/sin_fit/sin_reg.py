# practice problem attempting to recover a sin function
import numpy as np
import pandas as pd
from sklearn.linear_model import LassoCV
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score
from sklearn.utils import resample
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

num_rows = 1000
mat  = np.zeros((num_rows,1))
y    = np.zeros((num_rows,1))
x    = 10*np.random.rand(num_rows)
y    = np.sin(x) + 0.5*np.random.randn(num_rows)

X_pre = pd.DataFrame(x)
y = pd.DataFrame(y)

poly = PolynomialFeatures(7,include_bias=False)
X = poly.fit_transform(X_pre)
scaler = StandardScaler().fit(X)
X = scaler.transform(X)
X = pd.DataFrame(X)

X_train, X_test, y_train, y_test = \
        train_test_split(X,y,train_size=0.9)

model = LinearRegression()
model.fit(X_train,np.ravel(y_train))
y_pred = model.predict(X_test)
print('r2_score:', r2_score(y_test,y_pred))

# get coefficients together with uncertainties
params = pd.Series(model.coef_.ravel())
err = \
    np.std([model.fit(*resample(X_train, \
    np.ravel(y_train))).coef_ 
    for i in range(100)],0)

# print results
sourceFile = open('sin_regression_results.txt', 'w')
print(pd.DataFrame({'effect':params,
                    'error': err.ravel()}), \
                    file=sourceFile)
sourceFile.close()

plt.scatter(X.iloc[:,0],y,c='k',alpha=0.6)
plt.scatter(X_test.iloc[:,0],y_pred,c='r',alpha=0.8)
plt.show()
