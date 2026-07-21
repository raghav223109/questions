# pyramin pattern 

n = 5

for i in range (1,n+1):
    #spaces
    print(" " * (n-i+1), end="")

    #stars
    print(" * " * (2 * i - 1 ))