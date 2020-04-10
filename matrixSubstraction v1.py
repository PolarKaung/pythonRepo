import numpy as np
A = [
    [2,3,4,5],
    [3,4,5,6],
    [5,3,6,4],
    [3,5,3,6],
    ]

B = [
    [1,2,3,4],
    [2,3,4,5],
    [5,3,6,4],
    [3,5,3,6],
    ]

A = np.array(A)
B = np.array(B)

ASize = A.shape
BSize = B.shape

C = np.zeros(ASize)

if ( ASize != BSize ):
    print("Matrix A and B Dimension or shape must be the same!")
else:
    for m in range(ASize[0]):
        for n in range(ASize[1]):
            C[m,n] = A[m,n] - B[m,n]

    print("A = ", np.matrix(A))
    print("B = ", np.matrix(B))
    print("C = ", np.matrix(C))
