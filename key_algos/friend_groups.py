# say there are n people. if person A is friends with person B
# and B is friends with person C, then person A is considred an
# indirect friend of C
# define a friend group to be any group that is either directly or
# indirectly friends. given an n-by-n adjacency matrix N, where
# N[i][j] is one if person i and person j are friends, and zero
# otherwise, write a function to determine how many friend groups
# exist
import numpy as np
import sys

def find_cycles(N,row,visited={}):
    visited.update({row:True})
    for j in range(N.shape[1]):
        if N[row,j]==1 and visited.get(j)==None:
            find_cycles(N,j,visited)

def num_groups(N):
    visited = {}
    groups = 0
    for i in range(N.shape[0]):
        if visited.get(i)==None:
            find_cycles(N,i,visited)
            groups += 1
    return groups

def num_groups_brute(N):
    friends = {}
    for i in range(N.shape[0]):
        friends.update({i:{i}})
    for i in range(N.shape[0]):
        for j in range(N.shape[1]):
            if N[i,j]==1:
                friends_i = friends[i].copy()
                friends_j = friends[j].copy()
                friends_i = friends[i].union(friends_j)
                friends_j = friends[j].union(friends_i)
                friends.update({i:friends_i})
                friends.update({j:friends_j})
            for friend in friends[i]:
                friends_i = friends[i].copy()
                friends_friend = friends[friend].copy()
                friends_i = friends[i].union(friends_friend)
                friends_friend = friends[friend].union(friends_i)
                friends.update({i:friends_i})
                friends.update({friend:friends_friend})
    seen = {}
    num_groups = 0
    for key in friends.keys():
        if seen.get(str(friends[key]))==None:
            seen.update({str(friends[key]):True})
            num_groups += 1
    return num_groups

np.random.seed(4)
for i in range(100):
    num_ppl = np.random.randint(1,10)
    N = np.random.randint(0,2,size=(num_ppl,num_ppl))
    for i in range(N.shape[0]):
        for j in range(N.shape[0]):
            if i==j:
                N[i,j]=1
            else:
                N[i,j]=N[j,i]

#N = np.array([[1, 0, 0], \
#              [0, 1, 1], \
#              [0, 1, 1]])
    method_1 = num_groups_brute(N)
    method_2 = num_groups(N)
    if method_1 != method_2:
        print(N)
        print('num_groups method 1:', method_1)
        print('num_groups method 2:', method_2)
