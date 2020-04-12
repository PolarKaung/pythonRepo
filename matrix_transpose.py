import numpy as np
a = np.array([[1,2],[3,4],[5,6]])
shape = (len(a[0]),len(a))
b = np.zeros(shape)
for i in range(len(a)):
    for j in range(len(a[0])):
        b[j,i] = a[i,j]
print("a=",a)
print("the transpose matrix is")
print(b)
        


        

