def golomb(n,memo={}):
    if n==1:
        return 1
    if memo.get(n) != None:
        return memo[n]
    else:
        if memo.get(n-1) != None:
            inner1 = memo[n-1]
        else:
            inner1 = golomb(n-1,memo)
            memo.update({n-1:inner1})
        if memo.get(inner1) != None:
            inner2 = memo[inner1]
        else:
            inner2 = golomb(inner1,memo)
            memo.update({inner1:inner2})
        if memo.get(n-inner2) != None:
            outer = memo[n-inner2]
        else:
            outer = golomb(n-inner2,memo)
        return 1 + outer

for i in range(1,21):
    print(i,golomb(i))
