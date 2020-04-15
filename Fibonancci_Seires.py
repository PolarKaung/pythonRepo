print("Python Program for Producing Fibonancci Series")

n1 = 0
n2 = 1
count = 0
num = int(input("Please enter the number up to nth term:"))
if num == 0:
    print("-")
elif num == 1:
    print(n1)
elif num == 2:
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
