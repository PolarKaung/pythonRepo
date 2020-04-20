import numpy as np
a = int(input("Enter the type of the matrix : "))

m = np.zeros((a,a),dtype=float)
minor = np.zeros((a,a), dtype=float)
cofactor = np.zeros((a,a),dtype=float)
adjoint = np.zeros((a,a),dtype=float)
inverse = np.zeros((a,a),dtype=float)

for i in range(len(m)):
    for j in range(len(m[i])):
        m[i,j] = input("Enter the value : ")

print("The input matrix : \n",m)

#Minors

for i in range(len(m)):
    for j in range(len(m[i])):
        index= []
        for k in range(len(m[i])):
            index.append(tuple([i,k]))
        for k in range(len(m)):
            index.append(tuple([k,j]))
        det=[]
        for x in range(len(m)):
            for y in range(len(m[i])):
                if not (x,y) in index:
                    det.append(m[x,y])
                    
        minor[i,j]=(det[0]*det[3])-(det[1]*det[2])
#Cofactor
        cofactor[i,j]=((-1)**(i+j))*minor[i,j]
            
print("Matrix of Minors : \n",minor)
            
print("Matrix of Cofactors : \n",cofactor)

#Adjoint

for i in range(len(m)):
    for j in range(len(m[i])):
        adjoint[i,j]=cofactor[j,i]

print("Matrix of Adjoint : \n",adjoint)

#Multiply by 1/determinant

determinant=0
for i in range(a):
    determinant += m[0,i] * cofactor[0,i]

print("Determinant : ",determinant)

#inverse

for i in range(len(m)):
    for j in range(len(m[i])):
        inverse[i,j] = (1/determinant) * adjoint[i,j]

print("The inverse of 3x3 Matrix : \n", inverse)





            
        
    
