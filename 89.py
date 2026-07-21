# prime number or not 

n = int(input("enter the number: "))

i = 2
flag = 0

if n < 2:
    print("no")
else:
    while n > i:
        if n % i ==0:
            flag = 1
            break
        i += 1

    if flag == 1:
        print("not prime")
    else:
        print("prime")