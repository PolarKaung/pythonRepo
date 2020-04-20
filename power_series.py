print("Format")
print("a + a*(x-c) + a*(x-c)**2 + a*(x-c)**3 + .... + a*(x-c)**n")
result = 0
x = float(input("Enter x :"))
n = int(input("Enter n :"))
c = input("Enter c :")
if not c:
    c = 0
else:
    c = float(c)
a = float(input("Enter a :"))

for i in range(n+1):
    result += (x - c)**i
result *= a
print(result)
