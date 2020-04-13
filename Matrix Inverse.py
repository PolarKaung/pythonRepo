import numpy as np
a = [[2,2],[3,3]]
a = np.array(a)
b = a[0,0] * a[1,1] - a[0,1] * a[1,0]
if(b == 0):
    print("Inverse Matrix doesn't exist.")
else:
    print ("Determinant = ", b)
    a = [[a[1,1]/b,-a[0,1]/b],[-a[1,0]/b,a[0,0]/b]]
    print ("Inverse matrix is ", np.matrix(a))
