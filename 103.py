#extracting name from the mailID

email = input("enter your mail ID:")

userName = ""

for i in email:
    if i == '@':
        break
    userName = userName + i

print(userName)
print("program ended here")