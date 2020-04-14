import numpy as np

print("FOR 2x2 MATRIX INVERSION;")

print()
a = np.zeros((2,2))
b = np.zeros(a.shape)
inv = np.zeros(a.shape)

for i in range(2):
    for j in range(2):
        print("position = (",i,",",j,")")
        a[i,j] = int(input("enter the element:"))
print()
print("the initial matrix is")
print(a)
print("the size =",a.shape)


det = (a[0,0] * a[1,1]) - (a[0,1] * a[1,0])
print("determinant =",det,'\n')

if (det != 0):
    b[0,0] = a[1,1]
    b[0,1] = -a[1,0]
    b[1,0] = -a[0,1]
    b[1,1] = a[0,0]
    
    inv = (1/det) * b
    print("the inverse matrix is")
    print(inv,'\n')
  
   
    
else:
    print("The matrix inversion can't be done because the determinant value is zero.")
