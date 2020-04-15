import numpy as np


terms = int(input("enter the number of terms : "))


if terms <= 0:
    print("\nplease enter positive number.")


else:
    firstD = int(input("\nenter the value for first digit ="))
    secondD = int(input("enter the value for second digit ="))
    print("\nFibonacci sequence is")
    print()
    print(firstD)
    if terms >= 2:
        print(secondD)
        for i in np.arange(start = 2, stop = terms):
            nD = firstD + secondD
            print (nD)
            firstD = secondD
            secondD = nD
                
