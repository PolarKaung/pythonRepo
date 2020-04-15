qty = int(input("How many Fibonacci number you want:"))
f = int(input("1st number:")) 
s = int(input("2nd number:"))
fib = [0]*qty

fib[0]=f	
fib[1]=s

for i in range(qty):
	if(i>1):
		fib[i]=fib[i-1]+fib[i-2]	

print(fib)
