import numpy as np
a=np.array([[1,2],
           [3,4]])
A=int(a[0,0])
B=int(a[0,1])
C=int(a[1,0])
D=int(a[1,1])
det_a=(A*D)-(B*C)
e=B*(-1)
f=C*(-1)
b=np.array([[D/det_a,e/det_a],
   [f/det_a,A/det_a]])
print("The inverse of matrix is ",b)
