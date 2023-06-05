import graphviz
from graphviz import Digraph
import sys

class trie_node:
    def __init__(self):
        self.children = {}

class prefix_tree:
    def __init__(self):
        self.root = trie_node()

    def insert_str(self,string,use_freq=5):
        # use_freq is from 1, very infrequent, to 10,
        # very frequent
        current = self.root.children
        key = string[0]
        if current.get(key)==None:
            current.update({key:trie_node()})
        for n in string[1:len(string)]:
            current = current[key].children
            key = n
            if current.get(key)==None:
                current.update({key:trie_node()})
        current = current[key].children
        key = "*"
        current.update({key:use_freq})

    def find_word(self,string):
        current = self.root
        for n in string:
            if current.children.get(n)!=None:
                current = current.children[n]
            else:
                return None
        return current

    def find_all_words(self,start_node,word="",words=[]):
        if word=="":
            words = []
        keys = start_node.children.keys()
        prefix = word
        for n in keys:
           if n=="*":
               words.append((start_node.children[n],word))
           else:
               word += n
               next = start_node.children[n]
               self.find_all_words(next,word,words)
           word = prefix
        return words

    def autocomplete(self,prefix):
        current = self.find_word(prefix)
        if current == None:
            return
        suggestions = self.find_all_words(current)
        return [x for _, x in sorted(suggestions)][::-1]

    def autocorrect(self,prefix):
        # cycle through all substrings of prefix
        substring = []
        max_common = 0
        cur_common = 0
        best_string = ""
        for n in prefix:
            substring.append(n)
            similar = self.find_word(substring)
            if similar!=None:
                for item in self.find_all_words(similar):
                    cur_string = item[1]
                    comp_string = prefix
                    comp_string_set = set(comp_string)
                    cur_string_set = set(cur_string)
                    cur_common = \
                        len(comp_string_set.intersection \
                            (cur_string_set))
                    if cur_common>max_common:
                        max_common = cur_common
                        best_string = prefix[0] + cur_string
        return best_string

    def build_graph(self, trie_node, dot):
        current = trie_node.children
        keys = current.keys()
        for n in keys:
            if n!="*":
                A = str(trie_node)
                B = str(current[n])
                if trie_node.children.get("*")!=None:
                    dot.node(A,"*",shape="rect")
                else:
                    dot.node(A,"",shape="rect")
                dot.node(B,"",shape="rect")
                dot.edge(A,B,label=n)
                if current[n].children.get("*")!=None:
                    dot.node(B,"*",shape="rect")
                else:
                    dot.node(B,"",shape="rect")
                self.build_graph(current[n],dot)

    def display_trie(self):
        root = self.root
        if root.children=={}:
            print('no tree to display!')
            return
        dot = Digraph()
        self.build_graph(root, dot)
        dot.render('tree', format='png', view=True)

    def print_keys(self,start_node):
        current_keys = []
        for n in start_node.children.keys():
            current_keys.append(n)
            if n!="*":
                self.print_keys(start_node.children[n])
        print(current_keys)

import numpy as np
trie = prefix_tree()
word_list = ["tweet","poast","poaster","twitter","tweeps", \
             "two","huel","hello"]
for n in word_list:
    use_freq = np.random.randint(1,11)
    trie.insert_str(n,use_freq)
