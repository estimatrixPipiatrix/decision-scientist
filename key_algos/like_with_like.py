# given a string return a list that groups the same letters together

string = "how are you doing today"

def group_like_letters(string):
    counts = {}
    for n in string:
        if n!=" ":
            if counts.get(n)==None:
                counts.update({n:1})
            else:
                counts.update({n:counts[n]+1})

    groups = []
    keys = list(counts.keys())
    for key in keys:
        num_repeat = counts[key]
        for i in range(num_repeat):
            groups.append(key)

    return groups
