# use a recursive function to return all the numbers in an array
# that contains arrays that contain arrays etc.

vec = [2,3,0,
       [4,0,-1,2,[4,6,2,10]],
       9,8,2,
       [3,4,1,-2,-3,[6,5,-4,[10,20,-30,[1,8,7,3]]]]]

def print_nums(vec):
    for n in vec:
        if type(n)==int:
            print(n)
        else:
            print_nums(n)

print_nums(vec)
