import numpy as np

A = [[1,2],[3,4]]
B = [[1,2],[3,4]]

A = np.array(A)
B = np.array(B)

a = A.shape
b = B.shape

addition = np.zeros(a)

if a!=b:
    print("Need to match shape")
else:
    for i in range(len(addition)):
        for j in range (len(addition[i])):
            addition[i,j]= A[i,j] + B[i,j]

print("addition:",addition)


