import numpy as np

#Fibonacci_series_using_Binet's_Formula
n1 = int(input("Please enter initial value: "))
n2 = int(input("Please enter final value: "))

n = np.arange(n1, n2)
sqrt5 = np.sqrt(5)
phi = (1 + sqrt5)/2
fibonacci = np.rint((phi**n - (-1/phi)**n)/sqrt5)
print("Fibonacci", fibonacci)


