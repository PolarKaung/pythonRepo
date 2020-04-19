n=int(input("Enter the number of terms : "))
x=int(input("Enter the value of x : "))
series=1
factorial = 1 
for i in range(1,n+1):
    factorial = factorial*i
    print(factorial)
    series+=(x**i)/factorial
print("The sum of series is",round(series,4))

