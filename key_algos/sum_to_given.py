# given an array return the indices of two elements that sum to a given
# number. assume there is exactly one solution

nums = [6,7,2,3,5]
given = 7

def sum_to_given(nums,given):
    nums_hash = {}
    for i,n in enumerate(nums):
        nums_hash.update({n:i})

    for i,n in enumerate(nums):
        complement = given-n
        if nums_hash.get(complement)!=None:
            j = nums_hash[complement]
            if j!=i:
                return i,j

print(sum_to_given(nums,given))
