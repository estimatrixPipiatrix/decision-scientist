from class_queue import queue
from class_graph import *

A = vertex('A')
B = vertex('B')
C = vertex('C')
D = vertex('D')
E = vertex('E')
F = vertex('F')
G = vertex('G')
A.add_adjacent_vertex(B)
B.add_adjacent_vertex(C)
C.add_adjacent_vertex(D)
D.add_adjacent_vertex(A)
D.add_adjacent_vertex(E)
D.add_adjacent_vertex(F)
C.add_adjacent_vertex(F)
F.add_adjacent_vertex(G)

# given two vertices, return a list with the shortest path from 
# the first to the second
def shortest_path(start):
    visited = {}
    shortest = {start:[start]}
    q = queue()
    q.enqueue(start)
    while q.first != None:
        curr_vert = q.dequeue()
        visited.update({curr_vert:True})
        dist_to_curr = len(shortest[curr_vert])-1
        for edge in curr_vert.edges:
            if visited.get(edge)!=True:
                if shortest.get(edge)==None:
                    shortest.update({edge:[curr_vert,edge]})
                else:
                    dist_to_edge = dist_to_curr+1
                    min_path = shortest[edge]
                    min_dist = len(min_path)-1
                    if dist_to_edge < min_dist:
                        min_path = shortest[curr_vert].append(edge)
                        shortest.update({edge:min_path})
                q.enqueue(edge)
    keys = list(shortest.keys())
    shortest_vals = {}
    for key in keys:
        key_val = key.value
        mapped_to = shortest[key]
        mapped_to_vals = []
        for vert in mapped_to:
            mapped_to_vals.append(vert.value)
        shortest_vals.update({key_val:mapped_to_vals})
    return shortest_vals
