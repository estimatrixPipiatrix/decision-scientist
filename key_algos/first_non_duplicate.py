# returns the first non-duplicated character in a string, and 
# do so with O(N)
import numpy as np
import pandas as pd

my_string = 'iimumnu'

chars = {}
for n in my_string:
    chars.update({n:True})

counts = np.zeros((1,len(chars)))
counts = pd.DataFrame(counts,columns=chars)
for n in my_string:
    if chars.get(n):
        counts[n] += 1

i = 0
flag = 0
while ((flag==0) and (i<counts.shape[1])):
    if counts.iloc[0,i]==1.0:
        flag = 1
    i += 1

if flag != 0:
    print(counts.columns[i-1])
else:
    print('no solution')
