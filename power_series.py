n = int(input("Enter the number of terms:"))
c = float(input("Enter the constant:"))

coef = []

for i in range(n):
	x = float(input("Enter the coefficient, a%d: " %i))
	coef.append(x)

for i in range(n):
	print("%.2f(x-%.2f)^%d + " %(coef[i],c,i), end = "")

print("....")
