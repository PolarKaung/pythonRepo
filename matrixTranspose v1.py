import numpy as np
A = [
    [2,3,4,5],
    [3,4,5,6],
    ]

A = np.array(A)

ASize = A.shape
ASizeR = ASize[::-1]

C = np.zeros(ASizeR)
##
for m in range(ASize[0]):
    for n in range(ASize[1]):
        C[n,m] = A[m,n]

print("A' = ", np.matrix(C))
