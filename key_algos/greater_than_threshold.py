# Given an array of integers arr and two integers k and threshold, 
# return the number of sub-arrays of size k and average greater 
# than or equal to threshold
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 
# 4, 5 and 6 respectively. All other sub-arrays of size 3 have 
# averages less than 4 (the threshold)

import numpy as np

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

def avg_over_threshold(arr,k,threshold):
    arr = np.array(arr)
    left = 0
    right = left+k-1
    count = 0
    while right<len(arr):
        avg = arr[left:right+1].mean()
        if avg>=threshold:
            count += 1
        left += 1
        right += 1
    return count

print(avg_over_threshold(arr,k,threshold))
