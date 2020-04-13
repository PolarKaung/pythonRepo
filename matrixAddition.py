import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])
c = np.zeros(a.shape,dtype=int)

if (a.shape == b.shape):
	for i in range(a.shape[0]):
		for j in range(a.shape[1]):
			c[i,j] = a[i,j]+b[i,j]
	print (c)
	
else:
	print("Error :The matrices does not have same dimensions")



