coe = [] 
A = []
num = int(input("Enter the number to expand: "))
C = float(input("Enter the constant: "))

#To get coeffients in one list

for i in range(num):
    a = float(input("Enter the value of a%d: " %i))
    coe.append(a)

#print the output

for j in range(num):
    [print("%f(x-%f)^%f + "%(coe[j],C,j), end = ' ')]
print("...")
    
 
    
    
