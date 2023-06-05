from partition_array import quicksort
import numpy as np
# given an array of consecutive integers where one is missing,
# determine the missing integer with O(N*log N)

def find_missing(vec):
    vec = quicksort(vec)
    for i in range(len(vec)-1):
        if vec[i+1] != vec[i]+1:
            missing = vec[i]+1
    return missing

for i in range(100):
    low = np.random.randint(-10,0)
    high = np.random.randint(1,11)
    vec = np.linspace(low,high,high-low+1).astype('int')
    to_delete = np.random.randint(1,len(vec)-1)
    deleted_val = vec[to_delete]
    vec = np.delete(vec,[to_delete])
    vec = vec.tolist()
    predicted = find_missing(vec)
    if deleted_val != predicted:
        print('mismatch:')
        print(vec)
        print(deleted_val)
        print(find_missing(vec))
