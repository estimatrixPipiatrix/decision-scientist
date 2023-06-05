# use recursion to accept a string and return the first index
# where the string as the character x. assume there is at least
# one x in the string

string = 'qwerpoiughjlzxcvadsfj;zzcxz'
# the answer should be 13

def first_x(string,index=0):
    if string[0]=='x':
        return index
    else:
        index += 1
        return first_x(string[1:len(string)],index)

print(first_x(string))
