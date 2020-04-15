n = int(input("Enter the number of Fibonacci Serie: "))

a = 0
b = 1
fiba = []
for i in range(0,n):
    c = a + b
    a = b
    b = c
    fiba.append(c)
    
print(fiba)
