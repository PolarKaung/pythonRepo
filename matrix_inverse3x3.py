import numpy as np

print("FOR 3x3 MATRIX INVERSION;")

print()
a = np.zeros((3,3))
c = np.zeros(a.shape)
b = np.zeros(a.shape)
det = np.zeros(a.shape)
inv = np.zeros(a.shape)

for i in range(3):
    for j in range(3):
        print("position = (",i,",",j,")")
        a[i,j] = int(input("enter the element:"))
print()
print("the initial matrix is")
print(a)
print("the size =",a.shape)

c[0,0] = a[1,1] * a[2,2] - a[2,1] * a[1,2]
c[0,1] = a[1,0] * a[2,2] - a[2,0] * a[1,2]
c[0,2] = a[1,0] * a[2,1] - a[2,0] * a[1,1]
c[1,0] = a[0,1] * a[2,2] - a[2,1] * a[0,2]
c[1,1] = a[0,0] * a[2,2] - a[2,0] * a[0,2]
c[1,2] = a[0,0] * a[2,1] - a[2,0] * a[0,1]
c[2,0] = a[0,1] * a[1,2] - a[1,1] * a[0,2]
c[2,1] = a[0,0] * a[1,2] - a[1,0] * a[0,2]
c[2,2] = a[0,0] * a[1,1] - a[1,0] * a[0,1]

for i in range(len(a)):
    for j in range(len(a[0])):
        b[j,i] = int(c[i,j])
b[0,1] = -b[0,1]
b[1,0] = -b[1,0]
b[1,2] = -b[1,2]
b[2,1] = -b[2,1]


det = a[0,0] * c[0,0] + a[0,1] * c[0,1] + a[0,2] * c[0,2]
print("determinant =",det,'\n')

if (det != 0):
    inv = (1/det) * b
    print("the inverse matrix is")
    print(inv,'\n')
  
else:
    print("the matrix inversion can't be done because the determinant value is zero.")

