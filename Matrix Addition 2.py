import numpy as np
A = np.array([[1,2],[3,4]])
print(A)
a = A.shape
print(a)
B = np.array([[4,5],[3,0]])
print(B)
b = B.shape
print(b)
answer = np.zeros([len(A),len(A[0])])
print(answer)
if a == b:
    for i in range(len(A)):
        for j in range(len(A[0])):
                       answer[i,j] = A[i,j] + B[i,j]
    print("answer of A+B=",answer)
    print(answer.shape)
else:
    print("Can't operate because of different orders of the matrixs")
