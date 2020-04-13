import numpy as N
X=N.array(((1,2,3),(4,5,6),(7,8,9)))
Y=N.array(((10,11,12),(13,14,15),(16,17,18)))
Z=N.zeros(X.shape)
if X.shape==Y.shape:
    for i in range(len(X)):
        for j in range(len(X[0])):
            Z[i][j]=X[i][j]*Y[i][j]
                
print("The answer is",N.matrix(Z))
