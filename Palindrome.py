import numpy as np
a = input("Enter a string")

b = a[::-1]
if a == b:
    print("The given input is a Palindrome.")
else:
    print("The given input is not a Palindrome.")
