import numpy as np
B = np.array([[9,3],[12,6]])
print(B)
print(B.shape)
if len(B) == len(B[0]):
    det_b = round(np.linalg.det(B))
    print("Determinant of B=",det_b)
    inv_B = np.linalg.inv(B)
    print("Inverse of matraix B=",inv_B)
    print(inv_B.shape)
else:
    print("can't calculate because the matrix is not a square matrix")

