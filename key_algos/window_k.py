import numpy as np

# given a vector and an integer k, return True if there are 
# duplicate values within any window of that size

vec = np.array([1,2,3,1,2,3])
k = 3
window_size = k+1

window = set()
L = 0
flag = 0
for R in range(vec.shape[0]):
    if (R-L+1)>window_size:
        window.remove(vec[L])
        L += 1
    if vec[R] in window:
        flag = 1
    window.add(vec[R])

if flag:
    print('True')
else:
    print('False')
