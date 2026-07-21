# armstrong number in a given range 
a = int(input())
b = int(input())

for num in range (a ,b+1):
    num_str = str(num)
    n = len(num_str)
    result = 0

    for digit_char in num_str:
        digit = int(digit_char)
        result = result + digit**n

    if result == num:
        print(num)