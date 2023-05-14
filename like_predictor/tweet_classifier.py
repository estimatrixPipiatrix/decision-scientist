import torch
import torch.nn as nn
import torch.nn.functional as F
from transformer import transformer

class tweet_classifier(nn.Module):
    # vec_dim = dimension of the vector that a word maps to in
    #           the word embedding and also that a position
    #           maps to in the position embedding
    # seq_length = length of the sentence for the positional
    #              embedding
    # num_words = size of the dictionary for the word embedding
    def __init__(self,vec_dim,num_heads,depth,seq_length, \
                 num_words,num_classes):
        super().__init__()

        self.num_words = num_words
        self.word_emb = nn.Embedding(num_words,vec_dim)
        self.pos_emb = nn.Embedding(seq_length,vec_dim)

        tblocks = []
        for i in range(depth):
            tblocks.append(transformer(vec_dim=vec_dim, \
                                       num_heads=num_heads))
        self.tblocks = nn.Sequential(*tblocks)

        self.toprobs = nn.Linear(vec_dim,num_classes)

    def forward(self,x):
        # x: A (batch_size, sent_len) tensor of integer values 
        #    representing words (in some predetermined vocabulary).
        # output: A (batch_size, num_classes) tensor of 
        #         log probabilities over the classes

        # generate word embeddings
        words = self.word_emb(x)
        batch_size, sent_len, vec_dim = words.size()

		# generate position embeddings
        positions = torch.arange(sent_len)
        positions = self.pos_emb(positions)[None, :, :]. \
                    expand(batch_size,sent_len,vec_dim)

        x = words + positions
        x = self.tblocks(x)

        # Average-pool over the sent_len dimension and project 
        # to class probabilities
        x = self.toprobs(x.mean(dim=1))
        return F.log_softmax(x, dim=1)
