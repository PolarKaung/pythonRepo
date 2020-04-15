import numpy as np
def M33inverse(A):
    A = np.array(A)
    ASize = A.size
    AShape = A.shape
    index = []
    m = 0
    n = 2
    minors = np.zeros(AShape)
    cofactors = np.zeros(AShape)
    adjoint = np.zeros(AShape[::-1])
    for m in range(AShape[0]):
        for n in range(AShape[1]):
            index =[]
            for i in range (AShape[0]):
                index.append(tuple([i,n]))
            for i in range (AShape[1]):
                index. append(tuple([m,i]))
            detEle =[]
            for a in range(AShape[0]):
                for b in range(AShape[1]):
                    if not (a,b) in index:
                        detEle.append(A[a,b])
            minors[m,n] = detEle[0]*detEle[3] - detEle[1]*detEle[2]
            cofactors[m,n] = ((-1)**m * (-1)**n) * minors[m,n]
    det = np.dot(A[0,:],cofactors[0,:])
    if det!= 0:
        for m in range(AShape[0]):
            for n in range(AShape[1]):
                adjoint[n,m] = cofactors[m,n]
        A_inv = adjoint * (1/det)
        return A_inv
    else:
        return (print("Det becomes zero. Please choose another matrix to solve."))



def multi(x,y):
    if len(x[0]) == len(y):
        B = np.zeros([len(x),len(y[0])])
        if len(x[0]) == len(y):
            for i in range(len(x)):
                for j in range(len(y[0])):
                    for k in range(len(y)):
                            B[i,j] += x[i,k] * y[k,j]
        return B
    else:
        return str("Muliplication of the matrixs can't be done as length of row of first matrix is not equal to the length of column of second matrix.")      




def inverse_checking(x,y):
    B = np.zeros([len(x),len(y[0])])
    if len(x[0]) == len(y):
        if len(x[0]) == len(y):
            for i in range(len(x)):
                for j in range(len(y[0])):
                    for k in range(len(y)):
                        B[i,j] += x[i,k] * y[k,j]
    I = np.eye(len(x),len(x[0]))
    if B.all() == I.all():
        return str("The inverse is correct.")
    else:
        return str("The inverse is not correct.")

    
  
def M22inverse(B):
    if len(B) == len(B[0]):
        a = int(B[0,0])
        b = int(B[0,1])
        c = int(B[1,0])
        d = int(B[1,1])
        det = a*d - b*c
        e = int(-1*b)
        f = int(-1*c)
        C = np.array([[d,e],[f,a]])
        B_inv = (1/det) * C
        return B_inv
    else:
        return str("Can't calculate because the matrix is not a square matrix")



def transpose(X):
    trX = np.zeros((len(X[0]),len(X)),dtype=int)
    for i in range(len(X)):
        for j in range(len(X[0])):
            trX[j,i] = X[i,j]
    return trX



def add(A,B):
    answer = np.zeros([len(A),len(A[0])])
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        for i in range(len(A)):
            for j in range(len(A[0])):
                           answer[i,j] = A[i,j] + B[i,j]
        return answer
    else:
        return str("Can't operate because of different orders of the matrixs")


def sub(A,B):
    answer = np.zeros([len(A),len(A[0])])
    print(answer)
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        for i in range(len(A)):
            for j in range(len(A[0])):
                           answer[i,j] = A[i,j] - B[i,j]
        return answer   
    else:
        return str("Can't operate because of different orders of the matrixs")
        
