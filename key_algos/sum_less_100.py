# use recursion to sum the numbers of an array without including 
# any numbers that would be bring the sum over 100

vec = [2,6,10,55,2,6,16,32,6,230,5,1,1]

def sum_less_100(vec):
    if len(vec)==0:
        return 0
    else:
        v_last = vec[len(vec)-1]
        sum_part = sum_less_100(vec[0:len(vec)-1])
        if (sum_part+v_last)<=100:
            return sum_part+v_last
        else:
            return sum_part

print(sum_less_100(vec))
