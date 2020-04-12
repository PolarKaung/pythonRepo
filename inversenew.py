#inverse of matrix
a = [[4,7],
     [2,6]]
a1 = a[0][0]
a2 = a[0][1]
a3 = a[1][0]
a4 = a[1][1]

m = a1*a4-a2*a3
multiply= 1/m
a[0][1] = -a2
a[1][0] = -a3
x = a[0][0]
a[0][0]=a[1][1]
a[1][1]=x

print(a)
det = multiply
print(det)

for i in range(2):
  for j in range(2):
     a[i][j] = det * a[i][j]

print(a)
