print("This is the power series program")
x = int(input("Enter the value of x : "))
c = int(input("Enter the value of constant : "))
n = int(input("Enter the number of counts : "))

a = [] * n
for i in range(n):
    print("For %d th value" %(i+1))
    a.append(int(input("Enter the value of a : ")))
    
sum = 0
for j in range(n):
    d = int(x-c)
    sum += a[j]*(d**j)

print("The sum of Power Series : ", sum)



