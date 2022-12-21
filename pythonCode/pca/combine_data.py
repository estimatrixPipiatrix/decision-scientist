import pandas as pd

data_frames = {}
for i in range(1950,2011,10):
    data_frames[i] = pd.read_csv(str(i)+'.csv')
    data_frames[i] = data_frames[i].drop(['Number'],axis=1)

all_data = pd.concat([data_frames[i]  \
    for i in range(1950,2011,10)])

all_data.to_csv('all_years.csv',index=False)
