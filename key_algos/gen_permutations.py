# given a list of one or more distinct integers, write a function
# to generate all permutations of those integers. for example, given
# the input [2,3,4], return the following 6 permutations: [2,3,4],
# [2,4,3],[3,2,4],[3,4,2],[4,2,3],[4,3,2]

nums = [2,3,4,5]

def get_perms(nums):
    if len(nums)==1:
        return nums
    if len(nums)==2:
        perm1 = [nums[0],nums[1]]
        perm2 = [nums[1],nums[0]]
        return [perm1,perm2]
    else:
        perm_list = []
        for i in range(len(nums)):
            prefix = [nums[i]]
            before = nums[0:i]
            after  = nums[i+1:len(nums)]
            rest = before.copy()
            rest.extend(after)
            rest_perms = get_perms(rest)
            for perm in rest_perms:
                new_perm = prefix.copy()
                new_perm.extend(perm)
                perm_list.append(new_perm)
        return perm_list

result = get_perms(nums)
print(result)
print()
seen = {}
flag = 0
for perm in result:
    if seen.get(str(perm))==None:
        seen.update({str(perm):True})
    else:
        flag = 1
if flag==1:
    print('check: repeats found')
else:
    print('check: no repeats found')
