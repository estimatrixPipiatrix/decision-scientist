# you are given a string s and an integer k. You can choose any 
# character of the string and change it to any other uppercase 
# english character. You can perform this operation at most k times
# return the length of the longest substring containing the same 
# letter you can get after performing the above operations
# example input: s = "ABAB", k = 2
# output: 4
# explanation: replace the two 'A's with two 'B's or vice versa
# another example input: s = "AABABBA", k = 1
# output: 4

#string = "AGFEGDFABBBAAA"
#k = 3
#string = "ABAB"
#k = 2
string = "AABABBA"
k = 1

def longest_with_replace(string,k):
    left = 0
    right = 0
    count = 0
    max_string = 0
    num_changes = 0
    prev = string[left]
    while right<len(string):
        curr = string[right]
        if curr!=prev:
            num_changes += 1
            if num_changes<=k:
                count += 1
            else:
                count = 1
                left += 1
                prev = string[left]
                right = left
                num_changes = 0
        else:
            count += 1
        #print(left,right,count)
        if count>max_string:
            max_string = count
        right += 1
    return max_string

print(longest_with_replace(string,k))
