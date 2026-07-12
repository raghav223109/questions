from collections import Counter

s = [12,23,34,45,57,12,12,12,34,34,56,57,57,57,89,89]

def count(s):
    return dict(Counter(s))


print(count(s) )