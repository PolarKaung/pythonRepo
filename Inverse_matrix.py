import numpy as np
A=np.zeros((2,2),dtype=float)
for i in range(len(A)):
    for j in range(len(A[i])):
        N = int(input("2*2 matrix required: "))
        A[i,j]= N      
det_A = A[0][0]*A[1][1] - A[1][0]*A[0][1]
print("The determinant is ",det_A)
Inverse_det_A = 1/det_A
print("The inverse of determinant is",Inverse_det_A)
B=np.zeros(A.shape)
print(B)
B[0][0] =  A[1][1]
B[0][1] = -A[0][1]
B[1][0] = -A[1][0]
B[1][1] =  A[0][0]
print("--",B)
Inverse_A =  Inverse_det_A * B
print("The inverse metrix is", Inverse_A)
