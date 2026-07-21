# prog to print first 25 add numbers 

odd_count = 0

for i in range(1,51):
    if i % 2 != 0:
        print(i)
        odd_count += 1

        if odd_count == 25:
            break