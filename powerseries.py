print("Power Series")
import math

x = int(input("Enter the value of x: "))
c = int(input("Enter the value of c: "))
n = int(input("Enter the no: of terms you want to find, n= "))
a = int(input("Enter the value of coefficient, an= "))

print("constant,    x = %d"%x)
print("constant,    c= %d"%c)
print("power,       n=  %d"%n)
print("coefficient, a = %d"%a)

result = 1
sum = 1
if n >= 0:
    for i in range(a, n+1):
        s = x-c
        p = s**i
        m = (1/math.factorial(i))*p
        result *= m
    print("result= %f" %result)
else:
    print("The value of n shoud be positive")
        


