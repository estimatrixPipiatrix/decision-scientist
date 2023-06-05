# note: This class is under construction and not yet operational!

import graphviz
from graphviz import Digraph
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

    def build_graph(self, dot, visited, done_edges):
        curr = self
        A = str(curr)
        dot.node(A,curr.value)
        visited.update({self:True})
        for vert in curr.edges:
            B = str(vert)
            dot.node(B,vert.value)
            if done_edges.get(A)!=B and \
               done_edges.get(B)!=A:
                dot.edge(A,B,arrowhead="none")
                done_edges.update({A:B})
                done_edges.update({B:A})
                if visited.get(vert)!=True:
                    vert.build_graph(dot,visited,done_edges)

    def print_graph(self,visited):
        visited.update({self:True})
        print(self.value)
        for vert in self.edges:
            if visited.get(vert)!=True:
                vert.print_graph(visited)
 
    def depth_first_search(self,val,visited):
        if self.value==val:
            return self
        visited.update({self:True})
        print(self.value,'self')
        for vert in self.edges:
            if visited.get(vert)!=True:
                print(vert.value,'vert')
                return vert.depth_first_search(val,visited)
        return

    def display_graph(self):
        start = self
        if start.edges==[]:
            print('vertex has no edges!')
            return
        dot = Digraph()
        self.build_graph(dot, {}, {})
        dot.render('graph', format='png', view=True)    

from name_generator import name_gen
import string
import random
import numpy as np

trie = name_gen()
num_names = 10
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
