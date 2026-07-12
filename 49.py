from collections import Counter

s = input("enter your string :")


def count(s):
    return dict(Counter(s))


print(count(s)) 
