from math import floor
import graphviz
from graphviz import Digraph

class heap:
    def __init__(self):
        self.root = []

    def insert(self,val):
        heap = self.root
        heap.append(val)
        child = len(heap)-1
        parent = self.parent_index(child)
        if parent < child:
            while (heap[parent]<heap[child] and parent>=0):
                tmp = heap[parent]
                heap[parent] = heap[child]
                heap[child]  = tmp
                child = parent
                parent = self.parent_index(child)

    def delete(self):
        heap = self.root
        if heap==[]:
            print('nothing to delete!')
            return
        if len(heap)==1:
            self.root = []
            return
        heap[0] = heap.pop()
        parent = 0
        self.trickle_down(heap,parent)

    def trickle_down(self,heap,parent):
        left,right=self.child_indices(parent)
        if left<len(heap) and right<len(heap):
            if heap[left]>heap[right]:
                max_child = left
            elif heap[right]>heap[left]:
                max_child = right
            if heap[max_child]>heap[parent]:
                tmp = heap[parent]
                heap[parent] = heap[max_child]
                heap[max_child] = tmp
                parent = max_child
                self.trickle_down(heap,parent=max_child)
        elif left<len(heap):
            if heap[left]>heap[parent]:
                tmp = heap[parent]
                heap[parent] = heap[left]
                heap[left] = tmp
                parent = left
                self.trickle_down(heap,parent=left)
        elif right<len(heap):
            if heap[right]>heap[parent]:
                tmp = heap[parent]
                heap[parent] = heap[right]
                heap[right] = tmp
                parent = right
                self.trickle_down(heap,parent=right)
        else:
            return

    def parent_index(self,child_index):
        return floor((child_index-1)/2.0)

    def child_indices(self,parent_index):
        return [2*parent_index+1,2*parent_index+2]

    def build_graph(self,index,dot):
        heap = self.root
        if heap != []:
            # create a node with the node's value
            dot.node(str(heap[index]))
            children = self.child_indices(index)
            left = children[0]
            right = children[1]
            if left<len(heap):
                # create an edge to the left child
                dot.edge(str(heap[index]), str(heap[left]))
                self.build_graph(left, dot)
            if right<len(heap):
                # create an edge to the right child
                dot.edge(str(heap[index]), str(heap[right]))
                self.build_graph(right, dot)

    def display_tree(self):
        root = self.root
        if root==[]:
            print('no tree to display!')
            return
        dot = Digraph()
        self.build_graph(0, dot)
        dot.render('tree', format='png', view=True)

import numpy as np
hc = heap()
np.random.seed(5)
data = np.random.randint(0,50,3)
tree_data = []
seen_before = {}
for n in data:
    if seen_before.get(n)==None:
        tree_data.append(n)
    seen_before.update({n:True})

for n in tree_data:
    hc.insert(n)
#hc.display_tree()
