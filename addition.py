import numpy as np
a=[[0,0],[1,1]]
b=[[1,1],[1,1]]
c=[[0,0],[0,0]]
for x in range(2):
  for y in range(2):
     c[x][y]=a[x][y]+b[x][y]
print("additiion",c)

a=np.array(a)
b=np.array(b)
d=a-b
print("substruction",d)
