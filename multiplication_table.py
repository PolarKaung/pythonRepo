n = int(input("Enter the end value for the table:"))

for i in range(1,n):
	for j in range(1,10):
		print(i*j, end = "\t")
	print("\n")
