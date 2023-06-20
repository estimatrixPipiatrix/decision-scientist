# Given an integer array nums sorted in non-decreasing order, 
# remove some duplicates in-place such that each unique element 
# appears at most twice. The relative order of the elements 
# should be kept the same.

# Since it is impossible to change the length of the array in 
# some languages, you must instead have the result be placed in 
# the first part of the array nums. More formally, if there are 
# k elements after removing the duplicates, then the first k 
# elements of nums should hold the final result. It does not 
# matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots 
# of nums.

# Do not allocate extra space for another array. You must do 
# this by modifying the input array in-place with O(1) extra 
# memory.

arr = [0,0,1,3,3,3,3,4,6,7,7,9,9,9]

def remove_from_arr(arr,position):
    tmp = arr[position]
    for i in range(position,len(arr)-1):
        arr[i]=arr[i+1]
    arr[len(arr)-1]=tmp
    return arr

def remove_repeats(arr):
    left = 0
    right = 1
    while right<len(arr):
        while arr[left]==arr[right]:
            remove_from_arr(arr,right)
            if right>=len(arr):
                break
        left += 1
        right = left + 1
    return arr

print(remove_repeats(arr))














