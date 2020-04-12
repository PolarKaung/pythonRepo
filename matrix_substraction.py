import numpy as np
a = np.array([[1,2],[3,4],[5,6]])
b = np.array([[11,12],[13,14],[15,16]])
print("a=",a)
print("b=",b)
if (a.shape == b.shape):
    print("the result is")
    row = len(a)
    column = len(a[0])
    c = np.zeros(a.shape)
    for i in np.arange(start = 0, stop = row):
        for j in np.arange(start = 0, stop = column):
            c[i,j] = a[i,j] - b[i,j]
    print(c)

else:
    print("Matrix substraction can't be done.")
