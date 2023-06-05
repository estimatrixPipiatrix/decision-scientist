import graphviz
from graphviz import Digraph

class node:
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

class bin_search_tree:
    def __init__(self):
        self.root = None

    def search(self,node,val):
        if node == None:
            return node
        elif (node.value == val):
            return node
        if val < node.value:
            return self.search(node.left,val)
        if val > node.value:
            return self.search(node.right,val)

    def find_parent(self,node,val):
        if val<node.value:
            if val==node.left.value:
                return node
            else:
                return self.find_parent(node.left,val)
        elif val>node.value:
            if val==node.right.value:
                return node
            else:
                return self.find_parent(node.right,val)
        else:
            return None

    def insert(self,parent,val):
        if parent == None:
            n = node(val)
            self.root = n
            return
        if val < parent.value:
            if parent.left == None:
                n = node(val)
                parent.left = n
            else:
                self.insert(parent.left,val)
        elif val > parent.value: 
            if parent.right == None:
                n = node(val)
                parent.right = n
            else:
                self.insert(parent.right,val)

    def build_graph(self, node, dot):
        if node is not None:
            # create a node with the node's value
            dot.node(str(node.value))
            if node.left is not None:
                # create an edge to the left child
                dot.edge(str(node.value), str(node.left.value))
                self.build_graph(node.left, dot)
            if node.right is not None:
                # create an edge to the right child
                dot.edge(str(node.value), str(node.right.value)) 
                self.build_graph(node.right, dot) 

    def delete(self,val):
        node = self.search(self.root,val)
        if node==None:
            print('target node not found!')
            return
        if (node.left==None and node.right==None):
            if node==self.root:
                self.root = None
                return
            parent = self.find_parent(self.root,val)
            if parent != None:
                if val<parent.value:
                    parent.left = None
                elif val>parent.value:
                    parent.right = None
        elif (node.left!=None and node.right==None):
            node.value = node.left.value
            node.right = node.left.right
            node.left = node.left.left
        elif (node.left==None and node.right!=None):
            node.value = node.right.value
            node.left = node.right.left
            node.right = node.right.right
        else:
            successor = node.right
            while successor.left!=None:
                successor = successor.left
            successor_val = successor.value
            self.delete(successor_val)
            node.value = successor_val

    def display_tree(self):
        root = self.root
        if root==None:
            print('no tree to display!')
            return
        dot = Digraph()
        self.build_graph(root, dot)
        dot.render('tree', format='png', view=True)

    def print_tree(self,node):
        if node==None:
            return None
        if node.left!=None:
            self.print_tree(node.left)
        print(node.value)
        if node.right!=None:
            self.print_tree(node.right)

    def return_max(self,node):
        if node == None:
            return
        if node.right == None:
            return node.value
        return self.return_max(node.right)

import numpy as np
np.random.seed(2)
bst = bin_search_tree()
data = np.random.randint(0,50,50)
tree_data = []
seen_before = {}
for n in data:
    if seen_before.get(n)==None:
        tree_data.append(n)
    seen_before.update({n:True})

for n in tree_data:
    bst.insert(bst.root,n)
#bst.display_tree()
