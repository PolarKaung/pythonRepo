import numpy as np

def data(A):
    
    m = int (input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))
    A = np.zeros((m,n))
    a = A.shape
    for i in range (a[0]):
        for j in range (a[1]):
            A[i,j] = int(input("Enter the element of matrix: "))
    return A
  
def transpose(A):
    
    AT = np.zeros(A.shape)                
    for m in range(A.shape[0]):
         for n in range(A.shape[1]):
             AT[m,n] = A[n,m]
    #print("The transpose of the given matrix is \n",AT)
    return AT

def add(A,B):
 
     a = A.shape
     b = B.shape
     C = np.zeros(a)
    
     if a != b:
         print("The matrices must have same shape!")
     else :
         for m in np.arange(a[0]):
             for n in range (a[0]):
                 C[m,n] = A[m,n] + B[m,n]
     #print("The Sum of two matrices:/n",C)
     return C
    
def sub(A,B):
 
     a = A.shape
     b = B.shape
     C = np.zeros(a)
    
     if a != b:
         print("The matrices must have same shape!")
     else :
         for m in np.arange(a[0]):
             for n in range (a[0]):
                 C[m,n] = A[m,n] - B[m,n]
    # print("The Subtraction of the Matrix: /n",C)
     return C

def multi(A,B):
    
    a = A.shape
    b = B.shape
    C = np.zeros((a[0],b[1]))
    
    if a[1] != b[0]:
        print("The Colum of 1st matrix must be the same as the row of 2nd matrix")
    else:
        for i in range(a[0]):
            for j in range(b[1]):
                for k in range(a[1]):
                    C[i,j]= C[i,j] + A[i,k]*B[k,j]
##    print("The Multiplicated Matrix = \n",C)
    return C
    
def Min(A): # 3x3 Minor
    a = A.shape
    #three_det  =0
    minor = np.zeros(a)
    for m in range(a[0]):
        for n in range (a[1]):
            remove = []
            for i in range(a[0]):
                remove.append (tuple([m,i]))
            for i in range (a[1]):
                remove.append(tuple([i,n]))
            det = []
            for x in range(a[0]):
                for y in range(a[1]):
                    if not(x,y) in remove:
                        det.append(A[x,y])
            minor[m,n] = det[0]*det[3] - det[1]*det[2]
         
          
    return minor

def threeDet(A):
    a = A.shape
    minor = np.zeros(a)
    cofactor = np.zeros(a)
    adjoint = np.zeros(a)
    minor = Min(A)
    
    for m in range(a[0]):
        for n in range (a[1]):
            cofactor[m,n] = ((-1)**m) * ((-1)**n) * minor[m,n]
            #cofactor[m,n] = (-1**(m+n)) * minor[m,n]
    Det = np.dot(A[0,:],cofactor[0,:])
  
              
    return Det

def fourDet(A):
    
    a = A.shape
    minor = np.zeros(a)
    cofactor = np.zeros(a)
    adjoint = np.zeros(a)
    
    
    for m in range(a[0]):
        for n in range (a[1]):
            remove = []
            for i in range(a[0]):
                remove.append (tuple([m,i]))
            for i in range (a[1]):
                remove.append(tuple([i,n]))
            det = []
            for x in range(a[0]):
                for y in range(a[1]):
                    if not(x,y) in remove:
                        det.append(A[x,y])
                        
            det = np.reshape(det, (3, 3))            
            minor[m,n] = threeDet(det)
            cofactor[m,n] = ((-1)**m) * ((-1)**n) * minor[m,n]
            
    det4 = np.dot(A[0,:],cofactor[0,:])

    return det4
   
def fiveDet(A):
    
    a = A.shape
    minor = np.zeros(a)
    cofactor = np.zeros(a)
    adjoint = np.zeros(a)
    
    
    for m in range(a[0]):
        for n in range (a[1]):
            remove = []
            for i in range(a[0]):
                remove.append (tuple([m,i]))
            for i in range (a[1]):
                remove.append(tuple([i,n]))
            det = []
            for x in range(a[0]):
                for y in range(a[1]):
                    if not(x,y) in remove:
                        det.append(A[x,y])
                        
            det = np.reshape(det, (4, 4))            
            minor[m,n] = fourDet(det)
            cofactor[m,n] = ((-1)**m) * ((-1)**n) * minor[m,n]
            
    det5 = np.dot(A[0,:],cofactor[0,:])

    return det5
   
   
def threeBy3(A) :
    
    a = A.shape
    I = np.eye(3,3)
    Test = np.zeros(a)
    B = np.zeros(a)
    
    minor = np.zeros(a)
    cofactor = np.zeros(a)
    adjoint = np.zeros(a)
    minor = Min(A)
    
    for m in range(a[0]):
        for n in range (a[1]):
            cofactor[m,n] = ((-1)**m) * ((-1)**n) * minor[m,n]
            #cofactor[m,n] = (-1**(m+n)) * minor[m,n]
    Det = np.dot(A[0,:],cofactor[0,:])
    if(Det == 0):
        print("Error! The determinent of the given matrix is zero")
    else:
        for m in range(a[0]):
            for n in range(a[1]):
                adjoint[m,n] = cofactor[n,m]

        A_Inverse = adjoint/Det
        print("Inverse of given 3x3 matrix: \n",A_Inverse)
    
    Test = multi(A_Inverse,A)
    
    B = np.round_(Test)
    
    test = B == I
    if test.all():
        print("The Inverse is correct")
    else:
        print("The Inverse is not correct")
    return A_Inverse


