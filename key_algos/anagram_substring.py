# given two strings A and B, write a function to return a list of 
# all start indices within A where the substring of A is an 
# anagram of B. for example, if A = "abcdcbac" and B = "abc" then
# you want to return [0,4,5] since those are the starting indices
# of substrings of A that are anagrams of B

A = 'abcdcbac'
B = 'abc'

B_hash = {}
for n in B:
    B_hash.update({n:True})

indices = []
for i,m in enumerate(A):
   if i<=(len(A)-len(B)):
       curr_window = A[i:i+len(B)]
       A_count = {}
       for n in curr_window:
           if B_hash.get(n)==True:
               if A_count.get(n)==None:
                   A_count.update({n:1})
               else:
                   A_count.update({n:A_count[n]+1})
           else:
               A_count = {}
       if len(A_count)==3:
           indices.append(i)

print(indices)
