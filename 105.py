# all unique combination of 1,2,3,4

num = [1,2,3,4]

for i in num:
    for j in num:
        if i != j:
            print(i,j)