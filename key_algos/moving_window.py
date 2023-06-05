# find the minimum length of the subarray whose values sum
# to a value greater than or equal to a target. assume all
# array entries are positive
import numpy as np

vec = np.array([2,3,1,2,4,3])
target = 7

L=0
R=0
min_length = np.inf
cur_length = np.inf
cur_sum = 0
for R,n in enumerate(vec):
    cur_sum += n
    while cur_sum>=target:
        cur_length = R-L+1
        cur_sum -= vec[L]
        L += 1
    if (cur_length<min_length):
        min_length=cur_length

if (min_length==np.inf):
    print(0)
else:
    print(min_length)
