import torch
import torch.nn as nn
from self_attention import self_attention

class transformer(nn.Module):
    def __init__(self,vec_dim,num_heads):
        super().__init__()

        self.attention = self_attention(vec_dim,num_heads)

        self.norm1 = nn.LayerNorm(vec_dim)
        self.norm2 = nn.LayerNorm(vec_dim)

        dim_multiplier = 4
        self.feed_forward = nn.Sequential( \
            nn.Linear(vec_dim,dim_multiplier*vec_dim),
            nn.ReLU(),
            nn.Linear(dim_multiplier*vec_dim,vec_dim))

    def forward(self,x):
        attended = self.attention(x)
        x = self.norm1(attended+x)

        feed_forward = self.feed_forward(x)
        return self.norm2(feed_forward+x)
