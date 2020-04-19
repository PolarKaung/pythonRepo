print("Mutltiplication Table")

r = int(input("Enter the nth value you want in the row: "))
c = int(input("Enter the nth value you want in the column:"))
if r >0 and c > 0:
    for i in range(1,r+1):
        print(i, end="\t")
    print()
    d = "-"*100
    print(d)
    for j in range(1,c+1):
        for k in range(1,r+1):
            print("%d"%(j*k),end="\t")
        print()
    print(d)
else:
    print("Please Enter Positive value only for both row and column")
