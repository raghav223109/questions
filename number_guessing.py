import random

number = random.randint(1,100)
print(number)


guess = 0
while guess != number:
    guess = int(input("enter the guess: "))
    if guess < number:
        print("too low")
    elif guess > number:
        print("too high")
    else:
        print("correct")
        break
print("program ended here")    