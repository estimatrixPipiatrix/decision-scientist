When machine learning algorithms are trained on data that has been labeled, in order to predict the labels for data that has not, they're called "supervised learning" algorithms; on the other hand, when they search for patterns in unlabeled data, in order to simplify it, they're called "unsupervised learning" algorithms. How might unsupervised learning algorithms, such as Isomap and K-means, categorize D&D monsters according to their stats alone? For example,  it group dragons together?

Let's have a look at the data:


```python
import pandas as pd

data = pd.read_json('srd_5e_monsters.json')
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>meta</th>
      <th>Armor Class</th>
      <th>Hit Points</th>
      <th>Speed</th>
      <th>STR</th>
      <th>STR_mod</th>
      <th>DEX</th>
      <th>DEX_mod</th>
      <th>CON</th>
      <th>...</th>
      <th>Challenge</th>
      <th>Traits</th>
      <th>Actions</th>
      <th>Legendary Actions</th>
      <th>img_url</th>
      <th>Damage Immunities</th>
      <th>Condition Immunities</th>
      <th>Damage Resistances</th>
      <th>Damage Vulnerabilities</th>
      <th>Reactions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Aboleth</td>
      <td>Large aberration, lawful evil</td>
      <td>17 (Natural Armor)</td>
      <td>135 (18d10 + 36)</td>
      <td>10 ft., swim 40 ft.</td>
      <td>21</td>
      <td>(+5)</td>
      <td>9</td>
      <td>(-1)</td>
      <td>15</td>
      <td>...</td>
      <td>10 (5,900 XP)</td>
      <td>&lt;p&gt;&lt;em&gt;&lt;strong&gt;Amphibious.&lt;/strong&gt;&lt;/em&gt; The a...</td>
      <td>&lt;p&gt;&lt;em&gt;&lt;strong&gt;Multiattack.&lt;/strong&gt;&lt;/em&gt; The ...</td>
      <td>&lt;p&gt;The aboleth can take 3 legendary actions, c...</td>
      <td>https://media-waterdeep.cursecdn.com/avatars/t...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Acolyte</td>
      <td>Medium humanoid, any</td>
      <td>10</td>
      <td>9 (2d8)</td>
      <td>30 ft.</td>
      <td>10</td>
      <td>(+0)</td>
      <td>10</td>
      <td>(+0)</td>
      <td>10</td>
      <td>...</td>
      <td>1/4 (50 XP)</td>
      <td>&lt;p&gt;&lt;em&gt;&lt;strong&gt;Spellcasting.&lt;/strong&gt;&lt;/em&gt; The...</td>
      <td>&lt;p&gt;&lt;em&gt;&lt;strong&gt;Club.&lt;/strong&gt;&lt;/em&gt; &lt;em&gt;Melee W...</td>
      <td>NaN</td>
      <td>https://media-waterdeep.cursecdn.com/attachmen...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Adult Black Dragon</td>
      <td>Huge dragon, chaotic evil</td>
      <td>19 (Natural Armor)</td>
      <td>195 (17d12 + 85)</td>
      <td>40 ft., fly 80 ft., swim 40 ft.</td>
      <td>23</td>
      <td>(+6)</td>
      <td>14</td>
      <td>(+2)</td>
      <td>21</td>
      <td>...</td>
      <td>14 (11,500 XP)</td>
      <td>&lt;p&gt;&lt;em&gt;&lt;strong&gt;Amphibious.&lt;/strong&gt;&lt;/em&gt; The d...</td>
      <td>&lt;p&gt;&lt;em&gt;&lt;strong&gt;Multiattack.&lt;/strong&gt;&lt;/em&gt; The ...</td>
      <td>&lt;p&gt;The dragon can take 3 legendary actions, ch...</td>
      <td>https://media-waterdeep.cursecdn.com/avatars/t...</td>
      <td>Acid</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Adult Blue Dragon</td>
      <td>Huge dragon, lawful evil</td>
      <td>19 (Natural Armor)</td>
      <td>225 (18d12 + 108)</td>
      <td>40 ft., burrow 30 ft., fly 80 ft.</td>
      <td>25</td>
      <td>(+7)</td>
      <td>10</td>
      <td>(+0)</td>
      <td>23</td>
      <td>...</td>
      <td>16 (15,000 XP)</td>
      <td>&lt;p&gt;&lt;em&gt;&lt;strong&gt;Legendary Resistance (3/Day).&lt;/...</td>
      <td>&lt;p&gt;&lt;em&gt;&lt;strong&gt;Multiattack.&lt;/strong&gt;&lt;/em&gt; The ...</td>
      <td>&lt;p&gt;The dragon can take 3 legendary actions, ch...</td>
      <td>https://media-waterdeep.cursecdn.com/avatars/t...</td>
      <td>Lightning</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Adult Brass Dragon</td>
      <td>Huge dragon, chaotic good</td>
      <td>18 (Natural Armor)</td>
      <td>172 (15d12 + 75)</td>
      <td>40 ft., burrow 30 ft., fly 80 ft.</td>
      <td>23</td>
      <td>(+6)</td>
      <td>10</td>
      <td>(+0)</td>
      <td>21</td>
      <td>...</td>
      <td>13 (10,000 XP)</td>
      <td>&lt;p&gt;&lt;em&gt;&lt;strong&gt;Legendary Resistance (3/Day).&lt;/...</td>
      <td>&lt;p&gt;&lt;em&gt;&lt;strong&gt;Multiattack.&lt;/strong&gt;&lt;/em&gt; The ...</td>
      <td>&lt;p&gt;The dragon can take 3 legendary actions, ch...</td>
      <td>https://media-waterdeep.cursecdn.com/avatars/t...</td>
      <td>Fire</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows ?? 31 columns</p>
</div>



There's a lot of information here, and it will need to be converted into fully numerical form before PCA and K-means can act on it. Also, there's a columns that includes urls for images of nearly all of the monsters; we'd like to use those in presenting our results. I've already run a script that downloads those images and turns them into thumbnails, so we just need to clean the data. 

We start by eliminating the rows for monsters that don't have corresponding images as well as columns that have NaN values, and creating a separate column to keep track of the row numbers identifying each monster. (The image files have these same numbers as suffixes, and it will be important to keep track of which row goes with which image file.)


```python
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer

