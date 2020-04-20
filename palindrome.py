
A = input("enter anything you want: ")
A = A.lower()
x = []
y = []
half = int(len(A)/2)
end = len(A)

for i in range(len(A)):

	end-=1
	if(A[i]!=' '):
		x.append(A[i])	
	if(A[end]!=' '):	
		y.append(A[end])
	

if(x==y):
	print("It is palindrome")
else:	
	print("It is not palindrome")


