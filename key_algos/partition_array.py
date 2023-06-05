import sys
import pdb
import numpy as np

def partition(vec):
    left = 0
    pivot = len(vec)-1
    right = pivot - 1
    while left<right:
        while (vec[left]<=vec[pivot] and left<pivot):
            left += 1
        while (vec[right]>vec[pivot] and right>0):
            right -= 1
        if left<right:
            tmp = vec[left]
            vec[left] = vec[right]
            vec[right] = tmp
    if vec[pivot]<vec[left]:
        tmp = vec[pivot]
        vec[pivot] = vec[left]
        vec[left] = tmp
        pivot = left
    return vec,pivot

# check that partition works
#vec = [4,7]
#print(vec)
#print(partition(vec))

#sys.exit()

#for i in range(100):
#    length = np.random.randint(1,20)
#    vec = np.random.randint(0,10,size=length)
#    vec = vec.tolist()
#    print('test vec:',vec)
#    out_vec,pivot = partition(vec)
#    print('output:',out_vec,pivot)

#sys.exit()

def quicksort(vec):
    if len(vec)==1:
        return vec
    else:
        vec,pivot = partition(vec)
 
        if pivot>0:
            left_vec = quicksort(vec[0:pivot])
        else:
            left_vec = []
        if (pivot+1)<len(vec):
            right_vec = quicksort(vec[pivot+1:len(vec)])
        else:
            right_vec = []
        pivot_val = vec[pivot]
        left_vec.extend([pivot_val])
        left_vec.extend(right_vec)
        return left_vec

#vec = [3,3,6,6,6,2,1,1,10,-1]
#print(quicksort(vec))

#for i in range(100):
#    length = np.random.randint(1,20)
#    vec = np.random.randint(0,10,size=length)
#    vec = vec.tolist()
#    out_vec = quicksort(vec)
#    vec.sort()
#    if out_vec!=vec:
#        print(vec)
#        print(out_vec)
