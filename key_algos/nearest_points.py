# given a collection of 2D coordinates, write a function to return 
# the k points that are closest to the origin, using Euclidean distance
import numpy as np
import heapq

k=3
points = [[2,-1],[3,2],[4,1],[-1,-1],[-2,2]]

def k_nearest_origin(k,points):
    distances = []
    dist_to_point = {}
    for point in points:
        x = point[0]
        y = point[1]
        dist = np.sqrt(x**2.0+y**2.0)
        dist_to_point.update({dist:point})
        distances.append(dist)

    distances = np.array(distances)
    distances = heapq.nsmallest(3,distances)
    nearest = []
    for dist in distances:
        nearest.append(dist_to_point[dist])
    return nearest

print(k_nearest_origin(k,points))
