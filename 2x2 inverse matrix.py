import numpy as np
a = int(input("Enter the type of the matrix : "))


while True:
    A=np.zeros((a,a))

    for i in range(len(A)):
        for j in range(len(A[i])):
            n = (input("Enter the value of the matrix : "))
            A[i,j] = n

    print("The Matrix is : \n", A)

    det_A= (A[0,0] * A[1,1]) - ((A[0,1]) * (A[1,0]))
    
    if det_A == 0:
        print("Determinant is zero. There is no matrix. Try again")
        continue

    b = A[0,0]
    A[0,0] = A[1,1]
    A[1,1] = b

    A[1,0] = -A[1,0]
    A[0,1] = -A[0,1]

    I=np.zeros((a,a))

    for i in range(len(A)):
        for j in range(len(A[i])):
            I[i,j] = (1/det_A)*A[i,j]

    print("The Inverse Matrix is : \n", I)
    break



