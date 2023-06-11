# generate a random sequence of n integers that sum to a given
# target and are all within sigma from the mean

import numpy as np

target = 27
length = 5
sigma = 6

def random_to_target(target,length,sigma):
    mean = target/length
    max_num = mean+sigma
    min_num = mean-sigma
    nums = []
    done = False
    while done == False:
        if len(nums)<length:
            candidate = np.random.randint(0,target)
            if candidate >= min_num and candidate <= max_num:
                nums.append(candidate)
        else:
            nums_np = np.array(nums)
            if nums_np.sum()==target:
                done=True
            else:
               nums = []
    return np.array(nums)
