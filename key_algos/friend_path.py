# given a social graph and two users, write a function to return
# the smallest number of friendships between the two users.
# for example, take a graph consisting of A,B,C,D,E with edges
# (A,B),(A,C),(B,D),(D,E) with inputs A and E. the answer should
# be 3 because A is friends with B, B with D, and D with E

import sys

class node:
    def __init__(self,value):
        self.value = value
        self.edges = []

A = node('A')
B = node('B')
C = node('C')
D = node('D')
E = node('E')
A.edges = [B,C]
B.edges = [A,D]
D.edges = [B,E]
E.edges = [D]
C.edges = [A]

start = A
end = E

queue = [start]
vis = {}
shortest = {start:[start]}
while queue != []:
    curr = queue.pop(0)
    vis.update({curr:True})
    for edge in curr.edges:
        if vis.get(edge)==None:
            queue.append(edge)
            dist_from_start = len(shortest[curr])-1
            dist_to_edge = dist_from_start + 1
            if shortest.get(edge)==None:
                min_path = shortest[curr].copy()
                min_path.append(edge)
                shortest.update({edge:min_path})
            else:
                min_path = shortest[edge].copy()
                min_dist = len(shortest[edge])-1
                if dist_to_edge<min_dist:
                    min_path = shortest[curr]
                    min_path.append(edge)
                    shortest.update({edge:min_path})
ans = len(shortest[end])-1

keys = shortest.keys()
shortest_vals = {}
for key in keys:
    key_name = key.value
    path = []
    for vert in shortest[key]:
        vert_name = vert.value
        path.append(vert_name)
    shortest_vals.update({key_name:path})
