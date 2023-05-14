# here is some code to illustrate how nn.Embedding works
import torch
import torch.nn as nn

sent_1 = 'hello world'
sent_2 = 'hello kitty'

# the dictionary size is 3 because we have only three words:
# hello, world, and kitty
dict_size = 3

# we will embed these words into 5 dimensional vectors
embed_dim = 5

# create a set with all the words in our dictionary
word_set_1 = set(sent_1.split())
word_set_2 = set(sent_2.split())
word_set = word_set_1.union(word_set_2)

# create a dictionary that assigns an index to each word
vocab = {word: index for index, word in enumerate(word_set)}

# convert each sentence into a vector of indices and put both
# into a tensor
indices_1 = [vocab[word] for word in word_set_1]
indices_2 = [vocab[word] for word in word_set_2]
sentences = torch.tensor([indices_1,indices_2])

# form the embedding layer
embedding = nn.Embedding(dict_size,embed_dim)

# because each sentence contains 2 words, we will get out a
# matrix with 2 rows for that sentence, and each row will contain
# the embedding for the corresponding word; because we have 2
# sentences, we'll get back 2 such matrices
sentences_emb = embedding(sentences)
