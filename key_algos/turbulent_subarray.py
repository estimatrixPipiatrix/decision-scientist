# Given an integer array arr, return the length of a maximum size 
# turbulent subarray of arr. A subarray is turbulent if the 
# comparison sign flips between each adjacent pair of elements 
# in the subarray

arr = [9,4,2,10,7,8,8,1,9]
#arr = [4,8,12,16]
#arr = [4,4,4,5,3]

turb = []
for i in range(1,len(arr)):
    turb.append(arr[i]-arr[i-1])

def sign(num):
    if num>0:
        return +1
    elif num<0:
        return -1
    else:
        return 0

def max_turb_sub(arr):
    max_flips = 0
    flips = 0
    flag = 0
    for i in range(1,len(turb)):
        prev_num = turb[i-1]
        curr_num = turb[i]
        if prev_num!=0 or curr_num!=0:
            flag = 1
        if (sign(prev_num)==1 and sign(curr_num)==-1) or \
           (sign(prev_num)==-1 and sign(curr_num)==1):
            flips += 1
        else:
            flips = 0
        if flips>max_flips:
            max_flips = flips
    if max_flips!=0 or flag==1:
        max_flips += 2
    return max_flips

print(max_turb_sub(arr))
