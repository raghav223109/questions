# sum and average until user enter 0

total = 0
count = 0

while True:
    num = int(input("enter the number:"))

    if num == 0:
        break
    
    total += num
    count += 1


if count > 0:
    average = total / count
    print("average is: ",average)
    print("total is: " , total)
else:
    print("no number was entered")