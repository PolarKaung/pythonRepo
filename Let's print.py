a = int(input("Enter the number to expand: "))
b = str(input("Enther whatever you like to expand: ")) # (eg. *, &, ^)
for i in range(a):
    print("%s" %b*a)
    a = a-1
    
