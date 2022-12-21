import subprocess
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LassoCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.utils import resample
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

subprocess.Popen("./extract_data.sh",shell=True)
data = pd.read_csv('Tornadoes_SPC_1950to2015.csv')

y = data['mag']
X_pre = pd.DataFrame(columns=['len', 'wid'])
X_pre['len'] = data.fillna(method='pad')['len']
X_pre['wid'] = data.fillna(method='pad')['wid']

poly = PolynomialFeatures(3,include_bias=False)
X = poly.fit_transform(X_pre)
scaler = StandardScaler().fit(X)
X = scaler.transform(X)
X = pd.DataFrame(X)
X.columns = poly.get_feature_names_out()

X_train,X_test,y_train,y_test = train_test_split(X,y,\
                                train_size=0.9)
model = LassoCV(max_iter=10000,tol=0.01)
#model = Lasso(max_iter=10000,tol=0.01,alpha=0.1)
#model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

# get coefficients together with uncertainties
params = pd.Series(model.coef_, \
                   index=poly.get_feature_names_out())
err = np.std([model.fit(*resample(X_train,y_train)).coef_
             for i in range(100)],0)

# print results
print(pd.DataFrame({'effect': params,
                    'error': err}))
#sourceFile = open('tornado_reg_results.txt', 'w')
#print(pd.DataFrame({'effect':params,
#                    'error': err}),file=sourceFile)
#sourceFile.close()

print('r2_score: ',r2_score(y_test,y_pred))

X = scaler.inverse_transform(X)
X = pd.DataFrame(X,columns=poly.get_feature_names_out())
X_train = scaler.inverse_transform(X_train)
X_train = pd.DataFrame(X_train, \
                       columns=poly.get_feature_names_out())
X_test = scaler.inverse_transform(X_test)
X_test = pd.DataFrame(X_test, \
                      columns=poly.get_feature_names_out())

y_pred = y_pred.astype('int')

plt.scatter(X_test['len'],X_test['wid'],s=50*y_test,alpha=0.2, \
            label='data')
plt.scatter(X_test['len'],X_test['wid'],s=50*y_pred,alpha=0.2, \
            label='pred')
plt.xlabel('track length (mi)')
plt.ylabel('track width (yard)')
plt.legend(loc='upper right')
plt.show()
