from sklearn.datasets import load_wine
import graphviz
from graphviz import Digraph
import pandas as pd
import numpy as np
from scipy import stats
import sys

class tree_node:
    def __init__(self,val):
        self.value = val
        self.split_on = ''
        self.left = None
        self.right = None

data = load_wine()
wine = pd.DataFrame(data['data'],columns=data['feature_names'])
# convert the numerical data into simple low/high class values
for column in wine.columns:
    median = wine[column].median()
    for i in range(wine[column].shape[0]):
        if wine.loc[i,column]>median:
            wine.loc[i,column] = 'high'
        else:
            wine.loc[i,column] = 'low'
target = data.target
classes = [0,1,2]
split_vals = ['low','high']

def entropy(target,classes):
    class_counts = []
    for c in classes:
        class_counts.append(target[target==c].shape[0])
    class_counts = np.array(class_counts)
    if class_counts.sum()!=0:
        class_probs = class_counts/class_counts.sum()
    else:
        class_probs = np.zeros(len(class_counts))
    S = 0
    for prob in class_probs:
        if prob!=0:
            S -= prob*np.log2(prob)
    return S

def info_gain(data_set,col_name,split_vals,target,classes):
    start_entropy = entropy(target,classes)
    split_entropies = []
    num_records = data_set.shape[0]
    split_fractions = []
    for split_val in split_vals:
        split_set = target[data_set[col_name]==split_val]
        split_fractions.append(split_set.shape[0]/num_records)
        split_entropies.append(entropy(split_set,classes))

    split_fractions = np.array(split_fractions)
    split_entropies = np.array(split_entropies)
    gain = \
        start_entropy - (split_fractions*split_entropies).sum()
    return gain

def decision_tree(data_set,split_vals,target,classes,root_node, \
                  max_level,curr_level=1,side=None):
    cols = data_set.columns
    info_gains = []
    for col in cols:
        gain = info_gain(data_set,col,split_vals,target,classes)
        info_gains.append(gain)
    info_gains = np.array(info_gains)
    index_max = info_gains.argmax()
    split_on = cols[index_max]
    if side==None:
        root_node.value=split_on
    else:
        root_node.value=split_on+side

    data_left = data_set[data_set[split_on]==split_vals[0]]
    target_left = target[data_set[split_on]==split_vals[0]]
    data_right = data_set[data_set[split_on]==split_vals[1]]
    target_right = target[data_set[split_on]==split_vals[1]]
    data_left = data_left.drop(split_on,axis=1)
    data_right = data_right.drop(split_on,axis=1)
    if curr_level<=max_level:
        curr_level += 1
        node_left = tree_node(None)
        node_right = tree_node(None)
        root_node.left = \
            decision_tree(data_left,split_vals,target_left, \
                          classes,node_left,max_level,curr_level, \
                          ' ')
        root_node.right = \
            decision_tree(data_right,split_vals,target_right, \
                          classes,node_right,max_level,curr_level, \
                          '')
    else:
        prob_0 = np.round((target_left==0).sum()/len(target_left),1)
        prob_1 = np.round((target_left==1).sum()/len(target_left),1)
        prob_2 = np.round((target_left==2).sum()/len(target_left),1)
        root_node.left = tree_node([prob_0,prob_1,prob_2])
        prob_0 = np.round((target_right==0).sum()/len(target_right),1)
        prob_1 = np.round((target_right==1).sum()/len(target_right),1)
        prob_2 = np.round((target_right==2).sum()/len(target_right),1)
        root_node.right = tree_node([prob_0,prob_1,prob_2])
    return root_node

def build_graph(node, dot):
    if node is not None:
        # create a node with the node's value
        dot.node(str(node.value))
        if node.left is not None:
            # create an edge to the left child
            dot.edge(str(node.value), str(node.left.value), \
                     label="low")
            build_graph(node.left, dot)
        if node.right is not None:
            # create an edge to the right child
            dot.edge(str(node.value), str(node.right.value), \
                     label="high")
            build_graph(node.right, dot)

def display_tree(root_node):
    root = root_node
    if root==None:
        print('no tree to display!')
        return
    dot = Digraph()
    build_graph(root, dot)
    dot.render('tree', format='png', view=True)
        
root_node = tree_node(None)
node = decision_tree(wine,split_vals,target,classes,root_node,1)
display_tree(node)
