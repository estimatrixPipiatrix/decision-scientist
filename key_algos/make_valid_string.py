#given a string with lowercase letters and left and right parentheses,
#remove the minimum number of parentheses so the string is valid
# for example, if the string is ")a(b((cd)e(f)g)" return
# "ab((cd)e(f)g)"

string = ")a(b((cd)e(f)g)"
string = "())((())()())()"

def correct_string(string):
    paren = {'(':[]}
    new_string1 = ''
    for i,curr in enumerate(string):
        flag = 0
        if curr=='(':
            curr_locs = paren['('].copy()
            curr_locs.append(i)
            paren.update({'(':curr_locs})
        if curr==')':
            curr_locs = paren['('].copy()
            if len(curr_locs)>0:
                curr_locs.pop()
                paren.update({'(':curr_locs})
            else:
                flag = 1
        if flag==0:
            new_string1 += curr
        else:
            new_string1 += ' '
    new_string2 = ''
    locs = set(paren['('])
    for i,curr in enumerate(new_string1):
        if i not in locs and curr!=' ':
            new_string2 += curr
    return new_string2

print(correct_string(string))
