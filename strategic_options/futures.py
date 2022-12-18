import pandas as pd

options = pd.read_csv('options.csv')

# a1: i am able to make a significant difference
#     in the field of ai alignment
prob_a1 = 0.10

# a2: am not able to make difference
prob_a2 = 1.0-prob_a1

options['f1'] = [7,5,9,7,10]
options['f2'] = [9,6,9,8,7]

options['score'] = \
    prob_a1*options['f1'] + \
    prob_a2*options['f2'] 
