import numpy as np
v = []
a = int(input("Enter the number of inputs : "))
for i in range(a):
    n = int(input("Enter value : "))
    v.append(n)

array = np.array(v)
print("The inputs are : ", array)

print("-" * 50)
for j in range(a):
    for k in range(1,11):
        m = array[j] * k
        print("%4d"%m, end=' ')
    print()
print("-" * 50)
