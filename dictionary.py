student = {}
print("Welcome to student dictionary")
while True:
	name = input("\nEnter name of student:")
	roll = input("Enter roll no:")
	
	student[name] = roll
	key = []
	val = []

	for i in student:
		key.append(i)
		val.append(student[i])
	while True:
		a = input("\nWould you like to stop adding and check a dictionary and two lists? (y,n):")
		if a!= 'y' and a!= 'n':
			print("Wrong Input, Try again")
		elif a == 'y':
			print("\nThe dictionary for student:",student)
			print("The key list(Name):",key)
			print("The value list(Roll):",val)
			quit()
		elif a == 'n':
			break
			
