import pandas as pd
import numpy as np
import os
import re
from PIL import Image
from sklearn.manifold import Isomap
from sklearn.cluster import SpectralClustering
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from matplotlib import offsetbox

data = pd.read_csv('monsters_cleaned.csv')
X = data.drop(['name','monster num','Challenge'],axis=1)
names = data[['name','monster num']]

scaler = StandardScaler()
X = scaler.fit_transform(X)
model = Isomap(n_neighbors=7)
model.fit(X)

X_iso = pd.DataFrame(model.fit_transform(X),index=data.index)
X_iso['monster num'] = data['monster num']
X_iso = X_iso.set_index('monster num')

kmeans = SpectralClustering(n_clusters=5, \
                            affinity='nearest_neighbors',
                            assign_labels='kmeans')
kmeans.fit(X_iso)
labels = kmeans.fit_predict(X_iso)

iso_x = 0
iso_y = 1
fig, ax = plt.subplots()
fig.set_size_inches(18, 10)
im = ax.scatter(X_iso.loc[:][iso_x],X_iso.loc[:][iso_y],s=2500, \
                c=labels,cmap='Accent')
#fig.colorbar(im)

# load the monster images and plot them on top of the data
# points
directory = './monster_img'

pics = []
file_nums = np.arange(400)
for filename in os.listdir(directory):
    # strip the number off the file name
    img_id = re.search(r"(\d+)", filename).group()
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        pics.append([int(img_id),Image.open(f)])
images = pd.DataFrame(pics,columns=['monster num','jpeg'])
images = images.join(names.set_index('monster num'),on='monster num')
names = images['name']

def plot_components(X_iso, images, ax):
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.6)
    for i in range(images.shape[0]):
        num = images['monster num'][i]
        coords = [X_iso.loc[num][iso_x],X_iso.loc[num][iso_y]]
        imagebox = offsetbox.AnnotationBbox( \
            offsetbox.OffsetImage( \
            images.set_index('monster num').loc[num][0], \
            cmap='gray', \
            zoom=0.35),coords)
        ax.add_artist(imagebox)
        ax.text(X_iso.loc[num][iso_x],X_iso.loc[num][iso_y], \
                names[i], \
                bbox=props)
    ax.set_xlabel('iso '+str(iso_x))
    ax.set_ylabel('iso '+str(iso_y))

plot_components(X_iso,images,ax)
plt.show()
