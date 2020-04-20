import numpy as np

x = int(input("Till which number you want to see: "))+1#plus one for the number indication row and column

A = np.zeros((x,x),dtype=int)

for i in range(A.shape[0]):
	for j in range(A.shape[1]):
		if(i==0):
			A[i,j]=j
		elif(j==0):		
			A[i,j] = i
		else:
			A[i,j]= i*j



print("The multiplication table is\n",A)

