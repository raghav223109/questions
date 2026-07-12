fruits = ['apple' , 'orange' , 'banana' , ]
fruits.append('kela')
fruits.remove('orange')
fruits[1] = 'kiwi'
print(fruits)

others = [1,2,3,4]
fruits.extend(others)
print(fruits)
fruits.pop(2)
print(fruits)
fruits.pop()
print(fruits)