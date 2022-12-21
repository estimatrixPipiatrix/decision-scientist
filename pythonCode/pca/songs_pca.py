import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.decomposition import PCA

songs = pd.read_csv('all_years.csv')
pca = PCA()

X = songs.drop(['title','artist','top genre'],axis=1)

pca.fit(X)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('number of components (minus 1)')
plt.ylabel('cumulative explained variance')
# we see that 70% of the variance is explained by 2
# principal components

pca = PCA(0.70)
pca.fit(X)
X_pca = pd.DataFrame(pca.transform(X))
X_pca['genre'] = songs['top genre']

genre_pca = X_pca.groupby(by=['genre']).mean()

plt.scatter(X_pca.iloc[:,0],X_pca.iloc[:,1],s=10, \
            c=songs['pop'])
plt.xlabel('pca0')
plt.ylabel('pca1')
plt.colorbar()
plt.show()
# the most popular songs lie between pca0=-50 and pca0=100,
# while the least popular lie between pca0=-150 and pca0=-50
