# calculate the sum of the elements of matrix inside the 
# rectangle defined by its upper left corner (row1, col1) 
# and lower right corner (row2, col2). the implementation must
# have O(1) time complexity
import numpy as np

class num_matrix:
    # assume matrix is a numpy matrix
    def __init__(self,matrix):
        self.matrix = matrix
        prefix = np.zeros((matrix.shape[0]+1,matrix.shape[1]+1))
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                total = 0
                for k in range(i+1):
                    for l in range(j+1):
                        total += matrix[k,l]
                prefix[i+1,j+1] = total
        self.prefix = prefix

    def region_sum(self,row1,col1,row2,col2):
        term1 = self.prefix[row2+1,col2+1]
        term2 = self.prefix[row2+1,col1]
        term3 = self.prefix[row1,col2+1]
        term4 = self.prefix[row1,col1]
        return term1-term2-term3+term4

    def region_sum_brute(self,row1,col1,row2,col2):
        total = 0
        for i in range(row1,row2+1):
            for j in range(col1,col2+1):
                if i<matrix.shape[0] and j<matrix.shape[1]:
                    total += self.matrix[i,j]
        return total

for i in range(1000):
    num_rows = np.random.randint(1,10)
    num_cols = np.random.randint(1,10)
    matrix = np.random.randint(0,10,size=(num_rows,num_cols))
    nm = num_matrix(matrix)
    row1 = np.random.randint(nm.matrix.shape[0])
    col1 = np.random.randint(nm.matrix.shape[1])
    row2 = row1 + np.random.randint(nm.matrix.shape[0]-row1)
    col2 = col1 + np.random.randint(nm.matrix.shape[1]-col1)
    method_1 = nm.region_sum(row1,col1,row2,col2)
    method_2 = nm.region_sum_brute(row1,col1,row2,col2)
    if method_1!=method_2:
        print(row1,col1,row2,col2)
        print(nm.matrix) 
        print(method_1,method_2)
