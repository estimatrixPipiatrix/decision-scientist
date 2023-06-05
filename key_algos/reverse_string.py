# use a stack to reverse a string
from class_stack import stack

sent = 'this is the string i would like to reverse'

s = stack()
for n in sent:
    s.push(n)

reversed = ''
while s.below != None:
    reversed += s.below.data_val
    s.pop()
