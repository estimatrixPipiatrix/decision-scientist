import numpy as np

# kadane's algorithm finds the largest subarray sum
# but with only O(n) time complexity

vec = np.array([5,4,-1,7,8])

cursum = 0.0
maxsum = vec[0]
L = 0
R = 0
max_L = 0
max_R = 0

for i,n in enumerate(vec):
    cursum = max(0,cursum)
    if cursum == 0:
        L = i
    R = i
    cursum += n
    if cursum>maxsum:
        maxsum=cursum
        max_L,max_R = L,R

print(max_L,max_R,maxsum)
