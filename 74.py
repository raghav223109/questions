# filter function
numbers = [1,3,45,2,4,3,3,44,55,3322, 44 , 66,66,66]

even = list(filter(lambda x: x%2 == 0, numbers))
print("even numbers are", even)