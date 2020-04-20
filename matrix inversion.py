import numpy as np
while True:
    row = int(input("enter the number of rows = "))
    col = int(input("enter the number of columns = "))
    size = (row,col)

    if row == col and 2 <= row <= 3:
        print("\nThe dimension of matrix is %dx%d,"%(row,col))
    else:
        print("\nThe dimension of matrices must be (2,2) and (3,3).\nTRY AGAIN!\n")
        continue
    break


minor = np.zeros((row,col))
cofactor = np.zeros((row,col))
adjoint = np.zeros((row,col)) 
if 2 <= row <= 3:
    a = np.zeros((row,col))
    for i in range(row):
        for j in range(col):
            print("\nposition = (",i,",",j,")")
            a[i,j] = int(input("enter the element:"))
    print("\nthe initial matrix is")
    print(a)

   
    if row == 2:
        adjoint[0,1] = -a[0,1]
        adjoint[1,0] = -a[1,0]
        adjoint[0,0] = a[1,1]
        adjoint[1,1] = a[0,0]
        det = a[0,0]*a[1,1] - a[1,0]*a[0,1]
        if det == 0:
            print("Determinant is zero.\nMatirx inversion can't be perfomed")
        else:
            ainv = adjoint/det
            print("inverse matrix is\n",ainv)
    
                    
    elif row == 3:
        for i in range(row):
            for j in range(row):
                b = []
                for k in range(row):
                    b.append(tuple([i,k]))
                for k in range(row):
                    b.append(tuple([k,j]))
                c = []
                for l in range(row):
                    for m in range(row):
                        if not (l,m) in b:
                            c.append(a[l,m])
                minor[i,j] = c[0]*c[3] - c[1]*c[2]
                cofactor[i,j] = ((-1)**i) * ((-1)**j) * minor[i,j]

        for i in range(row):
            for j in range(row):
                adjoint[i,j] = cofactor[j,i]
        det = np.dot(a[0,:],cofactor[0,:])

        if det == 0:
            print("\nDeterminant is zero.\nMatirx inversion can't be perfomed")
        else:
            ainv = adjoint/det
            print("inverse matrix is \n",ainv)


I = np.identity(row)
c = np.zeros((row,row))
if det != 0:
    for i in range(row):
        for j in range(row):
            for z in range(row):
                c[i,j] += a[i,z]*ainv[z,j]
    c1 = np.round(c)
    answer = c1 == I
    if answer.all():
        print("the answer is correct.")
    else:
        print("the anser is wrong")
