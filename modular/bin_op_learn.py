import numpy as np
import pandas as pd
import sys
import json
import pickle

# the number of layers must be at least three
num_layers    = 7
# number of neurons in the hidden, input, and output layers
num_hidden    = num_layers-2
# modulus for the binary arithmetic operation
modulus       = 2
num_input     = 2*modulus
num_output    = modulus
layers_list   = list()
for i in range(num_layers):
    if (i==0):
        layer = np.zeros((1,num_input))
    elif (i==(num_layers-1)):
        layer = np.zeros((1,num_output))
    else:
        layer = np.zeros((1,num_hidden))
    layers_list.append(layer)

weights_list = list()
weight_corrects_list = list()
np.random.seed(4)
for i in range(num_layers-1):
    if (i==0):
        weights = 2.0*np.random.random((num_input,num_hidden))
    elif (i==(num_layers-2)):
        weights = 2.0*np.random.random((num_hidden,num_output))-1.0
    else:
        weights = 2.0*np.random.random((num_hidden,num_hidden))-1.0
    weights_list.append(weights)
    weight_corrects_list.append(np.zeros((num_hidden,num_hidden)))

# define the activation functions and their derivatives
# layer_type = 1 will return tanh (or its derivative)
# layer_type = 2 will return softmax (or its derivative)
def activ_func(x,layer_type):
    if (layer_type==1):
        return np.tanh(x)
    elif (layer_type==2):
        return np.exp(x)/np.exp(x).sum()

def activ_deriv(x,layer_type):
    if (layer_type==1):
        return 1.0-np.tanh(x)**2.0
    elif (layer_type==2):
        soft_max = np.exp(x)/np.exp(x).sum()
        return soft_max*(1.0-soft_max)

# set up the test and training data for binary operation of
# modular addition; the inputs and outputs are 1-hot endcoded
num_train = 10000
num_test  = 10000
Xtrain_pre = np.random.randint(0,modulus,(num_train,2))
Xtest_pre  = np.random.randint(0,modulus,(num_test,2))
ytrain_pre = np.mod(Xtrain_pre[:,0]+Xtrain_pre[:,1],modulus)
ytest_pre  = np.mod(Xtest_pre[:,0]+Xtest_pre[:,1],modulus)
Xtrain = np.zeros((num_train,num_input))
Xtest  = np.zeros((num_test,num_input))
for i in range(num_train):
    Xtrain[i,Xtrain_pre[i,0]]=1.0
    Xtrain[i,Xtrain_pre[i,1]+modulus]=1.0
for i in range(num_test):
    Xtest[i,Xtest_pre[i,0]]=1.0
    Xtest[i,Xtest_pre[i,1]+modulus]=1.0

# one-hot encode the target outputs
ytrain = np.zeros((num_train,modulus))
ytest  = np.zeros((num_test,modulus))
for i in range(num_train):
    ytrain[i,ytrain_pre[i]]=1.0
for i in range(num_test):
    ytest[i,ytest_pre[i]]=1.0

# train the model
alpha     = 0.0001
err_tol   = 0.1
max_iter  = 500
iter_num  = 0
err       = 1.e5
while ((iter_num<max_iter)&(err>err_tol)):
    err = 0.0
    for i in range(num_train):
        layers_list[0] = Xtrain[i]
        for j in range(1,num_layers-1):
            layers_list[j] = \
                    activ_func(np.matmul(layers_list[j-1], \
                               weights_list[j-1]),1)
        layers_list[num_layers-1] = \
            activ_func(np.matmul(layers_list[num_layers-2], \
                       weights_list[num_layers-2]),2)

        # backprop step
        # form the diagonal activation derivative matrices
        delta = (layers_list[num_layers-1]-ytrain[i])
        delta = delta.reshape(1,ytrain.shape[1])
        diag_activs = list()
        # NB: the ith entry in diag_activs corresponds to the
        #     (i+1)th layer, so entry 0 is for the 1st layer, etc
        for j in range(1,num_layers-1):
            activ_der = activ_deriv(layers_list[j],1)
            diag_mat = np.diag(activ_der)
            diag_activs.append(diag_mat)

        activ_der = activ_deriv(layers_list[num_layers-1],2)
        diag_mat = np.diag(activ_der)
        diag_activs.append(diag_mat)

        # form the products of the weights and diagonals
        mat_prods = list()
        mat_prods.append(np.matmul(delta,diag_activs[num_layers-2]))
        for j in range(num_layers-2):
            mat1 = weights_list[num_layers-2-j].T
            mat2 = diag_activs[num_layers-3-j]
            new_mat = np.matmul(mat1,mat2)
            tot_mat = np.matmul(mat_prods[j],new_mat)
            mat_prods.append(tot_mat)

        for j in range(len(weights_list)):
            weight_corrects_list[j] = \
                -alpha*np.outer(layers_list[num_layers-2-j], \
                                mat_prods[j])
            weights_list[num_layers-2-j] += weight_corrects_list[j]

        err += (delta**2.0).sum()

    err /= num_train
    print(iter_num,err)

    iter_num += 1

print('converged on iteration: ',iter_num)
print('training set error: ',err)

# check how well the model predicts out of sample
num_correct = 0.0
for i in range(num_test):
    layers_list[0] = Xtest[i]
    for j in range(1,num_layers-1):
        layers_list[j] = \
                activ_func(np.matmul(layers_list[j-1], \
                           weights_list[j-1]),1)
    layers_list[num_layers-1] = \
        activ_func(np.matmul(layers_list[num_layers-2], \
                   weights_list[num_layers-2]),2)

    pred_answer = layers_list[num_layers-1].argmax()
    true_answer = ytest[i].argmax()

    if (pred_answer==true_answer):
        num_correct += 1.0

percent_correct = (num_correct/num_test)*100.0
print('percent correct out of sample: ',percent_correct)

with open("weights.pkl", "wb") as f:
    pickle.dump(weights_list,f)
with open("Xtest.pkl","wb") as f:
    pickle.dump(Xtest,f)
with open("ytest.pkl","wb") as f:
    pickle.dump(ytest,f)
