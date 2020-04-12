import numpy as np

A = [[1,2,3],[4,5,6]]
B = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

A = np.array(A) #(2,3)
B = np.array(B) #(3,4)

a = A.shape
b = B.shape

C = np.zeros((a[0],b[1]))

if a[1] != b[0]:
    print("The Colum of 1st matrix must be the same as the row of 2nd matrix")
else:
    for i in range(a[0]):
        for j in range(b[1]):
            for k in range(a[1]):
               # C[i,j]= (A[i,j]*B[j,i])+(A[i,j+1]*B[j+1,i]+(A[i,j+2]*B[j+2,i]))
               C[i,j]= C[i,j] + A[i,k]*B[k,j]
print("The Matrix C = \n",C)



