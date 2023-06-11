# compute the greatest product from multiplying two numbers in
# a given array that may contain negative numbers; the algo should
# have O(N)

import numpy as np

def two_largest(nums):
    largest = -np.inf
    second_largest = -np.inf
    for i,n in enumerate(nums):
        if n>largest:
            largest = n
            ind = i
    for i,n in enumerate(nums):
        if n>second_largest and i!=ind:
            second_largest = n
    return largest,second_largest

def two_smallest(nums):
    smallest = np.inf
    second_smallest = np.inf
    for i,n in enumerate(nums):
        if n<smallest:
            smallest = n
            ind = i
    for i,n in enumerate(nums):
        if n<second_smallest and i!=ind:
            second_smallest = n
    return smallest,second_smallest

def greatest_prod(nums):
    largest,second_largest = two_largest(nums)
    smallest,second_smallest = two_smallest(nums)
    prod1 = largest*second_largest
    prod2 = smallest*second_smallest
    return max(prod1,prod2)

def greatest_prod_brute(nums):
    greatest = -np.inf
    for i,n in enumerate(nums):
        for j,m in enumerate(nums):
            if i!=j:
                if m*n>greatest:
                    greatest = m*n 
    return greatest          

np.random.seed(2)
for i in range(100):
    length = np.random.randint(2,5)
    nums = np.random.randint(-10,10,size=length)
    ans1 = greatest_prod(nums)
    ans2 = greatest_prod_brute(nums)
    if ans1!=ans2:
        print('answer mismatch')
        print(nums,ans1,ans2)
