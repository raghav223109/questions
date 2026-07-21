# 2nd largest element in the list 

num = [1,2,4,7,9,10,78]

largest = num[0]
second_largest = num[0]

for i in num:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print("largest number is",largest)
print("second largest number is",second_largest)
print("program ended here")