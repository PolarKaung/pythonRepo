import numpy as np
import function as f

print("Transpose of Matrix")

# user defined matrix
a = int(input("Enter number of rows of the matrix:"))
b = int(input("Entre number of columns of the matrix:"))
print("Please enter the entries rowwise:")
M = np.zeros((a,b),dtype = int)
for i in range(a):
    for j in range(b):
        M[i,j]=(int(input()))
print("Matrix=",M)
print("order of the matrix=",M.shape)

# transpose calculation
trs = f.transpose(M)
print("Transpose of the matrix",trs)
print("order of the transposed matrix=",trs.shape)
