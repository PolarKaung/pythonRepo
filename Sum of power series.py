import math
print("Program to caluclate the power series with center zero")
n = int(input("Enter the positive value of n for the nth term: "))
print("n = %d"%n)
x = int(input("Enter the value of x: "))
print(" x = %d"%x)
sum1 = 1
if n >= 0: 
    for i in range(1,n+1):
        sum1 = sum1 + ((x**i)/math.factorial(i))
    print(" The sum of power series is %f"%sum1)
else:
    print("Please choose positive number for n")
        



