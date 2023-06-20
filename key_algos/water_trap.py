# given n non-negative integers representing an elevation map 
# where the width of each bar is 1, compute how much water it 
# can trap after raining

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# explanation: the above elevation map is represented by array 
# [0,1,0,2,1,0,1,3,2,1,2,1]. in this case, 6 units of rain water 
# (blue section) are being trapped

heights = [0,1,0,2,1,0,1,3,2,1,2,1]

def calc_rain_trapped(heights):
    left = 0
    while heights[left]==0:
        left += 1
    vol = 0
    while left<len(heights)-1:
        right = find_right_wall(heights,left)
        if right!=len(heights):
            vol += calc_area(heights,left,right)
            left = right
        else:
            left += 1
    return vol

def find_right_wall(heights,left):
    # note: if there is no right wall then an index equal
    # to the size of the input array will be returned
    right = left+1
    h_left = heights[left]
    flag = 0
    while flag==0:
        if right<len(heights):
            h_right = heights[right]
        else:
            flag = 1
        if flag==0:
            if heights[right]>=heights[left] or \
               right>=len(heights):
                flag = 1
        right += 1
    return right-1

def calc_area(heights,left,right):
    # returns the area between between left and right
    h_left = heights[left]
    h_right = heights[right]
    surface_height = min(h_left,h_right)
    area = 0
    for i in range(left,right):
        area += surface_height-heights[i]
    return area

print(calc_rain_trapped(heights))
