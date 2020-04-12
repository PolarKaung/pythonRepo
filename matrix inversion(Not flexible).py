import numpy as np
B = np.array([[9,3],[12,6]])
print(B)
print(B.shape)
if len(B) == len(B[0]):
    a = float(B[0,0])
    b = float(B[0,1])
    c = float(B[1,0])
    d = float(B[1,1])
    det = a*d - b*c
    e = float(-1*b)
    f = float(-1*c)
    C = np.array([[d,e],[f,a]])
    print(C)
    print(C.shape)
    B_inv = (1/det) * C
    print(B_inv)
    print(B_inv.shape)
else:
    print("Can't calculate because the matrix is not a square matrix")
