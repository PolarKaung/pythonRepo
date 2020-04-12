import numpy as np

m1 = int(input("Enter number of row for 1st matrix:"))
n1 = int(input("Enter number of column for 2nd matrix:"))

a = np.zeros((m1,n1),dtype = int)

for i in range(len(a)):
	for j in range(len(a[i])):
		x = int(input("Enter Elements for 1st matrix:"))				
		a[i,j] = x

m2 = int(input("Enter number of row for 2nd matrix:"))
n2 = int(input("Enter number of column for 2nd matrix:" ))

b = np.zeros((m2,n2),dtype=int)

for i in range(len(b)):
	for j in range(len(b[i])):
		y = int(input("Enter Elements for 2nd matrix:"))
		b[i,j] = y

if a.shape == b.shape:
	c = np.zeros(a.shape,dtype = int)
	for i in range(len(a)):
		for j in range(len(a[i])):
			c[i,j] = a[i,j] - b[i,j]
	print("First matrix:\n",a)
	print("Second matrix:\n",b)
	print("The difference matrix:\n",c)
else:
	print("\nSince the two matrices do not have same size, subtraction cannot be done")
	print("First matrix:\n",a)
	print("Second matrix:\n",b)
	
	

