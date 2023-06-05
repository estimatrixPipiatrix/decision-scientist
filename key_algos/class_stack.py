class node:
    def __init__(self,data_val):
        self.data_val = data_val
        self.below = None

class stack:
    def __init__(self):
        self.below = None

    def push(self,data_val):
        new_item = node(data_val)
        new_item.below = self.below
        self.below = new_item

    def pop(self):
        self.below = self.below.below

    def print(self):
        current = self.below
        while current is not None:
            print(current.data_val)
            current = current.below

import numpy as np

# burgertime example
#enemies = np.random.randint(0,3,10)
#names = {0:'pesky pickle',1:'homicidal hot dog',2:'egregious egg'}
#s = stack()
#for e in enemies:
#    s.push(names[e])
#s.print()
