# given a list of positive integers, return the maximum increasing
# subsequence sum. in other words, return the sum of the largest 
# increasing subsequence within the input array. for example,
# if the input is [3,2,5,7,6], return 15 because it's the sum of
# 3,5,7; if the input is [5,4,3,2,1], return 5 (since no subsequence 
# is increasing)

def max_increasing_seq(vec):
    # max_hash will contain {i:max_sum} where max_sum is the 
    # maximum increasing subsequence sum up to index i that
    # includes the number at index i as part of the sum
    max_sum = {}
    for i in range(len(vec)):
        # we start off assuming that the max sum up to each
        # position is just the element at that position and
        # correct these starting amounts as we go
        max_sum.update({i:vec[i]})
    for i in range(len(vec)):
        for j in range(i):
            if vec[i]>vec[j] and vec[i]+max_sum[j]>max_sum[i]:
                max_sum[i] = vec[i]+max_sum[j]
    keys = list(max_sum.keys())
    max_result = 0
    for key in keys:
        curr = max_sum[key]
        if (curr>max_result):
            max_result = curr
    return max_result

#import sys
#vec = [1,4,2,3,1]
#print(max_increasing_seq(vec))
#sys.exit()

import numpy as np
for i in range(100):
    length = np.random.randint(1,10)
    vec = np.random.randint(0,10,size=length)
    ans = max_increasing_seq(vec)
    print(vec,ans)
