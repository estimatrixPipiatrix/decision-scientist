import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay,accuracy_score, \
                            confusion_matrix
import seaborn as sns; sns.set()
import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
import torch.nn as nn

part_data = pd.read_csv('part_data.csv')
X = part_data.iloc[:,0:6].to_numpy()
y = part_data.iloc[:,7].to_numpy()

Xtrain,Xtest,ytrain,ytest = train_test_split(X,y)
Xtrain = torch.from_numpy(Xtrain)
ytrain = torch.from_numpy(ytrain)
Xtest  = torch.from_numpy(Xtest)

train_ds = TensorDataset(Xtrain,ytrain)
batch_size = 10
train_dl = DataLoader(train_ds,batch_size,shuffle=True)

class Model(nn.Module):
    def __init__(self,input_size,hidden_size,output_size):
        super().__init__()
        self.layer1 = nn.Linear(input_size,hidden_size)
        self.layer2 = nn.Linear(hidden_size,output_size)
    def forward(self,x):
        x = self.layer1(x)
        x = nn.Sigmoid()(x)
        x = self.layer2(x)
        return x

input_size  = 6
hidden_size = 20
output_size = 1
model = Model(input_size,hidden_size,output_size)

learning_rate = 0.01
loss_fn = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(),lr=learning_rate)
num_epochs = 100
loss_hist = [0]*num_epochs
for epoch in range(num_epochs):
    for x_batch,y_batch in train_dl:
        x_batch = x_batch.squeeze()
        x_batch = x_batch.type(torch.float32)
        y_batch = y_batch.type(torch.float32)
        pred = model(x_batch).squeeze()
        loss = loss_fn(pred,y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
    loss_hist[epoch] += loss.item()
    print(loss.item())

Xtest = Xtest.type(torch.float32)
pred_test = torch.zeros(ytest.shape)
for i,record in enumerate(Xtest):
    ypred = model(record)
    pred_test[i] = ypred.round()
pred_test = pred_test.detach().numpy().astype(int)
accuracy = accuracy_score(pred_test,ytest)
print('percent accurate OOS: ',accuracy*100.0)
cm = confusion_matrix(ytest,pred_test)
labels=[1,2,3,4,5]
disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=labels)
disp.plot()
plt.grid(False)
plt.show()
