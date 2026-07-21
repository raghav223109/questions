# remove particular character from the string 

text = input("enter your string:")

char = input("enter the character to remove:")

result = ""

for i in text:
    if i != char:
        result = result + i

print(result)
print("program ended here")