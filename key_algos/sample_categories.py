# given a list of categories, e.g. ['A','B','C','D'], sample 
# them randomly according to a weight scheme. for example, if
# w_A = 5 and w_B = 10, then B should show up twice as often as A
import numpy as np

cats = ['A','B','C','D']
weights = [5,10,15,25]

def sample_with_weights(cats,weights):
    weights = np.array(weights)
    weight_sum = weights.sum()
    sample = np.random.randint(0,weight_sum)
    cum_sum = 0
    index = 0
    while sample>=cum_sum:
        cum_sum += weights[index]
        index += 1
    index -= 1
    print(cum_sum,sample,index)
    return cats[index]

print(sample_with_weights(cats,weights))
