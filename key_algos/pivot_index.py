# given an array of integers nums, calculate the pivot index 
# of this array. the pivot index is the index where the sum of all 
# the numbers strictly to the left of the index is equal to the 
# sum of all the numbers strictly to the index's right

# if the index is on the left edge of the array, then the left sum 
# is 0 because there are no elements to the left. This also 
# applies to the right edge of the array

# return the leftmost pivot index. If no such index exists, 
# return -1

# example: input: nums = [1,7,3,6,5,6]; output: 3; explanation:
# the pivot index is 3. left sum = nums[0] + nums[1] + nums[2] 
# = 1 + 7 + 3 = 11, right sum = nums[4] + nums[5] = 5 + 6 = 11

class num_array:
    def __init__(self,arr):
        self.array = arr
        total = 0
        prefix = []
        for i in range(len(arr)):
            total += arr[i]
            prefix.append(total)
        self.prefix = prefix
        total = 0
        postfix = []
        for i in range(len(arr)-1,-1,-1):
            total += arr[i]
            postfix.append(total)
        postfix.reverse()
        self.postfix = postfix

    def pivot_index(self):
        arr = self.array
        for i in range(len(arr)):
            if i==0:
                sum_left = 0
            else:
                sum_left = self.prefix[i-1]
            if i==len(arr)-1:
                sum_right = 0
            else:
                sum_right = self.postfix[i+1]
            if sum_left==sum_right:
                return i
        return -1

arr = [1,7,3,6,5,6]
na = num_array(arr)
