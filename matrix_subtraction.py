import numpy as np
a=np.array(((1,2,3),
            (4,5,6),
            (7,8,9)))
b=np.array(((1,2,3),
            (4,5,6),
            (7,8,9)))
if a.shape==b.shape:
    c=a-b
    print("The subtraction of two matrices is ",c)
else:
    print("Operation cannot be done because of unmatched size")
