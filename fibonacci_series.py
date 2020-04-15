
num = int(input("Enter number of Fibonacci Series:"))
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
f = []
f.append(a)

for i in range(1,num):
	
	f.append(b)
	a,b = b,a+b
	
	

print(f)

