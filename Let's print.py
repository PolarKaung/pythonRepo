a = int(input("Enter the number to expand: "))
b = str(input("Enther whatever you like to expand: ")) # (eg. *, &, ^) It'll change everything to string.
for i in range(a):
    print("%s" %b*a)
    a = a-1
    
