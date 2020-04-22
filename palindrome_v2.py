while True:
	a = input("\nEnter a word of sentence to check whether it is palindrome or not: ")
	
	d = a.lower()
	b = []
	c = []
	word = ""
	for i in d:
		x = ord(i)
		b.append(x)
	
	for i in b:
		if i >= 97 and i <= 122:
			c.append(i)

	for i in c:
		y = chr(i)
		word += y

	rev = word[::-1]

	if word == rev:
		print('\n"%s" is a palindrome' %a)
		while True:
			nex = input("\nWould you like to try another? (y,n):")
			if nex != 'y' and nex != 'n':
				print("Wrong Input, Try again")
			elif nex == 'n':
				quit()
			elif nex == 'y':
				break
	else:
		print('\n"%s" is not a palindrome' %a)
		while True:
			nex = input("\nWould you like to try another? (y,n):")
			if nex != 'y' and nex != 'n':
				print("Wrong Input, Try again")
			elif nex == 'n':
				quit()
			elif nex == 'y':
				break







