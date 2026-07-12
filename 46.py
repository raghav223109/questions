list_1 = [1 , 34 , 5 , 67 ,9]
list_2 = [34 , 9 , 45 , 78 , 7]

def common_ele(list_1 , list_2):
    return list(set(list_1) & set(list_2))

print(common_ele(list_1 , list_2))