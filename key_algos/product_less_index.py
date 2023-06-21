# given an integer array nums, return an array answer such that 
# answer[i] is equal to the product of all the elements of nums 
# except nums[i]
# the product of any prefix or suffix of nums is guaranteed to 
# fit in a 32-bit integer
# you must write an algorithm that runs in O(n) time and without 
# using the division operation.
# example: input: nums = [1,2,3,4]; output: [24,12,8,6]

class num_array:
    def __init__(self,arr):
        self.array = arr
        prefix_prod = []
        prod = 1
        for i in range(len(arr)):
            prod *= arr[i]
            prefix_prod.append(prod)
        self.prefix_prod = prefix_prod
        postfix_prod = []
        prod = 1
        for i in range(len(arr)-1,-1,-1):
            prod *= arr[i]
            postfix_prod.append(prod)
        postfix_prod.reverse()
        self.postfix_prod = postfix_prod

    def product_less_index(self,index):
        if index==0:
            return self.postfix_prod[1]
        elif index==len(self.array)-1:
            return self.prefix_prod[len(self.array)-2]
        else:
            before = self.prefix_prod[index-1]
            after = self.postfix_prod[index+1]
            return before*after

arr = [1,2,3,4]
na = num_array(arr)
