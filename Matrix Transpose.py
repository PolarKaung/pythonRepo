import numpy as np
a = np.array([[1,2],
              [3,4],
              [5,6]])
b = np.zeros((len(a[0]),len(a)))
for x in range(len(a)):
    for y in range(len(a[0])):
        b[y,x] = a [x,y]
print("The transpose matrix is ", b)
