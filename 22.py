numbers = [23,454,67,89,12,34,99,54,999]
max = numbers[0]
min = numbers[0]

for ele in numbers:
    if ele > max:
        max = ele
    if ele < min:
        min = ele

print(max)
print(min)