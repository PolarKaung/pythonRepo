import numpy as np

A = [[9,8,7],[6,5,4],[3,2,1]]
B = [[1,2,3],[4,5,6],[7,8,9]]


A = np.array(A)
B = np.array(B)

a = A.shape
b = B.shape
C = np.zeros(a)

if a == b:
    for i in range (a[0]):
        for j in range (a[0]):
            C[i,j] = A[i,j] * B[i,j]

            print(C)
else:
    print("The sizes of matrices are not the same.")



