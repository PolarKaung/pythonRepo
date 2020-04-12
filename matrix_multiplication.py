import numpy as np
a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
b=np.array([[1,2,3,5],
            [4,5,6,7],
            [7,8,9,10]])
c=np.zeros((len(a),len(b[0])))
print(c)
if len(a[0])==len(b):
    for x in range(len(a)):
        for y in range(len(b[0])):
            for z in range(len(a[0])):
                c[x,y]+=a[x,z]*b[z,y]
    print("The multiplication of 2 matrices is ",np.matrix(c))
else:
    print("The row and column of matrices do not match")
