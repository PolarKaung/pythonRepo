import numpy as np

a = np.zeros((2,2),dtype = float)

for i in range(len(a)):
	for j in range(len(a[i])):
		x = int(input("Enter Elements for 2x2 matrix:"))				
		a[i,j] = x

deta = (a[0,0]*a[1,1])-(a[0,1]*a[1,0])

if (deta != 0):
	r = np.zeros((2,2),dtype = float)
	for i in range(len(a)):
		for j in range(len(a[i])):
			r[i,j] = a[i,j]/deta
	
	r[0,0],r[0,1],r[1,0],r[1,1] = r[1,1],-r[0,1],-r[1,0],r[0,0]
	print("The original matrix:\n",a)
	print("The inverse matrix:\n",r)

else:
	print("\nSince determinant of the matrix is zero, the inverse cannot be found")
	print("The original matrix:\n",a)



