# give the first few letters and this routine will suggest D&D
# names that start with those letters :)

from class_trie import prefix_tree
import pandas as pd
import numpy as np

def name_gen():
    name_table = pd.read_csv("Kismets_Name_Compendium.csv")

    name_list = []
    for i in range(name_table.shape[0]):
        for j in range(name_table.shape[1]):
            current_name = name_table.iloc[i,j]
            if type(current_name)==str:
                name_list.append(current_name.lower())

    trie = prefix_tree()
    for n in name_list:
        use_freq = np.random.randint(1,11)
        trie.insert_str(n,use_freq)
    return trie
