import numpy as np

vec = np.array([9,-2,6,-1,0,4,5,2,3,3,8])

for i in range(len(vec)-1):
    tmp = vec[i+1]
    last_shift = -1
    inner_count = 0
    for j in range(i,-1,-1):
        if vec[j]>tmp:
            vec[i+1-inner_count]=vec[j]
            inner_count += 1
            last_shift = j

    if last_shift>=0:
        vec[last_shift]=tmp

print(vec)
