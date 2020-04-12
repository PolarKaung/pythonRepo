import numpy as np
X = np.array([[1,2,3],[4,5,6]])
print(X)
print(X.shape)
a = len(X)
print(a)
b = len(X[0])
print(b)

transpose_X = np.zeros([b,a])


for i in range(len(X)):
    for j in range(len(X[0])):
        transpose_X[j,i] = X[i,j]
print(transpose_X)
print(transpose_X.shape)
