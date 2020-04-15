import numpy as np
import matlib as mt

A = np.zeros
A = mt.data(A)

B = np.zeros
B = mt.data(B)

C = np.zeros
C = mt.sub(A,B)
print("\nThe subtraction of two matrices is ",C)

C = mt.add(A,B)
print("\nThe sum of the two matrices is ",C)

D = np.zeros
D = mt.twoBy2(A)
C = mt.multi(B,D)
print("\nThe multiplication of the two matrices is ",C)

C = mt.transpose(B)
print("\nThe transpose of the given matrix is ",C)
