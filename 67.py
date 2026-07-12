text = "hello how are you"

char = input("enter character")

for i in range(len(text)):
    if text[i] == char:
        print("character is present at index" , i)
        break
else:
    print("character is not present at index")  