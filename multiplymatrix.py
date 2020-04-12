
a=[[1,1],
    [2,2]]
b=[[1,1],
   [2,2]]
n=int(2)
for x in range(1):
    for y in range(1):
       c1=(a[x][y]*b[x][y] + a[x][y]*b[x+1][y])
       print("c1",c1)
    print("\n")

for x in range(1):
    for y in range(1,2):
       c2=(a[x][y]*b[x][y] + a[x][y]*b[x+1][y])
       print("c2",c2)
    print("\n")

for x in range(1,2):
    for y in range(1):
       c3=(a[x][y]*b[x-1][y] + a[x][y]*b[x][y])
       print("c3",c3)
    print("\n")

for x in range(1,2):
    for y in range(1,2):
       c4=(a[x][y]*b[x-1][y] + a[x][y]*b[x][y])
       print("c4",c4)
    print("/n")

u=[[c1,c2],[c3,c4]]
print("multiplication result= ",u)
