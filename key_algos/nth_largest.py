import numpy as np
import sys
import pdb
# find the nth largest element in an array

from partition_array import quicksort,partition

#vec = [3,3,6,6,6,2,1,1,10,-1]
#vec = [5,6,0,2,8,4]
#n = 3

def get_largest(vec,n):
    target = n-1
    vec,pivot = partition(vec)
    while target != pivot:
        if (target<pivot):
            vec,pivot = partition(vec[0:pivot])
        elif (target>pivot):
            target = target - pivot - 1
            vec,pivot = partition(vec[pivot+1:len(vec)])
    return vec[target]

for i in range(100):
    length = np.random.randint(2,20)
    vec = np.random.randint(-10,11,size=length)
    vec.tolist()
    n = np.random.randint(1,length)
    ans1 = get_largest(vec,n)
    vec.sort()
    ans2 = vec[n-1]
    if ans1!=ans2:
        print('answer mismatch!')
