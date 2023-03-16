import numpy as np
import sys
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

np.random.seed(3)

# load X_conv and y_conv
Xconv_load   = np.load('X_conv.npz',allow_pickle=True)
yconv_load   = np.load('y_conv.npz',allow_pickle=True)

Xconv = Xconv_load['arr_0'].astype('float64')
yconv = yconv_load['arr_0'].astype('float64')

num_total = Xconv.shape[0]
num_soft_max = int(yconv.shape[1]/3)

for i in range(num_total):
   max_ind = yconv[i,2*num_soft_max:3*num_soft_max].argmax()
   yconv[i,2*num_soft_max:3*num_soft_max] = 0.0
   yconv[i,2*num_soft_max+max_ind] = 1.0

# set up the training and test samples
percent_train = 0.9
num_train = int(np.round(num_total*percent_train))
num_test  = num_total-num_train
Xtrain    = Xconv[0:num_train]
ytrain    = yconv[0:num_train]
Xtest     = Xconv[num_train:num_train+num_test]
ytest     = yconv[num_train:num_train+num_test]

# moving window of size frame_rows x frame_cols moves over
# every position in the image, such that the frame does not
# move outside the image, and captures part of the image
# for each of those positions
def capture_frames(image,frame_rows,frame_cols):
    image_rows = image.shape[0]
    image_cols = image.shape[1]
    frame_pos_horz = image_cols-frame_cols+1
    frame_pos_vert = image_rows-frame_rows+1
    captured_frames = np.zeros((frame_pos_horz*frame_pos_vert, \
                               frame_rows,frame_cols))
    for i in range(frame_pos_horz):
        for j in range(frame_pos_vert):
            single_frame = image[i:i+frame_rows,j:j+frame_cols]
            captured_frames[frame_pos_vert*i+j,:,:]=single_frame
    return captured_frames.reshape(frame_pos_horz*frame_pos_vert, \
                                   frame_rows*frame_cols).T

# define the activation functions and their derivatives
# layer_num = 1 will return the function for layer 1 and
# layer_num = 2 will return that for layer 2
def activ_func(x,layer_num):
    if (layer_num==1):
        return np.tanh(x)
    elif (layer_num==2):
        num_soft_max = int(x.shape[1]/3)
        soft_max1 = np.exp(x[0,0:num_soft_max]) \
                /np.exp(x[0,0:num_soft_max]).sum()
        soft_max2 = np.exp(x[0,num_soft_max:2*num_soft_max]) \
                /np.exp(x[0,num_soft_max:2*num_soft_max]).sum()
        soft_max3 = np.exp(x[0,2*num_soft_max:3*num_soft_max]) \
                /np.exp(x[0,2*num_soft_max:3*num_soft_max]).sum()
        soft_max1 = soft_max1.reshape(1,num_soft_max)
        soft_max2 = soft_max2.reshape(1,num_soft_max)
        soft_max3 = soft_max3.reshape(1,num_soft_max)
        out_vec = np.concatenate((soft_max1,soft_max2),axis=1)
        return np.concatenate((out_vec,soft_max3),axis=1)

def activ_deriv(x,layer_num):
    if (layer_num==1):
        return 1.0-np.tanh(x)**2.0
    elif (layer_num==2):
        soft_max = activ_func(x,2)
        num_soft_max = int(x.shape[1]/3)
        soft_deriv = soft_max*(1.0-soft_max).reshape(1,3*num_soft_max)
        return soft_deriv

def dirac_delta(x,y):
    return (x==y).astype('int64')

init_factor = 1.0

frame_rows = 2
frame_cols = 2
num_kernels = 3
image_rows = Xtrain[0].shape[0]
image_cols = Xtrain[0].shape[1]
frame_pos_horz = image_cols-frame_cols+1
frame_pos_vert = image_rows-frame_rows+1
# N.B.: if the weights are initialized lying too close together,
# gradient descent will not find many distinct kernels!
kernels = init_factor*np.random.random((num_kernels, \
                      frame_rows*frame_cols))-init_factor/2.0
grad_kernel = np.zeros((num_kernels,frame_rows*frame_cols))

#set up the fully connected layers

# the number of layers must be at least three
num_layers    = 4
# number of neurons in the hidden, input, and output layers
num_hidden    = 30
num_input     = frame_pos_horz*frame_pos_vert
num_output    = ytrain.shape[1]
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
for i in range(num_layers-1):
    if (i==0):
        weights = init_factor* \
           np.random.random((num_input,num_hidden))-init_factor/2.0
    elif (i==(num_layers-2)):
        weights = init_factor* \
            np.random.random((num_hidden,num_output))-init_factor/2.0
    else:
        weights = init_factor* \
            np.random.random((num_hidden,num_hidden))-init_factor/2.0
    weights_list.append(weights)
    weight_corrects_list.append(np.zeros((num_hidden,num_hidden)))

