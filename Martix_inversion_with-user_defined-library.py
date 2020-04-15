import numpy as np
import function as f

print("Matrix inversion")

# user defined matirx
a = int(input("Enter number of rows of the matrix:"))
b = int(input("Entre number of columns of the matrix:"))
print("Please enter the entries rowwise:")
M = np.zeros((a,b),dtype = int)
for i in range(a):
    for j in range(b):
        M[i,j]=(int(input()))
print("Matrix=",M)
print("order of matrix=",M.shape)

#inverse calculation
if M.shape == (2,2):
    M_inv = f.M22inverse(M)
    print("Inverse of the Matrix =",M_inv)
    try:
        print("Checking")
        Checkanswer = f.inverse_checking(M,M_inv)
        print(Checkanswer)
    except TypeError:
        print("Can't check as there is no inverse of the matrix")
    
    
elif M.shape == (3,3):
    M_inv = f.M33inverse(M)
    print("Inverse of the Matrix = ",M_inv)
    #checking
    try:
        print("Checking")
        Checkanswer = f.inverse_checking(M,M_inv)
        print(Checkanswer)
    except TypeError:
        print("Can't check as there is no inverse of the matrix")

else:
    print("This program is written only for (2*2) or (3*3) matrix. So, please change your matrix to be those matrix.")




    
   
