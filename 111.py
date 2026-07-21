# find the given number form the list 
List = [1,2,3,4,5,6,7,8,9]

number = int(input("enter the number: "))

for i in List:
    if i == number:
        print("number found")
        break
    else:
        print("number not found")
        break