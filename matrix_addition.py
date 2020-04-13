A= [[1,4,9],
    [2,3,9],
    [3 ,4,5]]

B= [[4,3,1],
    [15,4,5],
    [78,90,34]]

R = [[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
       R[i][j] = A[i][j] + B[i][j]

for r in R:
   print(r)
