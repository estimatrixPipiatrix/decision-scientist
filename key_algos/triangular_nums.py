# triangular numbers start off as 1,3,6,10,15,21 and afterward
# the Nth number in the series is N + the previous number
# use recursion to generate the Nth triangular number

N=9

def triangular(N):
    if (N<7 and N>0):
        early_nums = {1:1,2:3,3:6,4:10,5:15,6:21}
        return early_nums[N]
    if N==0:
        return 0
    return N+triangular(N-1)

print(triangular(N))
