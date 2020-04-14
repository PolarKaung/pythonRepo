import numpy as np

A = [[9,8,7],[6,5,4],[3,2,1]]



A = np.array(A)


a = A.shape

C = np.zeros(a)


for i in range (a[0]):
    for j in range (a[0]):
        C[j,i] = A[i,j]

        print("The transpose of A =\n",C)
        

          



            
