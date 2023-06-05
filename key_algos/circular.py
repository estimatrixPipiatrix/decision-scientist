# find the maximum subarray sum for a circular array
# we perform kadane's algorithm twice: once on the ordinary
# non-circular array and again on the same array but to find
# the *minimum* subarray sum; then the max subarray sum is either
# the first max we found or the min sum subtracted from the sum
# of all other array values
import numpy as np

vec = np.array([5,-3,5])

cur_sum = 0.0
max_sum = vec[0]
for i in range(len(vec)):
    cur_sum += vec[i]
    if cur_sum < 0.0:
        cur_sum = 0
    if (cur_sum > max_sum):
        max_sum = cur_sum

cur_sum = 0.0
min_sum = vec[0]
for i in range(len(vec)):
    cur_sum += vec[i]
    if cur_sum > 0.0:
        cur_sum = 0
    if (cur_sum < min_sum):
        min_sum = cur_sum

max_sum_edge = vec.sum()-min_sum
print(np.max([max_sum_edge,max_sum]))
