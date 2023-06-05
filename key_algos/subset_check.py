# check if one array contains a subset of another
import numpy as np

vec1 = np.array([6,2,-1,0,3,2,6])
vec2 = np.array([-1,2,6,10])

hash = {}
flag = 0
if len(vec1)>len(vec2):
    for n in vec1:
        hash.update({n:True})
    for n in vec2:
        if not hash.get(n):
            flag = 1
else:
    for n in vec2:
        hash.update({n:True})
    for n in vec1:
        if not hash.get(n):
            flag = 1

if flag==1:
    print("not a subset")
else:
    print("is a subset")
