# matrix multiplication of 2 matrices 

mat1 = [
    [1,2],
    [3,4]
]

mat2 = [
    [5,6],
    [7,8]
]

for i in range(len(mat1)):
    for j in range(len(mat1)):
        for k in range(len(mat1)):
            print(mat1[i][k] * mat2[k][j], end=" ")
        print()
