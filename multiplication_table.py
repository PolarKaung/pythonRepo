size = int(input("Enter the size of the multiplication table: ")) #Getting input, won't go fool-proof here.

for row in range(1,size+1):
    for column in range(1,size+1):
        value = row * column
        print(value,end = "\t")
    print("\n")

