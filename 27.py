word = input("enter the string to be reserved:")
string = word.split()
empty = []

for el in string:
    empty.append(el[::-1])
print(empty)
print(" ".join(empty))