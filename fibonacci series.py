#faibonacci series with user input and possibly user defined starting two digits

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
                


#if terms == 1:
#    print("\nFor %d terms,\nFibonacci sequence is"%terms)
#    print(firstD)
#elif terms == 2:
#    print("\nFor %d terms,\nFibonacci sequence is"%terms)
#    print(firstD)
#    print(secondD)
#else:
#    for i in np.arange(start = 3, stop = terms):
#        nD = firstD + secondD
#        print (nD)
#        firstD = secondD
#        secondD = nD
