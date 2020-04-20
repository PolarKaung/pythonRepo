import numpy as np
print("POWER SERIES: a[terms]*(x - c)^terms ; terms = from 0 to n\n")
while True:
    try:
        while True:
            terms = int(input("Enter the number of terms : "))
            if terms >= 1:
                break
            else:
                print("\nThe value of terms must be positive.")
                continue
            break
        c = float(input("Enter the value of c : "))
        x = float(input("Enter the value for x : "))
    except ValueError:
        print("\nInvalid input! Enter one more time.\n")
        continue
    break
a = np.zeros([terms])
sum = np.zeros([terms])
total = 0
print()
for i in range(terms):
    while True:
        try:
            a[i] = float(input("Enter the value for a[%d] : "%i))
        except:
            print("\nEnter again.\n")
            continue
        break
    x_c = (x - c)**i
    sum[i] = a[i] * x_c
    total += sum[i]
    #print("x - c = ",x-c)
    #print(sum)
    #print("sum = ",total)
    #print()
    
print("\nThe sum of power series is ",total)
