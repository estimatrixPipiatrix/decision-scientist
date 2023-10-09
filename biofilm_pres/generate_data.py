import pandas as pd
import numpy as np
import random

random.seed(1)
np.random.seed(1)

# List of part options
part_options = [
    'pump type', 'filter type', 'maintenance schedule',
    'backwash frequency', 'gradient strength', 'chemical flush', 
    'daily op hours'
]

num_rows = 2633

# Create synthetic data
data = []
for _ in range(num_rows):
    part = \
        [random.choice([1, 0]) \
            for _ in range(len(part_options))]
    data.append(part)
data = np.array(data)

longevity = np.zeros(num_rows)
for i in range(num_rows):
    longevity[i] = 0.4*data[i,0]+0.12*data[i,2]+ \
                          0.3*data[i,3]+0.18*data[i,6]
    random_factor = np.random.randint(0,2)
    longevity[i] += \
        (4.0*longevity[i]+1.0) + \
        random_factor*np.random.randint(0,2)
    longevity[i] = longevity[i].round()
    longevity[i] = np.min([longevity[i],5])
longevity = longevity.astype('int')

df = pd.DataFrame(data, columns=part_options)
df['longevity'] = longevity

df.to_csv('part_data.csv',index=False)
