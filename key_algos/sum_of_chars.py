# use recursion to return the sum of characters across all strings
# in an array

chars = ['ab','gfd','','bvds','hg']
# the answer should be 11

def sum_chars(chars):
    if len(chars)>1:
        return len(chars[0]) + sum_chars(chars[1:len(chars)])
    else:
        return len(chars[0])

print(sum_chars(chars))
