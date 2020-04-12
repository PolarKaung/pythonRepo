import numpy as np

m1 = int(input("Enter number of row for 1st matrix:"))
n1 = int(input("Enter number of column for 1st matrix:"))

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

if n1 == m2:
	c = np.zeros((m1,n2),dtype = int)
	for i in range(len(a)):
		for k in range(len(b[0])):
			for j in range(len(a[0])):
				c[i,k] += a[i,j]*b[j,k]
	print("First matrix:\n",a)
	print("Second matrix:\n",b)
	print("The product matrix:\n",c)
else:
	print("\nSince the column of first matrix and the row of second matrix are not the same, the multiplication cannot be done")
	print("First matrix:\n",a)
	print("Second matrix:\n",b)

