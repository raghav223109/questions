# count and print all vowels 

text = input("enter the string:")

vowels = ('a','e','i','o','u')

count = 0
result = ""

for i in text:
    if i in vowels:
        count += 1
        result += i

print(count,result)