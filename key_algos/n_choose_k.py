# given an integer n and an integer k, output a list of all the
# combinations of k numbers chosen from 1 to n. for example, if
# n=3 and k=2, return [1,2],[1,3],[2,3]

import numpy as np
import sys

def gen_next_combos(k,n,curr_combo):
    prev_len = len(curr_combo)
    prev_num = curr_combo[len(curr_combo)-1]
    slots_left = k-prev_len
    nums_left = n-prev_num
    next_len = nums_left-slots_left+1     
    next_combos = []
    for i in range(next_len):
        next_combos.append(curr_combo.copy())
    for i,combo in enumerate(next_combos):
        combo.append(prev_num+i+1)
    return next_combos

def gen_n_choose_k(k,n,combos=[]):
    if combos==[]:
        num_combos = n-k+1
        for i in range(num_combos):
            combos.append([i+1])
        return gen_n_choose_k(k,n,combos)
    next_combos = []
    if len(combos[0])<k:
        for combo in combos:
            next_combos.extend(gen_next_combos(k,n,combo))
        return gen_n_choose_k(k,n,next_combos)
    return combos

n=4
k=2
print(gen_n_choose_k(k,n,[]))
