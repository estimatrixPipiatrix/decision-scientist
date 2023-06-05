from partition_array import quicksort
import numpy as np
# given an array, return the greatest product possible by 
# multiplying three different elements

vec = [3,4,-2,1]

def greatest_product(vec):
    neg = 0
    pos = 0
    for n in vec:
        if n>0:
            pos += 1
        if n<0:
            neg += 1
    
    vec = quicksort(vec)
    vec = np.array(vec)

    if neg<=1 or pos==0:
        return vec[-3:].prod()
    elif neg>=2:
        choice1 = vec[len(vec)-3:len(vec)].prod()
        choice2 = vec[0]*vec[1]*vec[-1]
        return max(choice1,choice2)

def greatest_brute(vec):
    max_prod = -np.inf
    vec = np.array(vec)
    for i in range(len(vec)):
        for j in range(len(vec)):
            for k in range(len(vec)):
                if i!=j and i!=k and j!=k:
                    prod = vec[i]*vec[j]*vec[k]
                    if prod>max_prod:
                        max_prod = prod
    return max_prod

for i in range(100):
    length = np.random.randint(3,11)
    vec = np.random.randint(-10,10,size=length)
    vec = vec.tolist()
    val1 = greatest_brute(vec)
    val2 = greatest_product(vec)
    if val1 != val2:
        print('mismatch:')
        print(vec)
        print('brute: ',val1)
        print('sort method: ',val2)
