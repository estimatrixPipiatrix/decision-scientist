import torch.nn as nn
import torch
import torch.nn.functional as F

class self_attention(nn.Module):
    def __init__(self,vec_dim,num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.vec_dim   = vec_dim

        self.to_keys     = nn.Linear(vec_dim,vec_dim,bias=False)
        self.to_queries  = nn.Linear(vec_dim,vec_dim,bias=False)
        self.to_values   = nn.Linear(vec_dim,vec_dim,bias=False)
        self.unify_heads = nn.Linear(vec_dim,vec_dim,bias=False)

    def forward(self,x):
        num_batches, num_vecs, vec_dim = x.size()
        num_heads = self.num_heads

        trunc_dim = vec_dim // num_heads
        
        queries = self.to_queries(x)
        keys    = self.to_keys(x)
        values  = self.to_values(x)

        queries = \
            queries.view(num_batches,num_vecs,num_heads,trunc_dim)
        keys =    \
            keys.view(num_batches,num_vecs,num_heads,trunc_dim)
        values =  \
            values.view(num_batches,num_vecs,num_heads,trunc_dim)

        keys = keys.transpose(1, 2).contiguous(). \
            view(num_batches*num_heads,num_vecs,trunc_dim)
        queries = queries.transpose(1, 2).contiguous(). \
            view(num_batches*num_heads,num_vecs,trunc_dim)
        values = values.transpose(1, 2).contiguous(). \
            view(num_batches*num_heads,num_vecs,trunc_dim)

        dot_prod = torch.bmm(queries, keys.transpose(1, 2))
        dot_prod = dot_prod / (vec_dim**(1.0/2.0))
        dot_prod = F.softmax(dot_prod, dim=2)

        out = torch.bmm(dot_prod, values). \
            view(num_batches,num_heads,num_vecs,trunc_dim)
        out = out.transpose(1, 2).contiguous(). \
            view(num_batches,num_vecs,trunc_dim*num_heads)
        self.unify_heads(out)

        return out
