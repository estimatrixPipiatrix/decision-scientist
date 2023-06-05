import numpy as np
# return an array holding the numbers that appear in two given
# arrays

vec1 = np.array([1,5,3,0,-1,2,3])
vec2 = np.array([0,10,33,-1,2,6,9])

hash = {}
for n in vec1:
    hash.update({n:True})

same = []
for n in vec2:
    if hash.get(n):
        same.append(n)

same = np.array(same)
print(same)
