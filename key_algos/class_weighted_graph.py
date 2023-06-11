import graphviz
from graphviz import Digraph
import numpy as np

class vertex:
    def __init__(self,value):
        self.value = value
        self.edges = {}
        self.edge_vals = []

def least_path(start_vert,curr_vert,visited={}, \
               least={},previous={}):
    # least is a hash table that has the least amount to get from
    # the start_vert to the vert in question {vert:least_amount}
    # previous is a hash table that has the previous vertex to visit
    # in order to obtain that least amount
    visited.update({curr_vert:True})
    if (curr_vert==start_vert):
        least.update({start_vert:0})
        previous.update({start_vert:start_vert})
    cost_from_start = least[curr_vert]
    edges = list(curr_vert.edges.keys())
    for edge in edges:
        cost = curr_vert.edges[edge]
        total_cost = cost_from_start + cost
        if least.get(edge)==None:
            least.update({edge:total_cost})
            previous.update({edge:curr_vert})
        elif total_cost < least[edge]:
            least.update({edge:total_cost})
            previous.update({edge:curr_vert})
    least_cost = np.inf
    for edge in edges:
        if visited.get(edge)!=True:
            cost_from_start = least[edge]
            if cost_from_start<least_cost:
                least_cost = cost_from_start
                least_edge = edge
    if least_cost<np.inf:
        least_path(start_vert,least_edge,visited,least,previous)
       
def get_least(start_vert):
    visited = {}
    least = {}
    previous = {}
    least_path(start_vert,start_vert,visited,least,previous)
    keys = list(previous.keys())
    from_to = {}
    for key in keys:
        key_value = key.value
        mapped_to = previous[key].value
        from_to.update({key_value:mapped_to})
    return from_to

def build_graph(vertices, dot):
    for curr in vertices:
        A = str(curr)
        edges = list(curr.edges.keys())
        for vert in edges:
            B = str(vert)
            dot.node(B,vert.value)
            dot.edge(A,B,label=str(curr.edges[vert]))

def display_graph(vertices):
    dot = Digraph()
    build_graph(vertices, dot)
    dot.render('Digraph', format='png', view=True)

import pandas as pd
import numpy as np
places = pd.read_csv('places.csv')
vertices = []
for place in places.iloc[:,0]:
    vert = vertex(place)
    vertices.append(vert)

np.random.seed(1)
num_places = len(places)
for i,vert in enumerate(vertices):
    connections = np.random.randint(2,size=num_places)
    mask        = np.random.randint(2,size=num_places)
    connections = connections*mask
    distances   = np.random.randint(100,size=num_places)
    connections[i] = 0
    distances[i]   = 0
    for j,link in enumerate(connections):
        if link==1:
            vert.edges.update({vertices[j]:distances[j]})
            vert.edge_vals.append(vertices[j].value)
    #print(vert.value,vert.edge_vals)