data['monster num'] = data.index
rows_to_keep = pd.read_csv('rows_to_keep.csv')
data = data.iloc[rows_to_keep['keep']]
data = data.dropna(axis=1).reset_index(drop=True)
data = data.drop('img_url',axis=1)
```

Next we clean up the columns with numerical data (e.g., for the modifiers we need to have entries like "1" and not "(+1)") and vectorize the columns with linguistic data.


```python
for i in range(data.shape[0]):
    data.loc[i,'Hit Points'] =int(re.search(r"(\d+)", \
                              data.loc[i]['Hit Points']).group())
    data.loc[i,'Challenge']  =int(re.search(r"(\d+)", \
                              data.loc[i]['Challenge']).group())
    data.loc[i,'Armor Class']=int(re.search(r"(\d+)", \
                              data.loc[i]['Armor Class']).group())
    data.loc[i,'Speed']      =int(re.search(r"(\d+)", \
                              data.loc[i]['Speed']).group())
    data.loc[i,'STR_mod']    =int(re.search(r"(\d+)", \
                              data.loc[i]['STR_mod']).group())
    data.loc[i,'DEX_mod']    =int(re.search(r"(\d+)", \
                              data.loc[i]['DEX_mod']).group())
    data.loc[i,'CON_mod']    =int(re.search(r"(\d+)", \
                              data.loc[i]['CON_mod']).group())
    data.loc[i,'CHA_mod']    =int(re.search(r"(\d+)", \
                              data.loc[i]['CHA_mod']).group())
    data.loc[i,'INT_mod']    =int(re.search(r"(\d+)", \
                              data.loc[i]['INT_mod']).group())
    data.loc[i,'WIS_mod']    =int(re.search(r"(\d+)", \
                              data.loc[i]['WIS_mod']).group())

vec = CountVectorizer()
langs = vec.fit_transform(data['Languages'])
langs = pd.DataFrame(langs.toarray(), \
                     columns=vec.get_feature_names_out())
data = data.drop(['Languages'],axis=1)

meta = vec.fit_transform(data['meta'])
meta = pd.DataFrame(meta.toarray(), \
                    columns=vec.get_feature_names_out())
data = data.drop(['meta'],axis=1)

senses = vec.fit_transform(data['Senses'])
senses = pd.DataFrame(senses.toarray(), \
                      columns=vec.get_feature_names_out())
data = data.drop(['Senses'],axis=1)

data = pd.concat((data,langs,meta,senses),axis=1)
```

Now that the data is cleaned, we store the monster number and name is a separate data frame and drop the "Challenge" column because we don't want the monster challenge rating to dominate the resulting categorization. Next, we rescale the data so that, e.g., hit points don't dominate simply because they are on a larger numerical scale than the other attributes.


```python
from sklearn.preprocessing import StandardScaler

X = data.drop(['name','monster num','Challenge'],axis=1)
names = data[['name','monster num']]

scaler = StandardScaler()
X = scaler.fit_transform(X)
```

Now we can apply Isomap to reduce the dimensionality of the space before applying K-means.


```python
from sklearn.manifold import Isomap
from sklearn.cluster import SpectralClustering

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
```

We have re-indexed X_iso above by monster number for plotting the results, with which we now proceed.


```python
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from matplotlib import offsetbox
from PIL import Image
import os

%matplotlib inline

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
```


    
![png](output_12_0.png)
    


The circles underlying the thumbnail images have been color-labeled and sorted into 5 groups via K-means; we see that, e.g., the dragons have indeed been placed together, as have mostly the undead and the celestials. Isomap and K-means have done a decent job of collecting like monsters with like, with knowledge only of the stats and not including the challenge rating.


```python

```
