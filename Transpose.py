import numpy as np

row,col = int(input("Enter number of roll:")),int(input("Enter number of column:"))
A = np.zeros((row,col))

T= np.zeros((col,row))

for i in range(len(A)):
    for j in range(len(A[i])):
        y = int(input("Enter values of matrix \n"))
        A[i,j] = y
        T[j,i] = A[i,j]
print("The matrix is\n", A)
print("The result is\n", T)
