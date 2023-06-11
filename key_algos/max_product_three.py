# return the maximum product of three numbers in a given input array

import numpy as np
import heapq

vec = np.array([-2,-4,5,3])

# method 1: sorting

def max_product_sort(vec):
    vec.sort()
    prod1 = vec[len(vec)-1]*vec[len(vec)-2]*vec[len(vec)-3]
    prod2 = vec[0]*vec[1]*vec[len(vec)-1]
    return max(prod1,prod2)

# method 2: heap
def max_product_heap(vec):
    max3 = np.array(heapq.nlargest(3,vec))
    max_num  = np.array(heapq.nlargest(1,vec))
    min2 = np.array(heapq.nsmallest(2,vec))
    prod1 = max3.prod()
    prod2 = max_num*min2.prod()
    return max(prod1,prod2[0])

print(max_product_sort(vec))
print(max_product_heap(vec))
