import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
a_row, a_col = len(a), len(a[0])
b_row, b_col = len(b), len(b[0])
print("a=",a)
print("b=",b)
print("")
if (a_col == b_row):
    print("the result is")
    shape = (a_row, b_col)
    c = np.zeros(shape)
    for i in np.arange(start = 0, stop = a_row):
        for j in np.arange(start = 0, stop = b_col):
            for z in np.arange(start = 0, stop = a_col):
                h = a[i,z] * b[z,j]
                c[i,j] += h
    print(c)        

else:
    print("Matrix multiplication can't be done.")
    
