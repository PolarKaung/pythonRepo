# This is a program to produce Fabonacci Series with User Defined Initials.

n1 = int(input("Enter the first initial of the wanted Fabonacci Series:"))
n2 = int(input("Enter the second iniitial of the wanted Fabonacci Series:"))
count = 0
num = int (input("Enter the numbers of terms you want in the series:"))
if num <= 0:
    print("Enter positive value for the number of terms")
elif num == 1:
    print(n1)
elif num ==2:
    print(n1)
    print(n2)
else:
    print(n1)
    print(n2)
    while count < num-1:
        nth = n1+n2
        n1 = n2
        n2 = nth
        print(n2)
        count += 1
