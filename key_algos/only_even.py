# write a recursive function that takes an array of numbers and
# outputs an array containing only the even numbers

vec = [4,6,7,2,0,6,3,10,13]

def return_even(vec,lst=[]):
    print('called!')
    if vec[0]%2==0:
        lst.append(vec[0])
    if len(vec)>1:
        lst.extend(return_even(vec[1:len(vec)],[]))
    return lst

ans = return_even(vec)
print(ans)
