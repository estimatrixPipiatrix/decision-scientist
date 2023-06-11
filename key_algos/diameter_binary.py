import graphviz
from graphviz import Digraph
# write a function that returns the diameter of a binary tree

# it's the maximum of:
# the diameter of T’s left subtree.
# the diameter of T’s right subtree.
# the longest path between leaves that goes through the root of T 
# = height of left subtree + height of right subtree + 1

class tree_node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

root_node = tree_node(2)
root_node.left = tree_node(3)
root_node.right = tree_node(1)
root_node.left.left = tree_node(4)
root_node.left.right = tree_node(10)
root_node.right.left = tree_node(6)
root_node.right.right = tree_node(8)
root_node.left.left.left = tree_node(5)
root_node.left.left.right = tree_node(11)
root_node.right.right.right = tree_node(15)
root_node.right.right.left = tree_node(7)
root_node.right.right.left.right = tree_node(9)
root_node.right.right.left.right.left = tree_node(20)

def build_graph(node, dot):
    if node is not None:
        # create a node with the node's value
        dot.node(str(node.value))
        if node.left is not None:
            # create an edge to the left child
            dot.edge(str(node.value), str(node.left.value))
            build_graph(node.left, dot)
        if node.right is not None:
            # create an edge to the right child
            dot.edge(str(node.value), str(node.right.value))
            build_graph(node.right, dot)

def display_tree(node):
    root = node
    if root==None:
        print('no tree to display!')
        return
    dot = Digraph()
    build_graph(root, dot)
    dot.render('tree', format='png', view=True)

def tree_height(root_node):
    if root_node==None:
        return 0
    if root_node.left!=None and root_node.right!=None:
        return max(tree_height(root_node.left), \
                   tree_height(root_node.right))+1
    elif root_node.left!=None:
        return tree_height(root_node.left)+1
    elif root_node.right!=None:
        return tree_height(root_node.right)+1
    else:
        return 0

def tree_diameter(root_node):
    ans1 = tree_height(root_node.left)+ \
           tree_height(root_node.right) + 3
    if root_node.left!=None:
        ans2 = tree_diameter(root_node.left)
    else:
        ans2 = 0
    if root_node.right!=None:
        ans3 = tree_diameter(root_node.right)
    else:
        ans3 = 0
    result = max(ans1,ans2)
    return max(result,ans3)

print(tree_diameter(root_node))
