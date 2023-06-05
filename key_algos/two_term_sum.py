# return the indices of two elements that add up to a given
# target

nums = [11, 5, 7, 15, 2, 6, 50]
target = 9
size = 7

hash = {}
for i,n in enumerate(nums):
    hash.update({n:i})

for i,n in enumerate(nums):
    complement = target-n
    if hash.get(complement) != None:
        index_1 = min(i,hash[complement])
        index_2 = max(i,hash[complement])

print([index_1,index_2])
