# write a function that returns the intersection of two lists

vec1 = [0,3,2,5,4,7]
vec2 = [1,3,5,10]

def intersection(vec1,vec2):
    seen = {}
    for n in vec1:
        seen.update({n:True})

    in_common = []
    for n in vec2:
        if seen.get(n):
            in_common.append(n)

    return in_common

print(intersection(vec1,vec2))
