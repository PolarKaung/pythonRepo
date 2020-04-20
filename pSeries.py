n = int(input("Enter Number of terms: "))
c = int(input("Constant: "))
a=[] #value for coef

for i in range(n):
	a.append(float(input("Enter the a%d: "%i)))
	
for i in range(n):
	print("%f(x-%d)^%d+" %(a[i],c,i),end='')
print('...')

