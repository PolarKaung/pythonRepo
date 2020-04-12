import numpy as np
a=np.array([[1,2],
            [4,5],
            [7,8]])
b=np.zeros((len(a[0]),len(a)))
for x in range(len(a)):
    for y in range(len(a[0])):
        b[y,x]=a[x,y]
print("The transpose of matrix is ",b)

