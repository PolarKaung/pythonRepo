a = input("Enter a word of sentence to check whether it is palindrome or not: ")

b = a[::-1]

print("The string you entered is:",a)
print("The reverse of its is:",b)

if a == b:
	print("It is a palindrome")

else:	
	print("It is not a palindrome")



