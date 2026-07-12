myList = [12,34,456,578]
largest = myList[0]

for numbers in myList[1:]:
    if numbers > largest:
        largest = numbers
print(largest)