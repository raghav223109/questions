# lambda to find the square of the number

n = int(input("enter the number: "))

square = lambda x: x * x

print("square of", n, "is", square(n))

print("program ended here")