# use recursion so solve this problem: given a number of rows and
# a number of columns, return the number of ways there are to get
# from the upper left corner of the matrix to the lower right 
# corner, given that we are only allowed to move either rightward
# or downward

rows = 3
cols = 3

def num_paths(rows,cols,memo={}):
    if (rows==1 or cols==1):
        return 1
    else:
        key = str(rows-1)+str(cols)
        if memo.get(key) != None:
            term1 = memo[key]
        else:
            term1 = num_paths(rows-1,cols)
            memo.update({key:term1})
        term2 = num_paths(rows,cols-1,memo)
        return term1 + term2

print(num_paths(rows,cols))
