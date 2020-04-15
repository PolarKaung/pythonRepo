print("Please Enter Positive Numbers")
a = float(input("Enter the first number, n1 = "))
b = float(input("Enter the second number, n2 = "))
count = 0
q = float(input("Quantity of numbers you want:"))

print("Fibonacci Series:")
while count < q:
    print(a)
    nth = a + b
    a = b
    b = nth
    count += 1
