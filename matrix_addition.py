import numpy as np
a=np.array(((1,2,3),
            (4,5,6),
            (7,8,9)))
b=np.array(((1,2,3),
            (4,5,6),
            (7,8,9)))
c=np.zeros(a.shape)
print(c)
if a.shape==b.shape:
    for x in range(len(a)):
        for y in range(len(a[0])):
            c[x,y]=a[x,y]+b[x,y]                       
    print("The addtion of two matrices is ",np.matrix(c))
else:
    print("Operation cannot be done because of unmatched size")
    
