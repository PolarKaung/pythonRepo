b = int(input("Enter the value to stop: "))

for i in range(1,b+1):
    for j in range(1,b+1):
        print(i*j, end = '\t')   
    print('')
