list = ["hello" , 10 , 10 , 20, 30 , 40]
d = []

for el in list:
    if list.count(el) > 1 and el not in d:
        d.append(el)
print(d)