# use naive_bayes to analyze synthetic widget data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay

widget_data = pd.read_csv("widget_data.csv")

def gen_test_train(data_frame,label_col,fraction_test):
    num_rows = data_frame.shape[0]
    rand_indices = np.linspace(0,num_rows-1,num_rows).astype('int')
    np.random.shuffle(rand_indices)

    shuffled_data = data_frame.iloc[rand_indices]
    cut_index = int(num_rows*(1.0-fraction_test))
    Xfull = shuffled_data.drop(label_col,axis=1)
    yfull = shuffled_data[label_col]

    Xtrain = Xfull.iloc[0:cut_index]
    Xtest  = Xfull.iloc[cut_index+1:num_rows]
    ytrain = yfull.iloc[0:cut_index]
    ytest  = yfull.iloc[cut_index+1:num_rows]

    return Xtrain, ytrain, Xtest, ytest

fraction_test = 0.1
Xtrain, ytrain, Xtest, ytest = \
    gen_test_train(widget_data,"durability",fraction_test)

def prob_E_given_H(data_frame,E_col,condition_on,E_val,H_val):
    # we assume that the hypothesis is y = 1 (H_val = 1)
    # or y = 0 (for H_val = 0); also we assume that the feature
    # data is either 0 or 1
    data_slice = data_frame[condition_on==H_val]
    
    return (data_slice[E_col]==E_val).sum()/data_slice.shape[0]

def fit_naive_bayes(X,y):
    cols = X.columns
    probs = np.zeros((4,len(cols)+1))
    # the last column will hold P(H) and P(~H), while the others
    # will hold P(e_i|H) (1st row) and P(e_i|~H) (2nd row)

    prob_cols = list(cols)
    prob_cols.append('base')
    probs = pd.DataFrame(probs,columns=prob_cols)
    for col in cols:
        probs.loc[0,col] = prob_E_given_H(X,col,y,1,1)
        probs.loc[1,col] = prob_E_given_H(X,col,y,1,0)
        probs.loc[2,col] = prob_E_given_H(X,col,y,0,1)
        probs.loc[3,col] = prob_E_given_H(X,col,y,0,0)
        probs.loc[0,'base'] = (y==1).sum()/len(y)
        probs.loc[1,'base'] = (y==0).sum()/len(y)
        probs.loc[2,'base'] = (y==1).sum()/len(y)
        probs.loc[3,'base'] = (y==0).sum()/len(y)
    return probs

def pred_naive_bayes(X,model_probs):
    prob_array = np.zeros((2,X.shape[1]))
    y = np.zeros(X.shape[0])
    base_H = model_probs.iloc[0,model_probs.shape[0]-1]
    base_notH = model_probs.iloc[1,model_probs.shape[0]-1]
    for i,row in enumerate(X.to_numpy()):
        for j,E_value in enumerate(row):
            if E_value==1:
                prob_array[0,j] = model_probs.iloc[0,j]
                prob_array[1,j] = model_probs.iloc[1,j]
            else:
                prob_array[0,j] = model_probs.iloc[2,j]
                prob_array[1,j] = model_probs.iloc[3,j]
        term1 = \
            prob_array[0].prod()*base_H
        term2 = \
            prob_array[1].prod()*base_notH
        if (term1+term2)!=0.0:
            y[i] = term1/(term1+term2)
        else:
            y[i] = 0.0
    return y

model_probs = fit_naive_bayes(Xtrain,ytrain)
pred = pred_naive_bayes(Xtest,model_probs)

pred_pd = pd.DataFrame(pred)
pred_pd.to_csv("bayes_pred.csv",index=None)
ytest_pd = pd.DataFrame(ytest)
ytest_pd.to_csv("bayes_ytest.csv",index=None)

pred_class = pred.round().astype('int')
accuracy = (pred_class==ytest).sum()/len(ytest)
base_acc = (ytest==1).sum()/len(ytest)
print('base rate predictor accuracy: ',base_acc)
print('naive bayes predictor accuracy:',accuracy)
confusion_mat = confusion_matrix(pred_class,ytest)
disp = ConfusionMatrixDisplay(confusion_mat)
disp.plot()
plt.grid(False)
plt.show()
