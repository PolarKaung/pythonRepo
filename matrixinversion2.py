print("Finding inverse of a 3x3 matrix")
import numpy as np

a = int(input("Enter no of rows of the matrix:"))
b = int(input("Enter no of columns of the matrix:"))

A = np.zeros((a,b),dtype = int)

for i in range(a):
   for j in range(b):
            A[i,j]=(int(input("Enter the entries for the matrix:")))
          
      
print("Matrix, A =",A)

A = np.array(A)

minors = np.zeros(A.shape)
cofactors = np.zeros(A.shape)
adjoint = np.zeros(A.shape[::-1])
for m in range(A.shape[0]):
    for n in range(A.shape[1]):
        index = []
        for p in range (A.shape[0]):
            index.append(tuple([p,n]))
        for p in range (A.shape[1]):
            index.append(tuple([m,p]))
        det = []
        for q in range(A.shape[0]):
            for r in range(A.shape[1]):
                if not (q,r) in index:
                    det.append(A[q,r])
        minors[m,n] = det[0]*det[3] - det[1]*det[2]
        cofactors[m,n] = ((-1)**m) * ((-1)**n) * minors[m,n]

det1 = np.dot(A[0,:],cofactors[0,:])

while True:
   if det1 == 0:
   
      RuntimeWarning
      print("Determinant shouldn't be zero")
   if det != 0:
      break
   
for m in range(A.shape[0]):
    for n in range(A.shape[1]):
        adjoint[n,m] = cofactors[m,n]
Ainv = adjoint/det1

Ainv = np.array(Ainv)
while True:
   if Ainv.all():
      
      RuntimeWarning
      print("Inverse matrix does not exit.")
      break
   

print("Matrix of minors= ",minors)
print("Matrix of cofactors = ",cofactors)
print("Adjugate = ",adjoint)
while True:
   if det1 == 0:
      print("Inverse matrix can't be found")
      Ainv = np.array([[np.nan, np.nan, np.nan],
                       [np.nan, np.nan, np.nan],
                       [np.nan, np.nan, np.nan]])
   break

print("Determinant = ", det1)
print("Inverse of A = ", Ainv)

z = np.zeros((len(A),len(Ainv[0])))

if len(A)==len(Ainv[0]):
   for p in range(len(A)):
       for q in range(len(A[0])):
           for r in range(len(Ainv[0])):
                 z[p,r] += A[p,q]*Ainv[q,r]

I = np.eye(3)

z1 = np.round(z)
result = z1 == I


if result.all():
   print("Product of matrix A and Inverse of matrix A is equal to matrix I.")
   print("The answer is correct.")
else:
   print("The answer is wrong")
