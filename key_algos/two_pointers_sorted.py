# find the indices of a sorted array where the elements add up
# to a given target

vec = [2,7,11,15]
target = 9

def add_to_target(vec,target):
    L = 0
    R = len(vec)-1
    flag = 0

    while ((L<R) and (flag==0)):
        cur_sum = vec[L]+vec[R]
        if cur_sum > target:
            R -= 1
        elif cur_sum < target:
            L += 1
        else:
            flag = 1

    if (flag==1):
        return [L,R]
    else:
        print('not found')

print(add_to_target(vec,target))
