x = int(input("enter the number of integers for horizontal line : "))
y = int(input("enter the number of intergers for vertical line  : "))

print()
i = 0
j = 0
a1 = 1 
for j in range (1,y+1) :
    a2 = a1 * j  
    for i in range (1,x+1):
        a = a2 * i
        print("%4d"%a,end='  ')
    print()
    



