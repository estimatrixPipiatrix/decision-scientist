# create a function that returns True if there is an upward three point
# trend in the input array and False otherwise; the three points need
# not be consecutive

import numpy as np

def three_point_trend(array):
    lowest = array[0]
    middle = np.inf
    for n in array:
        if n<lowest:
            lowest = n
        if n>lowest and n<middle:
            middle = n
        if n>lowest and n>middle:
            return True
    return False

# we'll test the above O(N) algo against an O(N^3) version
def three_point_trend_alt(array):
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                if i<j and j<k:
                    if array[i]<array[j] and array[j]<array[k]:
                        return True
    return False

max_length = 20
for i in range(100):
    array_size = np.random.randint(1,21)
    array = np.random.randint(0,10,size=array_size)
    ans1 = three_point_trend(array)
    ans2 = three_point_trend_alt(array)
    #print(array,ans1,ans2)
    if ans1!=ans2:
        print('answer mismatch for array: ',array)
        print('ans1: ',ans1)
        print('ans2: ',ans2)
