import numpy as np
a = np.array([[1,3,5],
              [2,4,6]])
b = np.zeros((len(a[0]),len(a)))
for p in range(len(a)):
    for q in range(len(a[0])):
        b[q,p] = a[p,q]
print(b)
