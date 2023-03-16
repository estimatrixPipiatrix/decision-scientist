import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# load X_conv and y_conv
Xconv_load   = np.load('X_conv.npz',allow_pickle=True)
yconv_load   = np.load('y_conv.npz',allow_pickle=True)

Xconv = Xconv_load['arr_0'].astype('float64')
yconv = yconv_load['arr_0'].astype('float64')

# set up the training and test samples
percent_train = 0.9
num_train = int(np.round(Xconv.shape[0]*0.8))
num_test  = Xconv.shape[0]-num_train
Xtrain    = Xconv[0:num_train]
ytrain    = yconv[0:num_train]

def show_kernels(num_kernels,frame_rows,frame_cols):
    kernels = pd.read_csv('kernels.csv').to_numpy()
    kernels = kernels.reshape(num_kernels,frame_rows,frame_cols)

    num_plot_rows = round(num_kernels/3.0)+1
    num_plot_cols = 3
    fig, axes = plt.subplots(num_plot_rows,num_plot_cols)
    for i, ax in enumerate(axes.flat):
        if (i<num_kernels):
            ax.imshow(kernels[i],interpolation='gaussian')
            ax.grid(None)
    plt.show()

kernels = pd.read_csv('kernels.csv').to_numpy()
num_kernels = kernels.shape[0]

frame_rows = 2
frame_cols = 2
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


to_plot = np.array([92,90,7993,85])

plot_list  = list()
title_list = list()
for k in range(len(to_plot)):
    current = to_plot[k]
    image = Xtrain[current]
    #print("ytrain: ",ytrain[current].round())
    image_frames = capture_frames(image,frame_rows,frame_cols)
    
    layer_0_pre = np.zeros((num_kernels,image_frames.shape[1]))
    for k in range(num_kernels):
        layer_0_pre[k,:]= \
            np.matmul(kernels[k].reshape(1,len(kernels[k])), \
                      image_frames)

    image_rows = image.shape[0]
    image_cols = image.shape[1]
    filtered_rows = image_rows-frame_rows+1
    filtered_cols = image_cols-frame_cols+1
    filtered_img = layer_0_pre.reshape(num_kernels,filtered_rows, \
                                                   filtered_cols)
    plot_list.append(filtered_img)
    name = str(ytrain[current][0:2].round().argmax()) + str(" + ") + \
           str(ytrain[current][2:4].round().argmax()) + str(" = ") + \
           str(ytrain[current][4:6].round().argmax())
    title_list.append(name)

num_plot_rows = 4
num_plot_cols = 3 
fig, axes = plt.subplots(num_plot_rows,num_plot_cols)
for i, ax in enumerate(axes.flat):
    current_row = int(i/num_plot_cols)
    current_col = i%num_plot_cols
    current_image = plot_list[current_row]
    ax.imshow(current_image[current_col],interpolation='gaussian')
    ax.xaxis.set_tick_params(labelbottom=False)
    ax.yaxis.set_tick_params(labelleft=False)
    if (current_col==0):
       ax.set_ylabel(title_list[current_row])
    ax.grid(None)
plt.show()
