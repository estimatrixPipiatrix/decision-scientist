# given an array of consecutive integers that has one missing,
# return the missing integer with O(N) time complexity

import numpy as np
nums = np.linspace(0,9,10).astype('int64')
np.random.shuffle(nums)
nums = np.delete(nums,4)

def find_missing(nums):
    is_present = {}
    for n in nums:
        is_present.update({n:True})

    for i in range(len(nums)):
        if is_present.get(i)==None:
            return i

print(find_missing(nums))
