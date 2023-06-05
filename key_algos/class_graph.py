import graphviz
from graphviz import Digraph
from class_queue import queue
import sys

class vertex:
    def __init__(self,val):
        self.value = val
        self.edges = []

    def add_adjacent_vertex(self,vert):
        if vert in self.edges:
            return
        self.edges.append(vert)
        vert.add_adjacent_vertex(self)

def build_graph(vertex, dot, visited):
    curr = vertex
    A = str(curr)
    if visited=={}:
        dot.node(A,curr.value)
    visited.update({curr:True})
    copy_visited = visited.copy()
    for vert in curr.edges:
        if visited.get(vert)!=True:
            visited.update({vert:True})
            B = str(vert)
            dot.node(B,vert.value)
            dot.edge(A,B,arrowhead="none")
            build_graph(vert,dot,copy_visited)

def print_graph(vertex,visited):
    visited.update({vertex:True})
    print(vertex.value,len(vertex.edges))
    for vert in vertex.edges:
        if visited.get(vert)!=True:
            print_graph(vert,visited)

def depth_first_search(vertex,val,visited):
    if vertex.value==val:
        return vertex
    visited.update({vertex:True})
    for vert in vertex.edges:
        if visited.get(vert)!=True:
            result = depth_first_search(vert,val,visited)
            if result!=None:
                if result.value==val:
                    return result
    return None

def breadth_first_search(vertex,val,visited,q = queue()):
    visited.update({vertex:True})
    q.enqueue(vertex)
    while q.first!=None:
        vert = q.dequeue()
        if vert.value==val:
            return vert
        for v in vert.edges:
            if visited.get(v)!=True:
                visited.update({v:True})
                q.enqueue(v)

def display_graph(vertex):
    start = vertex
    if start.edges==[]:
        print('vertex has no edges!')
        return
    dot = Digraph(strict=True)
    build_graph(start, dot, {})
    dot.render('Digraph', format='png', view=True)

from name_generator import name_gen
import string
import random
import numpy as np

random.seed(1)
np.random.seed(1)

trie = name_gen()
num_names = 6
names = []
for i in range(num_names):
   letter = random.choice(string.ascii_letters).lower()
   possible_names = trie.autocomplete(letter)
   num_possible = len(possible_names)
   rand_choice = np.random.randint(num_possible)
   name = possible_names[rand_choice]
   if name!="":
       names.append(name)

vertices = []
for n in names:
    vertices.append(vertex(n))

for v1 in vertices:
    count = 0
    for v2 in vertices:
        linked = np.random.randint(2)
        if (v1!=v2 and linked==1 and count<=5):
            v1.add_adjacent_vertex(v2)
        count += 1

for v1 in vertices:
    if v1.edges == []:
        num_vert = len(vertices)
        rand_vert_num = np.random.randint(num_vert)
        v1.add_adjacent_vertex(vertices[rand_vert_num])
