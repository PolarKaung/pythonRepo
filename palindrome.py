import numpy as np

check = input("enter the string to check : ")
reverse = check[::-1]
print("the reverse string is",reverse)
if check == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
