# given an array of integers nums and an integer k, return the 
# total number of subarrays whose sum equals to k
# a subarray is a contiguous non-empty sequence of elements 
# within an array
# example 1:
# input: nums = [1,1,1], k = 2
# output: 2
# example 2:
# input: nums = [1,2,3], k = 3
# output: 2

# idea: let p be the prefix sum array of nums. then we want all 
# the subarrays such that p[right]-p[left-1]=k, which is the same
# as p[left-1]=p[right]-k, so we can make an array of p[right]-k
# and count off every time that equals an element of the prefix
# array

nums = [1,2,3]
k = 3
#nums = [1,1,1]
#k = 2

def num_subarrays_k(nums,k):
    prefix = []
    prefix_minus_k = []
    total = 0
    seen = {}
    count = 0
    for i in range(len(nums)):
        total += nums[i]
        prefix.append(total)
        if seen.get(prefix[i])==None:
            seen.update({prefix[i]:1})
        else:
            seen[prefix[i]] += 1
        prefix_minus_k.append(prefix[i]-k)
        if seen.get(prefix_minus_k[i])!=None:
            count += seen[prefix_minus_k[i]]
        if prefix[i]==k:
            count += 1

    #print(seen)
    #print('nums:',nums)
    #print('prefix:', prefix)
    #print('prefix_minus_k:', prefix_minus_k)
    return count

def num_subarrays_k_brute(nums,k):
    left = 0
    count = 0
    while left<len(nums):
        right = left
        curr_sum = 0
        while right<len(nums):
            curr_sum += nums[right]
            if curr_sum==k:
                #print(left,right)
                count += 1
            right += 1
        left += 1
    return count

import sys

#nums = [-5,  0,  5, -7,  4]
#k = 2
#print(num_subarrays_k(nums,k))
#print(num_subarrays_k_brute(nums,k))
#sys.exit()

import numpy as np
#np.random.seed(1)
for i in range(1000):
    k = np.random.randint(1,4)
    nums_len = np.random.randint(10)
    nums = np.random.randint(-10,10,size=nums_len)
    method_1 = num_subarrays_k(nums,k)
    method_2 = num_subarrays_k_brute(nums,k)
    if method_1 != method_2:
        print(method_1,method_2)
        print(nums,k)
