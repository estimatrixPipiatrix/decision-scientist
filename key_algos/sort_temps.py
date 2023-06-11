# sort the following data in O(N). it's possible because the temps
# are limited to one decimal point and are all between 97.0 and
# 99.0 F

import numpy as np

temps = np.array([98.6,98.0,97.1,99.0,98.9,97.8,98.5,98.2,98.8,97.1])

start = 97.0
hash_temps = {}
for i in range(21):
    hash_temps.update({start:i})
    start += 0.1
    start = np.round(start,1)

sorted_temps = np.zeros(21)
for temp in temps:
    ind = hash_temps[temp]
    sorted_temps[ind] = temp

sorted_temps = np.delete(sorted_temps,sorted_temps==0)
print(sorted_temps)
