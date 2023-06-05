# given a statement with parentheses, determine whether each
# type is matched
from class_stack import stack

statement = '{blahblah [more blah( and more) but yes] done} haha'

paren = {'(':'open','[':'open','{':'open', \
         ')':'close',']':'close','}':'close'}
pair = {')':'(',']':'[','}':'{'}

s = stack()
error_flag = 0
for n in statement:
    if paren.get(n)=='open':
        s.push(n)
    elif paren.get(n)=='close':
        popped = s.below.data_val
        s.pop()
        if (popped != pair[n] or popped == None):
            error_flag = 1

if s.below != None:
    error_flag = 1

if error_flag==1:
    print('unmatched parenthesis')
else:
    print('parentheses match')
