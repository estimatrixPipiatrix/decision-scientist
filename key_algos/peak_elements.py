# write a function to return the indices of any 'peak' elements
# in a given array. a peak element is one that has values smaller
# than itself to its left and its right. count also if the first
# or last elements are larger than their neighbors. finally, make
# the algo have O(log N) time complexity

import sys

vec = [0,3,5,2,4,1]

def find_peaks(vec,peaks=[],offset=0):
    if len(vec)==1:
        return
    if len(vec)==2:
        if vec[0]>vec[1]:
            peaks.append(0+offset)
        elif vec[1]>vec[0]:
            peaks.append(1+offset)
        return
    mid = int(len(vec)/2)
    if mid-1>=0 and mid+1<=len(vec)-1:
        if vec[mid-1] < vec[mid] and \
           vec[mid+1] < vec[mid]:
               peaks.append(mid+offset)
        if mid-1==0 and vec[mid-1]>vec[mid]:
                peaks.append(mid-1+offset)
        if mid+1==len(vec)-1 and vec[mid+1]>vec[mid]:
                peaks.append(mid+1+offset)
        find_peaks(vec[0:mid],peaks,offset=0)
        find_peaks(vec[mid+1:len(vec)],peaks,offset=mid+1)
    elif mid-1>=0:
        if vec[mid-1] < vec[mid]:
            peaks.append(mid+offset)
        find_peaks(vec[0:mid],peaks,offset=0)
    elif mid+1<=len(vec)-1:
        if vec[mid+1]<vec[mid]:
            peaks.append(mid+offset)
        find_peaks(vec[mid+1:len(vec)],peaks,offset=mid+1)
    return peaks

print(find_peaks(vec))
