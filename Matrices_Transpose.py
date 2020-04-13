import numpy as N
X = N.array([[1,2],[2,3],[3,4]])
Y = N.zeros((len(X[0]),len(X)))
for x in range(len(X)):
    for y in range(len(X[0])):
        Y[y,x]=X[x,y]
print("Transpose is", Y)
