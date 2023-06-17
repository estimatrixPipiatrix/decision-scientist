import numpy as np
import pandas as pd

# we seek to produce widget data that looks like this sample
#i round,source,size,material,durability
# 0,1,0,1,1
# 1,1,0,1,1
# 1,1,0,1,1
# etc,
# where round and material are at first equal to durability but
# then with noise added, so that they only correlate

num_rows = 10000
num_cols = 5
widget_data = np.zeros((num_rows,num_cols))
columns = ['round','source','size','material','durability']
widget_data = pd.DataFrame(widget_data,columns=columns)

frac_durable = 0.63
widget_data.loc[0:int(0.63*num_rows),'durability']=1
widget_data.loc[0:int(0.63*num_rows),'round']=1
widget_data.loc[0:int(0.63*num_rows),'material']=1

# add in random variability
widget_data['source'] = np.random.randint(0,2,num_rows)
widget_data['size'] = np.random.randint(0,2,num_rows)
mask_1 = np.random.randint(0,2,num_rows)
mask_2 = np.random.randint(0,2,num_rows)
widget_data['round'] = widget_data['round']*mask_1+mask_1
widget_data['material'] = widget_data['material']*mask_2+mask_2
widget_data[widget_data['round']==2]=1.0
widget_data[widget_data['material']==2]=1.0
widget_data = widget_data.astype('int')

widget_data.to_csv("widget_data.csv",index=None)
