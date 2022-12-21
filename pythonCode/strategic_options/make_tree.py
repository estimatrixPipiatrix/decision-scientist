import pandas as pd
import numpy as np
from itertools import product

area1 = pd.read_csv('area1.csv')
area2 = pd.read_csv('area2.csv')
area3 = pd.read_csv('area3.csv')
block = pd.read_csv('block.csv')

combos = list(product(area1['area 1'],area2['area 2'], \
                      area3['area 3']))

combos = pd.DataFrame(combos,columns=['area 1', \
                      'area 2','area 3'])

for i in range(block.shape[0]):
    nogo = combos.isin([block.iloc[i][0]]).any(axis=1) & \
           combos.isin([block.iloc[i][1]]).any(axis=1)
    combos[i] = nogo

combos['possible'] = ~(combos[0] | combos[1] | combos[2])
combos = combos.drop([0,1,2],axis=1)

options = pd.DataFrame(combos[combos['possible']==True])
options = options.drop(['possible'],axis=1)

options.to_csv('options.csv',index=False)
