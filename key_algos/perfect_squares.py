# given a number n, find the smallest number of perfect squares
# that sum up to n

import numpy as np

def find_prev_squares(n):
    squares = []
    perfect_square = 0
    for i in range(1,n+1):
        if round(np.sqrt(i))==np.sqrt(i):
            squares.append(i)
    return squares

def find_nearest_square(n):
    i = n
    while round(np.sqrt(i))!=np.sqrt(i):
        i -= 1
    return i

def sum_of_squares(n):
    max_square = find_nearest_square(n)
    nums_to_sum = [max_square]
    # dist to the nearest perfect square
    dist = n-max_square
    # find squares that are less than dist
    below_dist = find_prev_squares(dist)
    nums_to_sum_np = np.array(nums_to_sum)
    to_add = len(below_dist)-1
    curr_sum = nums_to_sum_np.sum()
    while curr_sum!=n:
        candidate = below_dist[to_add]
        if curr_sum+candidate<=n:
            nums_to_sum.append(candidate)
            curr_sum += candidate
        else:
            to_add -= 1
 
    return nums_to_sum

n = 555
print('n = ',n)
print(sum_of_squares(n))         
