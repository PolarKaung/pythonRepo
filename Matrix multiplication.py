import numpy as np
A = np.array([[5,4,3],[10,5,10],[9,8,7],[3,2,1]])
print(A)
a = A.shape
print(a)
B = np.array([[1,0,0],[0,1,0],[0,0,1]])
print(B)
b = B.shape
print(b)
answer = np.zeros([len(A),len(B[0])])
print(answer)

if len(A[0]) == len(B):
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                answer[i,j] += A[i,k]*B[k,j]
    print("Answer for A*B=",answer)
    print(answer.shape)
else:
    print("Can't operate because of column of first matrix and row of second martrix are not the same")
