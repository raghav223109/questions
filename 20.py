myList = [1,3,3,1,1,4,4,4,4,6,6,7,8,9,1,2]
new_list = []
new_list2 = []
for num in myList:
    if myList.count(num)==1:
        new_list.append(num)
print(myList.count(1))
print(new_list)

for num in myList:
    if myList.count(num)>1 and num not in new_list2:
        new_list2.append(num)
print(new_list2)
