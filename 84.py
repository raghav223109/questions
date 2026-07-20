# write a program to reverse a four digit number 

num = (input("enter the number to be reversed :"))

if len(num)== 4 and num.isdigit():
    reversed = (num[::-1])
    print(reversed)
else:
    print("enter the valid number {num}")

if reversed == (num[::-1]):
    print("the number is reversed as {reversed}")


print("program ended here")