import numpy as np
a=np.array(((1,2,3),
            (4,5,6),
            (7,8,9)))
b=np.array(((1,2,3,5),
            (4,5,6,7),
            (7,8,9,10)))
column_a=len(a[0])
row_b=len(b)
if column_a==row_b:
    c=np.dot(a,b)
    print("The multiplication of two matrices is ",c)
else:
    print("Operation cannot be done because of unmatched rows and columns.")
            
