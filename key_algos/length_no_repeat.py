# given a string s, find the length of the longest substring 
# without repeating characters
# Input: s = "abcabcbb"
# Output: 3
# explanation: The answer is "abc", with the length of 3

string = "abcabcbb"
#string = "abcabcdeefg"

def len_no_repeat(string):
    left = 0
    right = 0
    seen = {}
    count = 0
    max_count = 0
    while right<len(string):
        curr = string[right]
        if seen.get(curr)==None:
            seen.update({curr:right})
            count += 1
        else:
            seen_at = seen[curr]
            if seen_at>=left:
                count -= seen_at-left
                left = seen_at+1
        #print(left,right,count)
        if count>max_count:
            max_count = count
        right += 1
    return max_count

print(len_no_repeat(string))
