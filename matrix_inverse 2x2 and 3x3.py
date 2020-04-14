import numpy as np

n = int(input("Enter the number of rows in a matrix :"))
m = int(input("Enter the number of columns in a matrix :"))
a = np.zeros((m,n))
for i in range (n):
    for j in range(m):
        print("Enter Element No:",i,j)
        a[i][j] = int(input())
print("The matrix is ",np.array(a))
b=np.zeros((len(a[0]),len(a)))

if a.shape==(2,2):
    A=int(a[0,0])
    B=int(a[0,1])
    C=int(a[1,0])
    D=int(a[1,1])
    e=B*(-1)
    f=C*(-1)
    det_a=(A*D)-(B*C)
    if det_a != 0:
        b=np.array([[D/det_a,e/det_a],
           [f/det_a,A/det_a]])
        print("The inverse of matrix is :",b)
    else:
        print("The determinant cannot be zero.")
        
elif a.shape==(3,3):
    A=int(a[0,0])
    B=int(a[0,1])
    C=int(a[0,2])
    D=int(a[1,0])
    E=int(a[1,1])
    F=int(a[1,2])
    G=int(a[2,0])
    H=int(a[2,1])
    I=int(a[2,2])
    det_a=(A*((E*I)-(H*F)))-(B*((D*I)-(G*F)))+(C*((D*H)-(G*E)))
    print("The determinant of matrix is :",det_a)
    if det_a != 0:   
        for x in range(len(a)):
            for y in range(len(a[0])):
                b[y,x]=a[x,y]
        print("The transpose of matrix is ",b)
        A=int(b[0,0])
        B=int(b[0,1])
        C=int(b[0,2])
        D=int(b[1,0])
        E=int(b[1,1])
        F=int(b[1,2])
        G=int(b[2,0])
        H=int(b[2,1])
        I=int(b[2,2])
        b1=E*I-H*F
        b2=D*I-G*F
        b3=D*H-G*E
        b4=B*I-H*C
        b5=A*I-G*C
        b6=A*H-G*B
        b7=B*F-E*C
        b8=A*F-D*C
        b9=A*E-D*B
        adj_b=np.array([[b1,-b2,b3],
               [-b4,b5,-b6],
               [b7,-b8,b9]])
        b_inverse=(1/det_a)*adj_b
        print("The inverse of matrix is ",b_inverse)
    else:
        print("The determinant cannot be zero.")
else:
    print("This code only works for 2x2 and 3x3.")
    



    

