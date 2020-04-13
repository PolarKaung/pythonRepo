import numpy as np

A = np.array([[1,2],[3,4],[5,6]])

B = np.zeros([A.shape[1],A.shape[0]],A.dtype) # B is transpose of A

for i in range(A.shape[0]):
	for j in range(A.shape[1]):
		B[j,i] = A[i,j]

print(B)

