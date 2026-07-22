# calculate numbers of letters in a string

text = input("enter the string : ")

result = 0

for i in text:
    if i != " ": 
        result = result+1
print(result)