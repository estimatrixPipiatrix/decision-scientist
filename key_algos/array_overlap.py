import numpy as np
# find the largest contiguous overlapping subarray

vec1 = np.array([0,5,-1,-2,6,4,7,-3])
vec2 = np.array([0,6,4,7,9,2,0,5])

max_start  = 0
max_length = 0
for i in range(len(vec1)):
    start = i
    for k in range(len(vec2)):
        if vec2[k]==vec1[start]:
            j = k
            length = 0
            while (vec2[j]==vec1[min(i+length,len(vec1)-1)] \
                  and (j<len(vec2)-1)):
                length += 1
                j += 1
        if length>max_length:
             max_length = length
             max_start  = start

print(max_start,max_length)
