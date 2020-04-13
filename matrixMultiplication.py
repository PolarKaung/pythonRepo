import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8],[9,10],[11,12]])
c = np.zeros([a.shape[0],b.shape[1]],dtype=int)

if(a.shape[1]==b.shape[0]):
	for i in range(a.shape[0]):
		for j in range(b.shape[1]):
			for k in range(a.shape[1]):
				c[i,j] += a[i,k] * b[k,j]
	print(c)
				

else:
	print("Matrix A column and Matrix B row must be same")


