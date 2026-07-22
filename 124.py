# find max item in each row 

list2d = [[1,2,3],[4,5,6],[7,8,9]]

for row in list2d:
    current_max = row[0]
    for item in row:
        if item > current_max:
            current_max = item
    print(current_max)