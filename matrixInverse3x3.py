import numpy as np

def det(T):
	T= np.array(T)
	return (T[0,0]*T[1,1])-(T[0,1]*T[1,0])

def transpose(T):
	T = np.array(T)
	B = np.zeros([T.shape[1],T.shape[0]],T.dtype)
	for i in range(T.shape[0]):
		for j in range(T.shape[1]):
			B[j,i] = T[i,j]
	return B

A = np.array([[3,0,2],[2,0,-2],[0,1,1]])
M = np.zeros(A.shape,dtype=float)
minor = np.zeros((2,2),dtype=float)
C = np.zeros((A.shape),dtype=float)
adj = np.zeros((A.shape),dtype=float)
inv = np.zeros((A.shape),dtype=float)
detA =0.0




for i in range(A.shape[0]):
	for j in range(A.shape[1]):

#np.delete(array,row/column number, 0 for row and 1 for column)
		minor = np.delete(np.delete(A,j,1),i,0)
		M[i,j] = det(minor)
		C[i,j] = ((-1)**(i+j))*M[i,j]

adj = transpose(C)

for x in range(A.shape[0]):
	detA += A[0,x]*C[0,x]

inv = adj/detA

print("The inverse of the Matrix is \n",inv)




