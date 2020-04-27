#v2 - punctuation removal
A = input("enter anything you want: ")
A = A.lower()
x = []
y = []
half = int(len(A)/2)
end = len(A)

for i in range(len(A)):

	end-=1
	if(65<=ord(A[i])<=90 or 97<=ord(A[i])<=122 or 48<=ord(A[i])<=57):
		x.append(A[i])	
	if(65<=ord(A[end])<=90 or 97<=ord(A[end])<=122 or 48<=ord(A[end])<=57):	
		y.append(A[end])
	

if(x==y):
	print("It is palindrome")
else:	
	print("It is not palindrome")

