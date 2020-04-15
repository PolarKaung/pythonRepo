import numpy as np
a = np.array([[1,2],
              [3,4]])

b = np.array([[1,1],
              [2,2]])

a_row, a_col = a.shape
b_row, b_col = b.shape

if a_col == b_row:
    x1 = (a[0,0]*b[0,0])+(a[0,1]*b[1,0])
    x2 = (a[0,0]*b[0,1])+(a[0,1]*b[1,1])
    x3 = (a[1,0]*b[0,0])+(a[1,1]*b[1,0])
    x4 = (a[1,0]*b[0,1])+(a[1,1]*b[1,1])

    s = [[x1,x2],
         [x3,x4]]

    print("The Multiplication of a and b is:")
    print(s)

else:
    print("The given matrices cannot be multipliesd")
