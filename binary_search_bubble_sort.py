def inp(ip):
	arr = []
	for i in range(0,ip):
		while True:
			try:
				b = int(input("Enter element %d:" %(i+1)))
				arr.append(b)
				break
			except ValueError:
				print("This is integer array, You must enter integer")
	return arr
	
def bub(a):
	n = len(a)
	for j in range(1,n):
		swp = False
		for i in range(0,n-j):
			if a[i] > a[i+1]:
				a[i],a[i+1] = a[i+1],a[i]
				swp = True
		
		if swp == False:
			break
	return a
	

def bins(c,ele):
	first = 0
	last = len(c)-1
	while first <= last:
		mid = (first + last)/2
		mid = int(mid)
		if ele == c[mid]:
			return mid
		elif ele < c[mid]:
			last = mid-1
		else:
			first = mid+1
	
	return -1
	
while True:
	print("\nWelcome to bubble sorting and binary searching algorithm!!")
	print("Let's search number in an array")
	while True:
		try:
			num = int(input("\nEnter the length of array:"))
			break
		except ValueError:
			print("The length of an array must be integer, Try again")
	
	iarr = inp(num)
	print("The user input array is:",iarr)
	print("Sorting the array in ascending order...")
	sor = bub(iarr)
	print("Sorted array is:",sor)
	
	ano = True
	while ano:
		while True:
			try:
				x = int(input("\nEnter the element you want to search:"))
				break
			except ValueError:
				print("This is integer array, You must search integer")
				
		pos = bins(sor,x)
		if pos != -1:
			print("\nElement %d is at index %d of the array" %(x,pos))
		else: 
			print("\nElement %d is not in the array" %x)
		while True:
			another = input("\nDo you want to search another element in this array? (y/n):")
			if another != 'y' and another != 'n':
				print("Wrong input, Try agian")
			elif another == 'y':
				break
			else:
				ano = False
				break
	
	while True:
		again = input("\nDo you want to start again with new array? (y/n):")
		if again != 'y' and again != 'n':
			print("\nWrong input, Try again")
		elif again == 'y':
			break
		else:
			print("\nBye Bye!, Come and try another algorithms soon")
			quit()
	
				
	
		
	
	
	
