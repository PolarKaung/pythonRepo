num = int(input("Enter the number of Fibonacci Serie: "))
Sum = 0
fabi = [1,1]

for i in range(num-2): 
    Sum = fabi[i]+fabi[i+1]
    fabi.append(Sum)

print(fabi)
