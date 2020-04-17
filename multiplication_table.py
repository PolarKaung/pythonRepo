print("Multiplication Table")

a = int(input("Enter the first number for the range:"))
b = int(input("Enter the final number for the range:"))

for i in range(a,b):
    for j in range(a,b):
        print(i*j, end='\t')
    print('')
        
