# palindrome with out string slicing 

num = int(input())
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("yes")
else:
    print("no")