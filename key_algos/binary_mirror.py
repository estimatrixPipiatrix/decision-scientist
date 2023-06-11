# check to see whether a binary tree is bilaterally symmetric

class tree_node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

root_node = tree_node(2)
root_node.left = tree_node(3)
root_node.right = tree_node(3)
root_node.left.left = tree_node(4)
root_node.left.right = tree_node(6)
root_node.right.left = tree_node(6)
root_node.right.right = tree_node(4)
root_node.left.left.left = tree_node(2)
root_node.left.left.right = tree_node(7)
root_node.right.right.right = tree_node(2)
root_node.right.right.left = tree_node(7)

def tree_to_list(node,elements=[],parity=0):
    elements.append(node.value)
    if parity==0:
        if node.left!=None:
            tree_to_list(node.left,elements,0)
        if node.right!=None:
            tree_to_list(node.right,elements,0)
    elif parity==1:
        if node.right!=None:
            tree_to_list(node.right,elements,1)
        if node.left!=None:
            tree_to_list(node.left,elements,1)
    return elements

def is_mirror(root_node):
    left_tree = tree_to_list(root_node.left,[],0)
    right_tree = tree_to_list(root_node.right,[],1)
    if left_tree==right_tree:
        return True
    else:
        return False

print(is_mirror(root_node))
    
