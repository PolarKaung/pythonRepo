import numpy as np

row = int(input("Enter the type of matrix:"))
col = row

m1 = np.zeros((row,col))

for i in range(len(m1)):
    for j in range(len(m1[i])):
        x = int(input("Enter values for matrix 1\n"))
        m1[i,j]= x
print("Matrix 1\n", m1)

m2 = np.zeros((row,col))

for i in range(len(m2)):
    for j in range(len(m2[i])):
        y = int(input("Enter values for matrix 2\n"))
        m2[i,j]= y
print("Matrix \n",m2)

Sub = np.zeros((row,col))

for i in range(len(Sub)):
    for j in range(len(Sub[i])):
        Sub[i,j] = m1[i,j] - m2[i,j]

print("The result is\n", Sub)

