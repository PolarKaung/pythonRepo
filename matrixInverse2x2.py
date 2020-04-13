import numpy as np

A = np.array([[3,3.2],[3.5,3.6]])
B = np.zeros(A.shape,dtype=float)

detA = (A[0,0]*A[1,1])-(A[0,1]*A[1,0])

if (detA != 0):
	for i in range(A.shape[0]):
		for j in range(A.shape[1]):
			B[i,j] = A[i,j]/detA
	#swapping and adding minux
	B[0,0],B[0,1],B[1,0],B[1,1] = B[1,1],-B[0,1],-B[1,0],B[0,0]
	print (B)
else:
	print("Determinant is zero and the inverse does not exist")



