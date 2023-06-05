import numpy as np

vec = ['d','e','f','g','b','f']

hash = {}
for n in vec:
    hash.update({n:True})

count = 0
repeat = ''
for n in vec:
    if hash.get(n):
        count += 1
        repeat = n

print(repeat)
