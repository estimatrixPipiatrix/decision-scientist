# given two arrays, compute the correlation between them

import numpy as np

vec1 = np.array([0,3,4,6,2,5])
vec2 = np.array([1,4,5,3,8,8])

mean1 = vec1.mean()
mean2 = vec2.mean()

delta1 = vec1-mean1
delta2 = vec2-mean2
numer = np.dot(delta1,delta2)

delta1_sqr = delta1**2.0
delta2_sqr = delta2**2.0
denom = np.sqrt(delta1_sqr.sum()*delta2_sqr.sum())

print(numer/denom)
