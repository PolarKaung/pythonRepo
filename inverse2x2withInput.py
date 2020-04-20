import numpy as np
shape = (2,2)
print("Enter the data for the matrix")
A = np.zeros(shape,dtype=float)
print("[1st 2nd"+"\n"+" 3rd 4th]")
k=0		
for i in range(A.shape[0]):
		for j in range(A.shape[1]):
			k+=1
			A[i,j] = float(input("Element %d: " %(k)))


B = np.zeros(A.shape,dtype=float)
detA = (A[0,0]*A[1,1])-(A[0,1]*A[1,0])

if (detA != 0):
	for i in range(A.shape[0]):
		for j in range(A.shape[1]):
			B[i,j] = A[i,j]/detA
	#swapping and adding minus
	B[0,0],B[0,1],B[1,0],B[1,1] = B[1,1],-B[0,1],-B[1,0],B[0,0]
	print ("The inverse of the matrix is \n",B)
else:
	print("Determinant is zero and the inverse does not exist")

