import numpy as np
A = [
    [1,1,1],
    [3,4,5],
    ]

B = [
    [1,2],
    [5,3],
    [2,1]
    ]

A = np.array(A)
B = np.array(B)

ASize = A.shape
BSize = B.shape

C = np.zeros((ASize[0], BSize[1]))
##
if ( ASize[1] != BSize[0] ):
    print("Matrix A column and B row must be the same!")
else:
    for m in range(ASize[0]):
        for k in range(BSize[1]):
            for n in range(ASize[1]):
                C[m,k] = C[m,k] + A[m,n]* B[n,k]
    print("A = ", np.matrix(A))
    print("B = ", np.matrix(B))
    print("A*B = C = ", np.matrix(C))

