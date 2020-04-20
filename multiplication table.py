a = float(input("enter the first integer : "))
c = float(input("enter the step(the value between two integers)   : "))
x = int(input("enter the number of integers for horizontal line : "))
y = int(input("enter the number of intergers for vertical line  : "))

print()
i = 0
j = 0
for j in range (y) :
    for i in range (x):
        print("%4d"%a,end='  ')
        a += c
    print()
        #if i == x:
          #  i = 0
         #   print()
           # break
       # break



