# check to see whether two input strings are anagrams of one another

str1 = "cheater"
str2 = "teacher"

def are_anagrams(str1,str2):
    hash1 = {}
    for n in str1:
        if hash1.get(n)==True:
            hash1.update({n:hash1[n]+1})
        else:
            hash1.update({n:1})

    hash2 = {}
    for n in str2:
        if hash2.get(n)==True:
            hash2.update({n:hash2[n]+1})
        else:
            hash2.update({n:1})

    return hash1==hash2
