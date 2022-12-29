import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

def plot_pixels(data,title,colors=None,N=10000):
    if colors is None:
        colors = data

    rng = np.random.RandomState(0)
    i = rng.permutation(data.shape[0])[:N]
    colors = colors[i]
    R, G, B = data[i].T

    fig, ax = plt.subplots(1,2,figsize=(16,6))
    ax[0].scatter(R,G,color=colors,marker='.')
    ax[0].set(xlabel='Red',ylabel='Green',xlim=(0,1), \
              ylim=(0,1))

    ax[1].scatter(R,B,color=colors,marker='.')
    ax[1].set(xlabel='Red',ylabel='Blue',xlim=(0,1), \
              ylim=(0,1))

    fig.suptitle(title,size=20)
