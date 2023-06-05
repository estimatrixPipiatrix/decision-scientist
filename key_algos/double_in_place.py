# use recursion to double every element of an array in place

import numpy as np
vec = np.array([2,7,4,2,1,3,6,3,10])

def dbl_in_place(vec,index=0):
    # pass in index = 0 for the first instance
    vec[index] = vec[index]**2.0
    if (index<(len(vec)-1)):
        index += 1
        dbl_in_place(vec,index)
    return

dbl_in_place(vec)
print(vec)
