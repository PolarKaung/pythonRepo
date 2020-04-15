import numpy as np
import function as f
print("Matrix inversion")

#user defined matrix
a = int(input("Enter number of rows of the first matrix:"))
b = int(input("Entre number of columns of the second matrix:"))
print("Please enter the entries rowwise:")
M = np.zeros((a,b),dtype = int)
for i in range(a):
    for j in range(b):
        M[i,j]=(int(input()))
print("Matrix1=",M)
print("order of matrix=",M.shape)

c = int(input("Enter number of rows of the matrix:"))
d = int(input("Entre number of columns of the matrix:"))
print("Please enter the entries rowwise:")
N = np.zeros((c,d),dtype = int)
for i in range(c):
    for j in range(d):
        N[i,j]=(int(input()))
print("Matrix=",N)
print("order of matrix=",N.shape)

#addition
ans = f.add(M,N)
print("The result of addition of two matrix:  ",ans)
