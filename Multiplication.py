import numpy as np

print("1st Matrix")
row1,col1 = int(input("Enter number of roll:")),int(input("Enter number of column:"))

print("2nd Matrix")
row2,col2= int(input("Enter number of roll:")),int(input("Enter number of column:"))

A = np.zeros((row1,col1))
B = np.zeros((row2,col2))

if ( col1!= row2):
    print("Column 1 and Row 2 need to be the same")
else:
    for i in range(len(A)):
        for j in range(len(A[i])):
            x = int(input("Enter values of matrix 1\n"))
            A[i,j] = x
print(A)
    
for i in range(len(B)):
    for j in range(len(B[i])):
        y = int(input("Enter values of matrix 2\n"))
        B[i,j] = y
print(B)

mul = np.zeros((row1,col2))

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(A[0])):
            mul[i,j] += A[i,k] * B[k,j]
        
print("The Result is\n", mul) 


