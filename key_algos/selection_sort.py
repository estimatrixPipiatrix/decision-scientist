import numpy as np

vec = np.array([-2,-4,5,4,8,9,5,0,-7,3])

for i in range(len(vec)):
    smallest = vec[i]
    for j in range(i,len(vec)):
        if vec[j]<smallest:
            smallest = vec[j]
            swap_flag = 1
            swap_index = j
            print(i,j)
    if swap_flag==1:
        tmp = vec[i]
        vec[i] = vec[swap_index]
        vec[swap_index]=tmp
        print(vec)
    swap_flag = 0

print(vec)
