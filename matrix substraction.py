import numpy as np
a = np.array(((1,3),
              (5,7)))
b = np.array(((2,4),
              (6,8)))
c = np.zeros(b.shape)
if a.shape==b.shape:
    for m in range(len(a)):
        for n in range(len(a[0])):
            c[m,n] = a[m,n]-b[m,n]
else:
    print("no result")
print(c)