alpha = 0.001
max_iter = 500
err_tol  = 0.1
err = 1000.0
iter = 0
dropout = 1
while ((iter<max_iter) & (err>err_tol)):
    err = 0.0
    for n in range(Xtrain.shape[0]):
        # forward propagation convolution + pooling steps
        image = Xtrain[n]
        image_frames = capture_frames(image, \
                                      frame_rows,frame_cols)

        # form layer_0 pre-pooling step
        layer_0_pre = np.zeros((num_kernels,image_frames.shape[1]))
        for k in range(num_kernels):
            layer_0_pre[k,:]= \
                np.matmul(kernels[k].reshape(1,len(kernels[k])), \
                          image_frames)
        which_kernel = np.argmax(layer_0_pre,axis=0)

        # pooling step
        layer_0 = \
            np.max(layer_0_pre,axis=0).reshape(1,layer_0_pre.shape[1])
        layer_0 = activ_func(layer_0,1)

        # forward propagation to the other layers
        layers_list[0] = layer_0
        for j in range(1,num_layers-1):
            layers_list[j] = \
                    activ_func(np.matmul(layers_list[j-1], \
                               weights_list[j-1]),1)
        layers_list[num_layers-1] = \
            activ_func(np.matmul(layers_list[num_layers-2], \
                       weights_list[num_layers-2]),2)

        # set dropout mask for the hidden layers that all have
        # the same size
        if (dropout==1):
            mask_rows = num_layers-2
            mask_cols = num_hidden
            dropout_mask = np.random.randint(0,2, \
                                            (mask_rows,mask_cols))
            for m in range(1,mask_rows+1):
                layers_list[m] = 2.0*dropout_mask[m-1]*layers_list[m]

        # backprop step for the fully connected neurons
        # form the diagonal activation derivative matrices
        delta = (layers_list[num_layers-1]-ytrain[n])
        delta = delta.reshape(1,ytrain.shape[1])
        diag_activs = list()
        for j in range(0,num_layers-1):
            activ_der = activ_deriv(layers_list[j],1)
            diag_mat = np.diag(activ_der.ravel())
            diag_activs.append(diag_mat)

        activ_der = activ_deriv(layers_list[num_layers-1],2)
        diag_mat = np.diag(activ_der.ravel())
        diag_activs.append(diag_mat)

        if (dropout==1):
            for m in range(1,mask_rows+1):
                diag_activs[m] = \
                        np.diag(dropout_mask[m-1])*diag_activs[m]

        # form the products of the weights and diagonals
        mat_prods = list()
        mat_prods.append(np.matmul(delta,diag_activs[num_layers-1]))
        for j in range(num_layers-2):
            mat1 = weights_list[num_layers-2-j].T
            mat2 = diag_activs[num_layers-2-j]
            new_mat = np.matmul(mat1,mat2)
            tot_mat = np.matmul(mat_prods[j],new_mat)
            mat_prods.append(tot_mat)

        for j in range(len(weights_list)):
            weight_corrects_list[j] = \
                -alpha*np.outer(layers_list[num_layers-2-j], \
                                mat_prods[j])
            weights_list[num_layers-2-j] += weight_corrects_list[j]

        # backprop step for the kernel corrections
        grad_kernel_indices = \
            np.indices((grad_kernel.shape[0],grad_kernel.shape[1]))
        for k in range(num_kernels):
            mask = (which_kernel==k).astype('int64')
            image_frames_masked = image_frames*mask
            mat_prod = np.matmul(weights_list[0].T,diag_activs[0])
            for l in range(1,len(diag_activs)-1):
                new_prod = np.matmul(weights_list[l].T,diag_activs[l])
                mat_prod = np.matmul(new_prod,mat_prod)
            mat_prod = np.matmul(mat_prod,image_frames_masked.T)
            grad_kernel[k] = np.matmul(delta,mat_prod)
        kernels -= alpha*grad_kernel

        err += np.sum(delta**2.0)
    err /= Xtrain.shape[0]
    print(iter,err)
    iter += 1

if (iter<max_iter):
    print("converged at iteration: ",iter-1)
    print("average error: ",err)
else:
    print("failed to converge")

err = 0.0
num_correct = 0
for n in range(Xtest.shape[0]):
    # forward propagation convolution + pooling steps
    image = Xtest[n].reshape(image_rows,image_cols)
    image_frames = capture_frames(image, \
                                  frame_rows,frame_cols)

    # form layer_0 pre-pooling step
    layer_0_pre = np.zeros((num_kernels,image_frames.shape[1]))
    for k in range(num_kernels):
        layer_0_pre[k,:]= \
            np.matmul(kernels[k].reshape(1,len(kernels[k])), \
                      image_frames)
    which_kernel = np.argmax(layer_0_pre,axis=0)

    # pooling step
    layer_0 = \
        np.max(layer_0_pre,axis=0).reshape(1,layer_0_pre.shape[1])

    # forward propagation to the other layers
    layers_list[0] = layer_0
    for j in range(1,num_layers-1):
        layers_list[j] = \
                activ_func(np.matmul(layers_list[j-1], \
                           weights_list[j-1]),1)
    layers_list[num_layers-1] = \
        activ_func(np.matmul(layers_list[num_layers-2], \
                   weights_list[num_layers-2]),2)

    delta = layers_list[num_layers-1].ravel()-ytest[n]
    err += np.sum(delta**2.0)

    num_pred1 = \
            layers_list[num_layers-1][0,0: \
                                      num_soft_max].argmax()
    num_pred2 = \
            layers_list[num_layers-1][0,num_soft_max: \
                                      2*num_soft_max].argmax()
    num_pred3 = \
            layers_list[num_layers-1][0,2*num_soft_max: \
                                        3*num_soft_max].argmax()

    num_test1 = ytest[n][0:num_soft_max].argmax()
    num_test2 = ytest[n][num_soft_max:2*num_soft_max].argmax()
    num_test3 = ytest[n][2*num_soft_max:3*num_soft_max].argmax()

    if ((num_pred1==num_test1)&(num_pred2==num_test2)& \
        (num_pred3==num_test3)):
        num_correct += 1.0
err /= Xtest.shape[0]
print("average test set error:",err)
percent_correct = (num_correct/Xtest.shape[0])*100.0
print("percent correct out of sample: ",percent_correct)

# save the kernels in csv format
import pandas as pd
kernels = pd.DataFrame(kernels)
kernels.to_csv('kernels.csv',index=False)
