import numpy as np
a = np.array([[1,2],
              [3,4]])

det_a = (a[0,0]*a[1,1])-(a[0,1]*a[1,0])

b = det_a

if b != 0:
    print("The inverse of the given matrix is:")
    print(a/b)
    
else:
    print("The inverse of the matrix does not exist")
