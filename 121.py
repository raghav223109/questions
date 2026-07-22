# replace a item with a new item in a list 

list = ["a","b","c","d","e","f"]

item1= input("enter the item to be replaced:")
item2 = input("enter the new item:")

for i in range(len(list)):
    if list[i] == item1:
        list[i] = item2

print(list)