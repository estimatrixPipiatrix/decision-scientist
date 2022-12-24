import os
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.manifold import Isomap
from matplotlib import offsetbox

from isomap_plot import *

directory = './cupcakes'

pics = []
data = pd.DataFrame()
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        # creating a object
        pics.append(Image.open(f))
        image = pd.Series(np.asarray(Image.open(f)).ravel())
        data = pd.concat([data,image.to_frame().T],ignore_index=True)

data = data.fillna(0)

# have a look at the cupcake thumbnails
#fig, ax = plt.subplots(6,10,subplot_kw={'xticks':[],'yticks':[]})
#for i, axi in enumerate(ax.flat):
#    axi.imshow(pics[i])
#plt.show()

model = Isomap(n_components=2)
proj = model.fit_transform(data)

def plot_components(data, model, images=None, ax=None,
                    cmap='gray'):
    ax = ax or plt.gca()

    proj = model.fit_transform(data)
    ax.plot(proj[:,0],proj[:,1],'.k')

    if images is not None:
        for i in range(data.shape[0]):
            imagebox = offsetbox.AnnotationBbox( \
                offsetbox.OffsetImage(images[i],cmap=cmap, \
                                      zoom=0.5), \
                                      proj[i])
            ax.add_artist(imagebox)

fig, ax = plt.subplots(figsize=(10,50))
plot_components(data,model=Isomap(n_components=2), \
                images=pics)

#plt.scatter(proj[:,0],proj[:,1],s=20,alpha=0.5)
plt.show()
