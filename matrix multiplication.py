import numpy as np
a = np.array(((1,3),
              (5,7)))
b = np.array(((2,4),
              (6,8)))


c = np.zeros((len(a),len(b[0])))

if len(a)==len(b[0]):
    for p in range(len(a)):
        for q in range(len(a[0])):
             for r in range(len(b)):
                 c[p,r] += a[p,q]*b[q,r]
    print(c)
else:
    print("no result")
