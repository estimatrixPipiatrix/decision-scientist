# check if the input is a palindrome

vec = 'amanaplanacanalpanama'
L = 0
R = len(vec)-1
continue_flag = 1

while (L<R and continue_flag==1):
    if vec[L]==vec[R]:
        L += 1
        R -= 1
    else:
        continue_flag = 0

if (continue_flag==1):
    print('true')
else:
    print('false')
