n = int(input("Enter the counts of number : "))

a,b = int(input("Enter 1st number : ")), int(input("Enter 2nd number : "))       
print("Fibonacci Series\n")
count =0
print(a)
print(b)
count = 0
while count<n:
    a,b=b,a+b
    print(b)
    count += 1
