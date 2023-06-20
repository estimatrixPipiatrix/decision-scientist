# given two arrays with integers, return the maximum length of 
# the common subarray within both arrays. for example, if the two
# arrays are [1,3,5,6,7] and [2,4,3,5,6] then return 3, since the
# length of the maximum common subarray, [3,5,6], is 3

import sys

vec1 = [7,7,1,1,7,7,7]
vec2 = [7,7,4,7,7,7]

def max_common_len(vec1,vec2):
    seen = {}
    for i,num in enumerate(vec1):
        if seen.get(num)==None:
            seen.update({num:[i]})
        else:
            ind_lst = seen[num].copy()
            ind_lst.append(i)
            seen.update({num:ind_lst})

    max_length = 0
    left = 0
    right = 0
    while right<len(vec2):
        if seen.get(vec2[right])!=None:
            right_prev = right
            for i in seen[vec2[right]]:
                flag = 0
                count = 0
                left = i
                right_prev = right
                while left<len(vec1) and right<len(vec2) and flag==0:
                   if vec1[left]==vec2[right]:
                       count += 1
                       left += 1
                       right += 1
                   else:
                       flag = 1
                if count > max_length:
                    max_length = count
                right = right_prev
        right += 1
    return max_length

def max_common_len_brute(vec1,vec2):
    max_length = 0
    for i in range(len(vec1)):
        for j in range(len(vec2)):
            if vec1[i]==vec2[j]:
                count = 0
                left = i
                right = j
                while left<len(vec1) and right<len(vec2) and \
                      vec1[left]==vec2[right]:
                    count += 1
                    left += 1
                    right += 1
                if count>max_length:
                    max_length = count
    return max_length

#print(max_common_len(vec1,vec2))
#print(max_common_len_brute(vec1,vec2))
#sys.exit()

import numpy as np
for i in range(1000):
    max_len1 = np.random.randint(1,11)
    max_len2 = np.random.randint(1,11)
    range1 = np.random.randint(1,20)
    range2 = np.random.randint(1,20)
    vec1 = np.random.randint(0,range1,max_len1)
    vec2 = np.random.randint(0,range2,max_len2)

    method_1 = max_common_len(vec1,vec2)
    method_2 = max_common_len_brute(vec1,vec2)
    if (method_1!=method_2):
        print(method_1,method_2)
        print(vec1)
        print(vec2)
