import os
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.manifold import TSNE
from sklearn.manifold import Isomap
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from matplotlib import offsetbox

#directory = './avatars'
directory = '/home/kayla/pylearn/manifold/cupcakes'

pics = []
data = pd.DataFrame()
count = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        # creating a object
        pics.append(Image.open(f))
        pics[count] = pics[count].resize((100,100))
        image = pd.Series(np.asarray(pics[count]).ravel())
        data = pd.concat([data,image.to_frame().T],ignore_index=True)
        count += 1

dims = np.asarray(pics[0]).shape
data = data.fillna(data.mean())

model = Isomap(n_components=10)
proj = model.fit_transform(data)

kmeans = KMeans(n_clusters=10)
kmeans.fit(proj)
clusters = kmeans.predict(proj)
data['cluster'] = clusters

#avg_data = data.groupby(by=['cluster']).sample().drop(['cluster'], \
#                        axis=1)
avg_data = data.groupby(by=['cluster']).median()
avg_image = []
for i in avg_data.index.astype('int'):
    avg_image.append(avg_data.loc[i].to_numpy().reshape(dims).astype('int'))
    
fig, ax = plt.subplots(2,5,figsize=(8,3))
for axi, img in zip(ax.flat, avg_image):
    axi.set(xticks=[],yticks=[])
    axi.imshow(img,interpolation='nearest')
plt.show()
