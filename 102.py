# largest element in the list

num = [1,4,7,29]

largest = num[0]

for i in num:
    if i > largest:
        largest = i

print(largest)

# output: 29