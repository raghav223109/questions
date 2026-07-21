# check if the list is in ascending order or not 

numbers = [12,45,78,1,90,11,24,70,1]

is_asec = True

for i in range(len(numbers)-1):
    if numbers[i] > numbers[i+1]:
        is_asec = False
        break

if is_asec:
    print("ascending")
else:
    print("not ascending")