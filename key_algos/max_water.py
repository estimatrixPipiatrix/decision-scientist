# you are given an integer array height of length n. There are n 
# vertical lines drawn such that the two endpoints of the ith 
# line are (i, 0) and (i, height[i])

# find two lines that together with the x-axis form a container, 
# such that the container contains the most water

# return the maximum amount of water a container can store

# note: the array elements are potential heights of the two walls
# of a container; the space between those elements is the width
# of the container; we're trying to maximize the volume

# input: height = [1,8,6,2,5,4,8,3,7]
# output: 49
# explanation: The above vertical lines are represented by array 
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water 
# (blue section) the container can contain is 49

#heights = [1,8,6,2,5,4,8,3,7]

def max_volume(heights):
    max_vol = 0
    left = 0
    right = len(heights)-1
    while left<right:
        left_h = heights[left]
        right_h = heights[right]
        curr_vol = min(left_h,right_h)*(right-left)
        if curr_vol>max_vol:
            max_vol = curr_vol
        if heights[left]<heights[right]:
            left += 1
        else:
            right -= 1

    return max_vol

def max_volume_brute(heights):
    left = 0
    max_vol = 0
    while left<len(heights)-1:
        h_left = heights[left]
        right = left+1
        while right<len(heights):
            h_right = heights[right]
            curr_vol = min(h_left,h_right)*(right-left)
            if curr_vol > max_vol:
                max_vol = curr_vol
            right += 1
        left += 1
    return max_vol

import numpy as np

for i in range(1000):
    length = np.random.randint(2,20)
    heights = np.random.randint(1,20,size=length)
    method_1 = max_volume(heights)
    method_2 = max_volume_brute(heights)
    if method_1!=method_2:
        print(heights)
        print(method_1,method_2)
