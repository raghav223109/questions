# index of a particular char

text = input("enter a string:")

char = input("enter the character:")

for i in range(len(text)):
    if text[i] == char:
        print(i)