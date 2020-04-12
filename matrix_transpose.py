import numpy as np

m = int(input("Enter number of row:"))
n = int(input("Enter number of column:"))

a = np.zeros((m,n),dtype = int)

for i in range(len(a)):
	for j in range(len(a[i])):
		x = int(input("Enter Elements:"))				
		a[i,j] = x

b = np.zeros((n,m),dtype = int)

for i in range(len(b)):
	for j in range(len(b[i])):
		b[i,j] = a[j,i]

print("The original matrix:\n",a)
print("The transpose matrix:\n",b)
