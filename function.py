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
        return print("Det becomes zero. Please choose another matrix to solve.")
        
def inverse_checking(x,y):
    B = np.zeros([len(x),len(y[0])])
    if len(x[0]) == len(y):
        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                        B[i,j] += x[i,k] * y[k,j]
        return B
    else:
        return print("Can't operate because of column of first matrix and row of second martrix are not the same")
    


    
