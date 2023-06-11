# given two arrays, find the indices of numbers such that, when the
# arrays trade those two numbers, the sum of each array equals the
# sum of the other one; if there's more than one solution just return 
# one of them

import numpy as np
vec1 = np.array([7,5,4,3,1,0])
vec2 = np.array([1,0,4,2,5])

def sum_swap_indices(vec1,vec2):
    sum1 = vec1.sum()
    sum2 = vec2.sum()
    avg_sum = (sum1+sum2)/2
    shift = np.abs(avg_sum-sum1)

    complements = {}
    for i,n in enumerate(vec1):
        complements.update({n-shift:i})
    for j,m in enumerate(vec2):
        if complements.get(m)!=None:
            return [complements[m],j]
    return None

print(sum_swap_indices(vec1,vec2))
