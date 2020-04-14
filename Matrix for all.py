import numpy as np

##A = [[1,3,9], [2,1,2], [4,8,1]] #3x3
##B = [[1,2],[3,4]] #2x2
##C = [[1,3,2,1],[7,1,3,9],[6,2,1,2],[2,4,8,1]] #4x4
##D = [[1,4,5,8,2],[3,1,3,2,3],[6,4,1,6,6],[7,2,5,1,7],[2,4,5,8,1]]#5x5
##E = [[1,3,4,5,6,7],[2,1,3,4,5,6],[3,2,1,3,4,5],[5,3,2,1,3,4],[6,5,3,2,1,3],[7,6,5,3,2,1]]

##A= np.array(A)
##B = np.array(B)
##C = np.array(C)
##D = np.array(D)
##E = np.array(E)


def transpose():
    m = int(input("Enter row number for the matrix: "))
    n = int(input("Enter column number for the matrix: "))

    A = np.zeros((m,n))
    AT = np.zeros((m,n))


    for i in range(len(A)):
            for j in range(len(A[i])):
                    x = int(input("Enter the elements for 1st matrix:"))				
                    A[i,j] = x
                    
    for m in range(A.shape[0]):
         for n in range(A.shape[1]):
             AT[m,n] = A[n,m]
    print("The transpose of the given matrix is \n",AT)
    return AT

def add():
 
     m = int(input("Enter row number for the first matrix: "))
     n = int(input("Enter column number for the first matrix: "))

     A = np.zeros((m,n))


     for i in range(len(A)):
             for j in range(len(A[i])):
                     x = int(input("Enter the elements for 1st matrix:"))				
                     A[i,j] = x
                    
     m1 = int(input("Enter row number for the first matrix: "))
     n1 = int(input("Enter column number for the first matrix: "))

     B = np.zeros((m1,n1))


     for i in range(len(B)):
             for j in range(len(B[i])):
                     x = int(input("Enter the elements for 1st matrix:"))				
                     B[i,j] = x
     a = A.shape
     b = B.shape
     C = np.zeros(a)
    
     if a != b:
         print("The matrices must have same shape!")
     else :
         for m in np.arange(a[0]):
             for n in range (a[0]):
                 C[m,n] = A[m,n] + B[m,n]
     print("The Sum of two matrices:/n",C)
     return C
    
def sub():
 
     m = int(input("Enter row number for the first matrix: "))
     n = int(input("Enter column number for the first matrix: "))

     A = np.zeros((m,n))


     for i in range(len(A)):
             for j in range(len(A[i])):
                     x = int(input("Enter the elements for 1st matrix:"))				
                     A[i,j] = x
                    
     m1 = int(input("Enter row number for the first matrix: "))
     n1 = int(input("Enter column number for the first matrix: "))

     B = np.zeros((m1,n1))


     for i in range(len(B)):
             for j in range(len(B[i])):
                     x = int(input("Enter the elements for 1st matrix:"))				
                     B[i,j] = x
     a = A.shape
     b = B.shape
     C = np.zeros(a)
    
     if a != b:
         print("The matrices must have same shape!")
     else :
         for m in np.arange(a[0]):
             for n in range (a[0]):
                 C[m,n] = A[m,n] - B[m,n]
     print("The Subtraction of the Matrix: /n",C)
     return C

def multi():
 
     m = int(input("Enter row number for the first matrix: "))
     n = int(input("Enter column number for the first matrix: "))

     A = np.zeros((m,n))


     for i in range(len(A)):
             for j in range(len(A[i])):
                     x = int(input("Enter the elements for 1st matrix:"))				
                     A[i,j] = x
                    
     m1 = int(input("Enter row number for the first matrix: "))
     n1 = int(input("Enter column number for the first matrix: "))

     B = np.zeros((m1,n1))


     if a[1] != b[0]:
         print("The Colum of 1st matrix must be the same as the row of 2nd matrix")
     else:
         for i in range(a[0]):
             for j in range(b[1]):
                 for k in range(a[1]):
                    C[i,j]= C[i,j] + A[i,k]*B[k,j]
     print("The Multiplicated Matrix = \n",C)
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
    return A_Inverse


def twoBy2(A):
    
    a = A.shape
    det = A[1,1]*A[0,0] - A[0,1]*A[1,0]
    if(det == 0):
        print("Error! The determinent of the given matrix is zero")
    else:

        inv = [A[1,1], -1*A[0,1], -1*A[1,0], A[0,0]]
        A_Inverse = inv/det
        print("Inverse of given 2x2 matrix: \n", A_Inverse)
    return A_Inverse

def fourBy4 (A):
    
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
    if(det4 == 0):
        print("Error! The determinent of the given matrix is zero")
    else:
        for m in range(a[0]):
            for n in range(a[1]):
                adjoint[m,n] = cofactor[n,m]
        
        A_Inverse = adjoint/det4
        print("The Inverse of the given matrix 4x4 is\n",A_Inverse)
        
    return A_Inverse 
      

def fiveBy5 (A):
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
    if(det5 == 0):
        print("Error! The determinent of the given matrix is zero")
    else:
        for m in range(a[0]):
            for n in range(a[1]):
                adjoint[m,n] = cofactor[n,m]
        
        A_Inverse = adjoint/det5
        print("The Inverse of the given matrix 5x5 is\n",A_Inverse)
    
    return A_Inverse 
      
def sixBy6 (A):
    
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
    
    return A_Inverse 

  
key = int(input("The functions that you can perform: \n 1 for sum \t 2 for sub \t 3 for multiplication \n 4 for transpose\t \t 5 for inverse\n Enter:" ))

if(key == 5):
    print("In order to perform inverse function, the row no: & colo no: must be same !")
    m = int(input("Enter row number for the matrix: "))
    n = int(input("Enter column number for the matrix: "))

    A = np.zeros((m,n))


    for i in range(len(A)):
            for j in range(len(A[i])):
                    x = int(input("Enter the elements for 1st matrix:"))				
                    A[i,j] = x
    print("A = \n",A)

    if A.shape == (2,2):
        twoBy2(A)
    elif A.shape == (3,3):
        threeBy3(A)
    elif A.shape == (4,4):
        fourBy4(A)
    elif A.shape == (5,5):
        fiveBy5(A)
    elif A.shape == (6,6):
        sixBy6(A)
        
elif(key == 1):
    
    add()


elif(key == 2):
    sub()
    
elif(key == 3):
    multi()
    


elif(key == 4):
    transpose()

else:
    print("Please enter any of the above")
