# given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element 
# appears only once. the relative order of the elements should 
# be kept the same. then return the number of unique elements 
# in nums

nums = [0,0,1,1,2,4,4,4,5,6,7,7,9,9]

def delete_repeats(nums):
    left = 0
    right = 1
    while left<len(nums) and right<len(nums):
        #print(nums,left,right)
        while nums[left]==nums[right]:
            nums.pop(right)
            if right>=len(nums):
                break
        left += 1
        right = left+1
    return nums,len(nums)

print(delete_repeats(nums))
