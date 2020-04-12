import numpy as np

A = [[1,2,3], [4,5,6], [7,8,9]]
A = np.array(A)
a = A.shape

AT = np.zeros(a)

for i in range (a[0]):
    for j in np.arange(a[0]):
        AT[j,i] = A[i,j]
print("The transpose of A is \n",AT)
 
    
