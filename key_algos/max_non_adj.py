import numpy as np
# find the max subarray sum of non-adjacent elements

vec = np.array([1,0,0,4,10,0,1])

def max_non_adj_sum(vec,use_left=1):
    if len(vec)==1:
        if (use_left==1):
            return vec[0]
        else:
            return 0
    elif use_left==1:
        use_left = 0
        choice1 = vec[0] + max_non_adj_sum(vec[1:len(vec)],use_left)
        use_left = 1
        choice2 = max_non_adj_sum(vec[1:len(vec)],use_left)
        return max(choice1,choice2)
    else:
        use_left = 1
        return max_non_adj_sum(vec[1:len(vec)],use_left)

print(max_non_adj_sum(vec))
