import numpy as np

M=np.zeros((3,3),dtype=float)
Minor=np.zeros((3,3),dtype=float)
for i in range(len(M)):
    for j in range(len(M[i])):
        N = int(input("3*3 matrix required: "))
        M[i,j]= N
print("Original matrix is ",M)

#finding determinant
A=M[1,1]*M[2,2]
B=M[1,2]*M[2,1]
C=M[1,0]*M[2,2]
D=M[1,2]*M[2,0]
E=M[1,0]*M[2,1]
F=M[1,1]*M[2,0]
G=M[0,0]
H=M[0,1]
I=M[0,2]
detM =G*(A-B)-H*(C-D)+I*(E-F)
print("The determinant is", detM)
if detM != 0:
    
    #finding minor
    Minor[0,0]=A-B
    Minor[0,1]=C-D
    Minor[0,2]=E-F
    Minor[1,0]=M[0,1]*M[2,2] - M[0,2]*M[2,1]
    Minor[1,1]=M[0,0]*M[2,2] - M[0,2]*M[2,0]
    Minor[1,2]=M[0,0]*M[2,1] - M[0,1]*M[2,0]
    Minor[2,0]=M[0,1]*M[1,2] - M[0,2]*M[1,1]
    Minor[2,1]=M[0,0]*M[1,2] - M[0,2]*M[1,0]
    Minor[2,2]=M[0,0]*M[1,1] - M[0,1]*M[1,0]
    print("The minor of matrix is",Minor)

    #finding Co-factor(Adj)
    if  Minor.shape==M.shape:
        C=np.array([[1,-1,1],[-1,1,-1],[1,-1,1]])
        J=np.zeros(C.shape)
        for i in range(len(Minor)):
            for j in range(len(Minor[0])):
                J[i][j]=Minor[i][j] * C[i][j]
        print("The cofactor matrix is", J)
    else:
        print("Error")

    #finding inverse
    inverse=np.zeros((3,3),dtype=float)
    inverse=1/detM * J
    print("The inverse function is", inverse)

else:
    print("The determinant is zero and the matrix is singular.")
