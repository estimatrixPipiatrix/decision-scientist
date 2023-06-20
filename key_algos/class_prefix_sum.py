# given an integer array nums, handle multiple queries of the 
# following type: calculate the sum of the elements of nums 
# between indices left and right inclusive where left <= right

class prefix_sum:
    def __init__(self,arr):
        self.arr = arr
        prefix = []
        total = 0
        for i in range(len(arr)):
            total += arr[i]
            prefix.append(total)
        self.prefix = prefix

    def range_sum(self,left,right):
        if left-1<0:
            left_val = 0
        else:
            left_val = self.prefix[left-1]
        right_val = self.prefix[right]
        return right_val-left_val
