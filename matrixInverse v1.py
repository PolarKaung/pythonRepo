import numpy as np
A = [
    [2,3,4],
    [3,4,3],
    [1,1,1]
    ]
A = np.array(A)
ASize = A.size
AShape = A.shape

index = []
m = 0
n = 2
minors = np.zeros(AShape)
cofactors = np.zeros(AShape)
adjoint = np.zeros(AShape[::-1])
for m in range(AShape[0]):
    for n in range(AShape[1]):
        index = []
        for i in range (AShape[0]):
            index.append(tuple([i,n]))
        for i in range (AShape[1]):
            index.append(tuple([m,i]))
        detEle = []
        for a in range(AShape[0]):
            for b in range(AShape[1]):
                if not (a,b) in index:
                    detEle.append(A[a,b])
        minors[m,n] = detEle[0]*detEle[3] - detEle[1]*detEle[2]
        cofactors[m,n] = ((-1)**m) * ((-1)**n) * minors[m,n]

det = np.dot(A[0,:],cofactors[0,:])

for m in range(AShape[0]):
    for n in range(AShape[1]):
        adjoint[n,m] = cofactors[m,n]

Ainv = adjoint/det
print("A = ",A)
print('\n')
print("Minors = ",minors)
print('\n')
print("Cofactors = ",cofactors)
print('\n')
print("Adjoint = ",adjoint)
print('\n')
print("Determinent = ", det)
print('\n')
print("Inverse of A = ", Ainv)


