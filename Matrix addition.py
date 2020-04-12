import numpy as np

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,3,5],[7,9,11],[13,15,17]]

A = np.array(A)
B = np.array(B)

a = A.shape 
b = B.shape

C = np.zeros(a)


if a != b:
    print("The matrices must have same shape!")
else :
    for m in np.arange(a[0]):
        for n in range (a[0]):
            C[m,n] = A[m,n] + B[m,n]
    print(C)
