#convert 2d list into 1d list

list2d = [[1,2,3],[4,5,6],[7,8,9]]

list1d = []

for i in list2d:
    for j in i:
        list1d.append(j)

print(list1d)
