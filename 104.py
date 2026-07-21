# index position of a particular character 
print("="*30)
text = input("enter a string:")
print("="*30)


print("="*30)
char = input("enter a character:")
print("="*30)


for i in range(len(text)):
    if text[i] == char:
        print("="*30)
        print("index position of", char, "is", i)
        print("="*30)
        break
else:
    print("="*30)
    print("character not found")
    print("="*30)


