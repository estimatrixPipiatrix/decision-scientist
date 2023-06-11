# write a function that takes an array and reverses the items in it
# while only requiring O(1) space complexity

array = [2,7,6,2,4,2,0,8]

def reverse_array(array):
    right = len(array)-1
    left  = 0
    while left < right:
        tmp = array[right]
        array[right]=array[left]
        array[left]=tmp
        left += 1
        right -= 1
    return array

print(reverse_array(array))