def twoBy2(A):
    
    a = A.shape
    B = np.zeros(a)
    I = np.eye(2,2)
    Test = np.zeros(a)
    A_Inverse = np.zeros(a)
    
    det = A[1,1]*A[0,0] - A[0,1]*A[1,0]
    if(det == 0):
        print("Error! The determinent of the given matrix is zero")
    else:
        inv = [A[1,1], -1*A[0,1], -1*A[1,0], A[0,0]]
        A_Inverse = inv/det
        A_Inverse = np.reshape(A_Inverse,(2,2))
        print("Inverse of given 2x2 matrix: \n", A_Inverse)

    Test = multi(A_Inverse,A)
    
    B = np.round_(Test)
    test = B == I
    if test.all():
        print("The Inverse is correct")
    else:
        print("The Inverse is not correct")
    return A_Inverse

def fourBy4 (A):

    a = A.shape
    minor = np.zeros(a)
    cofactor = np.zeros(a)
    adjoint = np.zeros(a)
    
    I = np.eye(4,4)
    Test = np.zeros(a)
    B = np.zeros(a)
    
    for m in range(a[0]):
        for n in range (a[1]):
            remove = []
            for i in range(a[0]):
                remove.append (tuple([m,i]))
            for i in range (a[1]):
                remove.append(tuple([i,n]))
            det = []
            for x in range(a[0]):
                for y in range(a[1]):
                    if not(x,y) in remove:
                        det.append(A[x,y])
                        
            det = np.reshape(det, (3, 3))            
            minor[m,n] = threeDet(det)
            cofactor[m,n] = ((-1)**m) * ((-1)**n) * minor[m,n]
            
    det4 = np.dot(A[0,:],cofactor[0,:])
    if(det4 == 0):
        print("Error! The determinent of the given matrix is zero")
    else:
        for m in range(a[0]):
            for n in range(a[1]):
                adjoint[m,n] = cofactor[n,m]
        
        A_Inverse = adjoint/det4
        print("The Inverse of the given matrix 4x4 is\n",A_Inverse)
    Test = multi(A_Inverse,A)
    B = np.round_(Test)
    test = B == I
    if test.all():
        print("The Inverse is correct")
    else:
        print("The Inverse is not correct")
    
        
    return A_Inverse 
      

def fiveBy5 (A):
    a = A.shape
    minor = np.zeros(a)
    cofactor = np.zeros(a)
    adjoint = np.zeros(a)

    I = np.eye(5,5)
    Test = np.zeros(a)
    B = np.zeros(a)
    
    
    
    for m in range(a[0]):
        for n in range (a[1]):
            remove = []
            for i in range(a[0]):
                remove.append (tuple([m,i]))
            for i in range (a[1]):
                remove.append(tuple([i,n]))
            det = []
            for x in range(a[0]):
                for y in range(a[1]):
                    if not(x,y) in remove:
                        det.append(A[x,y])
                        
            det = np.reshape(det, (4, 4))            
            minor[m,n] = fourDet(det)
            cofactor[m,n] = ((-1)**m) * ((-1)**n) * minor[m,n]
            
    det5 = np.dot(A[0,:],cofactor[0,:])
    if(det5 == 0):
        print("Error! The determinent of the given matrix is zero")
    else:
        for m in range(a[0]):
            for n in range(a[1]):
                adjoint[m,n] = cofactor[n,m]
        
        A_Inverse = adjoint/det5
        print("The Inverse of the given matrix 5x5 is\n",A_Inverse)
    Test = multi(A_Inverse,A)
    B = np.round_(Test)
    test = B == I
    if test.all():
        print("The Inverse is correct")
    else:
        print("The Inverse is not correct")
    
    return A_Inverse 
      
def sixBy6 (A):
    
    a = A.shape
    minor = np.zeros(a)
    cofactor = np.zeros(a)
    adjoint = np.zeros(a)

    I = np.eye(6,6)
    Test = np.zeros(a)
    B = np.zeros(a)
    
    
    
    for m in range(a[0]):
        for n in range (a[1]):
            remove = []
            for i in range(a[0]):
                remove.append (tuple([m,i]))
            for i in range (a[1]):
                remove.append(tuple([i,n]))
            det = []
            for x in range(a[0]):
                for y in range(a[1]):
                    if not(x,y) in remove:
                        det.append(A[x,y])
                        
            det = np.reshape(det, (5, 5))            
            minor[m,n] = fiveDet(det)
            cofactor[m,n] = ((-1)**m) * ((-1)**n) * minor[m,n]
            
    det6 = np.dot(A[0,:],cofactor[0,:])
    if(det6 == 0):
        print("Error! The determinent of the given matrix is zero")
    else:
        for m in range(a[0]):
            for n in range(a[1]):
                adjoint[m,n] = cofactor[n,m]
        
        A_Inverse = adjoint/det6
        print("The Inverse of the given matrix 6x6 is\n",A_Inverse)
    Test = multi(A_Inverse,A)
    B = np.round_(Test)
    test = B == I
    if test.all():
        print("The Inverse is correct")
    else:
        print("The Inverse is not correct")
    
    
    return A_Inverse 

