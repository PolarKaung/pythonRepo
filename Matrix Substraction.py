import numpy as np
a = np.array([[1,2],
              [3,4]])

b = np.array([[5,6],
              [7,8]])

a_size = a.shape
b_size = b.shape

if a_size != b_size:
    print("Can't solve. The matrices must be of the same order")

else:
    print("The Substraction is")
    print(a-b)
