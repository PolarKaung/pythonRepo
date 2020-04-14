import numpy as np

a = np.zeros((3,3),dtype = float)

for i in range(len(a)):
	for j in range(len(a[i])):
		x = int(input("Enter Elements for 3x3 matrix:"))				
		a[i,j] = x

minor = np.zeros((a.shape),dtype = float)
cof = np.zeros((a.shape),dtype = float)
adj = np.zeros((a.shape),dtype = float)
inv = np.zeros((a.shape),dtype = float)
deta = 0.0

for i in range(len(a)):
	for j in range(len(a[i])):
		index = []
		for m in range(len(a[i])):
			index.append(tuple([i,m]))
		for m in range(len(a)):
			index.append(tuple([m,j]))
		detNum = []
		for x in range(len(a)):
			for y in range(len(a[i])):
				if not (x,y) in index:
					detNum.append(a[x,y])
		minor[i,j] = detNum[0]*detNum[3]-detNum[1]*detNum[2]
		cof[i,j] = ((-1)**(i+j))*minor[i,j]

for k in range(len(a[0])):
	deta += a[0,k]*cof[0,k]

for i in range(len(a)):
	for j in range(len(a[i])):
		adj[i,j] = cof[j,i]

inv = adj/deta

print("\nThe original matrix:\n",a)
print("\nThe inverse matrix:\n",inv)

y = input("\nPress C to check:")

if y!= 'C':
	print("Wroug Input")
else:
	iden = np.zeros((a.shape),dtype = float)
	for i in range(len(a)):
		for k in range(len(a[0])):
			for j in range(len(a[0])):
				iden[i,k] += a[i,j]*inv[j,k]
	iden = np.round_(iden)	
	print("The product of a matrix and its inverse:\n",iden)
	
	idenI = np.eye(3,3)
	if np.array_equal(iden,idenI):
		print("The inverse is correct")
	else:
		print("The inverse is incorrect")



		

	




