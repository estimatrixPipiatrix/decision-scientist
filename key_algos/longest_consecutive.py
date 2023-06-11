# create an O(N) function that returns the length of the longest
# sequence of consecutively increasing integers in a given input
# array. the integers aren't necessarily next to one another or
# in any particular order

import numpy as np

def max_consec_run(nums):
    seen = {}
    for n in nums:
        seen.update({n:True})

    max_count = 0
    for n in nums:
        count = 1
        if seen.get(n-1)==None:
            val = n
            while seen.get(val+1)==True:
                val += 1
                count += 1
        if count>1 and count>max_count:
            max_count = count
    return max_count

def max_consec_sort(nums):
    nums.sort()
    max_count = 0
    count = 1
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]+1:
            count += 1
            if count>max_count:
                max_count=count
        elif nums[i]!=nums[i-1]:
            count = 1
    return max_count

for i in range(1000):        
    length = np.random.randint(20)
    nums = np.random.randint(0,30,size=length)
    ans1 = max_consec_sort(nums)
    ans2 = max_consec_run(nums)
    if ans1!=ans2:
        print('answer mismatch')
        print(nums,ans1,ans2)
