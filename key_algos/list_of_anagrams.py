# given an array of strings, return a list of lists where each list
# contains the strings that are anagrams of one another. for example,
# if the input is ["abc","abd","cab","bad","bca","acd"] then return
# [["abc","cab","bca"],["abd","bad"],["acd"]]

strings = ["abc","abd","cab","bad","bca","acd"]

def string_to_freq(string):
    freq = {}
    for letter in string:
        if freq.get(letter)==None:
            freq.update({letter:1})
        else:
            freq[letter] += 1

    key_list = freq.keys()
    key_list = list(key_list)
    key_list.sort()
    freq_sorted = {i:freq[i] for i in key_list}
    return freq_sorted

def group_anagrams(strings):
    anagrams = {}
    for string in strings:
        letter_freq = str(string_to_freq(string))
        if anagrams.get(letter_freq) == None:
            anagrams.update({letter_freq:[string]})
        else:
            string_list = anagrams[letter_freq]
            string_list.append(string)
            anagrams.update({letter_freq:string_list})
       
    keys = anagrams.keys()
    string_groups = [anagrams[i] for i in keys]
    return string_groups

print(group_anagrams(strings))
