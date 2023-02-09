import numpy as np

inputs = np.array([[1,0,1],
                   [0,1,1],
                   [0,0,1],
                   [1,1,1]])

outputs = np.array([1,1,0,0])

hidden_layer = 4
weights_0_1 = 2.0*np.random.random((hidden_layer,3))-1.0
weights_1_2 = 2.0*np.random.random((1,hidden_layer))-1.0

def relu(x):
    return (x>0)*x

def relu_deriv(x):
    return x>0

def activate_mid(weights,layer):
    return relu(np.matmul(weights,layer))

def activate(weights,layer):
    return np.matmul(weights,layer)

def error(inp,weights_0_1,weights_1_2,out):
    layer_1 = activate_mid(weights_0_1,inp)
    layer_2 = activate(weights_1_2,layer_1)
    return np.sum((layer_2-out)**2.0)

def error_derivs(layer_num,inp,out,weights_0_1,weights_1_2):
    delta_w = 0.0001
    layer_1 = activate_mid(weights_0_1,inp)
    layer_2 = activate(weights_1_2,layer_1)
    if (layer_num==1):
        derivs_1 = np.zeros((hidden_layer,3))
        weights_0_1_left  = weights_0_1
        weights_0_1_right = weights_0_1
        for i in range(weights_0_1.shape[0]):
            for j in range(weights_0_1.shape[1]):
                weights_0_1_left[i,j]=weights_0_1[i,j]-delta_w
                err_0 = error(inp,weights_0_1_left, \
                              weights_1_2,out)
                weights_0_1_left[i,j]=weights_0_1[i,j]+delta_w
                weights_0_1_right[i,j]=weights_0_1[i,j]+delta_w
                err_1 = error(inp,weights_0_1_right, \
                              weights_1_2,out)
                weights_0_1_right[i,j]=weights_0_1[i,j]-delta_w
                derivs_1[i,j] = (err_1-err_0)/(2.0*delta_w)

                #print('num:',derivs_1[i,j])
                derivs_1[i,j] = 2.0*(layer_2-out)* \
                                relu_deriv(layer_1[i])* \
                                weights_1_2[0,i]*inp[j]
                #print('ana:',derivs_1[i,j])
        prefactor = 2.0*(layer_2-out)
        #print("before: ",derivs_1)
        derivs_1  = prefactor*np.outer(relu_deriv(layer_1)* \
                                       weights_1_2.T,inp)
        #print("after: ",derivs_1)
        return derivs_1
    elif (layer_num==2):
        derivs_2 = np.zeros((1,hidden_layer))
        weights_1_2_left  = weights_1_2
        weights_1_2_right = weights_1_2
        for i in range(weights_1_2.shape[0]):
            for j in range(weights_1_2.shape[1]):
                weights_1_2_left[i,j]=weights_1_2[i,j]-delta_w
                err_0 = error(inp,weights_0_1, \
                              weights_1_2_left,out)
                weights_1_2_left[i,j]=weights_1_2[i,j]+delta_w
                weights_1_2_right[i,j]=weights_1_2[i,j]+delta_w
                err_1 = error(inp,weights_0_1, \
                              weights_1_2_right,out)
                weights_1_2_right[i,j]=weights_1_2[i,j]-delta_w
                derivs_2[i,j] = (err_1-err_0)/(2.0*delta_w)

                #print('num:',derivs_2[i,j])
                derivs_2[i,j] = 2.0*(layer_2-out)*layer_1[j]
                #print('ana:',derivs_2[i,j])
        derivs_2 = 2.0*(layer_2-out)*layer_1.T
        return derivs_2

alpha = 0.1
for iter in range(60):
    err = 0.0
    for i in range(inputs.shape[0]):
        inp = inputs[i:i+1].T
        out = outputs[i]
       
        derivs_1 = error_derivs(1,inp,out,weights_0_1, \
                                weights_1_2)
        derivs_2 = error_derivs(2,inp,out,weights_0_1, \
                                weights_1_2)

        weights_0_1 -= alpha*derivs_1
        weights_1_2 -= alpha*derivs_2
        err += error(inp,weights_0_1,weights_1_2,out)

        layer_1 = relu(np.matmul(weights_0_1,inp))
        layer_2 = np.matmul(weights_1_2,layer_1)
        #print(layer_2,out)

    err /= inputs.shape[0]
    print(err)
