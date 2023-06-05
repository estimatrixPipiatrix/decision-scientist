import numpy as np
# take a sentence that contains all letters of the alphabet but
# one and return the missing letter. make sure the algorithm
# is O(N)

sent = 'the quick brown box jumps over a lazy dog'

sent = sent.replace(' ','')
hash = {}
for n in sent:
    hash.update({n:True})

alpha = 'abcdefghijklmnopqrstuvwxyz'
for n in alpha:
    if not hash.get(n):
        print(n)
