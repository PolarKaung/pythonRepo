import numpy as np
import function as f
print("Matrix inversion")
a = int(input("Enter number of rows of the matrix:"))
print(a)
b = int(input("Entre number of columns of the matrix:"))
print(b)
print("Please enter the entries rowwise:")
M = np.zeros((a,b),dtype = int)
for i in range(a):
    for j in range(b):
        M[i,j]=(int(input()))
print("Matrix=",M)

if M.shape == (3,3):
     M_inv = f.M33inverse(M)
     print("Inverse of the Matrix = ",M_inv)
     print("Checking")
     Checkanswer = f.inverse_checking(M,M_inv)
     print("Matrix * Inverse of that Matrix :",Checkanswer)
else:
    print("This program is written only for (3*3) matrix. So, please change your matrix to be (3*3) matrix.")

   
