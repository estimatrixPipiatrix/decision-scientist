import torch
import torch.nn as nn

# Assuming we have a classification problem with 2 classes
num_classes = 2

# Generate some random predictions and target labels
batch_size = 3
predictions = torch.randn(batch_size, num_classes) 
target_labels = torch.tensor([0, 1, 0])  

# Create an instance of NLLLoss
loss_function = nn.NLLLoss()

# Compute the loss
loss = loss_function(torch.log_softmax(predictions, dim=1), \
                     target_labels)

print(loss.item())

# so the target_labels are just a vector, where each element
# of the vector is an integer that represents the class that
# the output should get assigned. so, e.g., if our classes were
# cat = 0 and dog = 1, target_labels should be a sequence of
# 1s and 0s
