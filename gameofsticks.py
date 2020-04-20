import numpy as np 

sticks = 21
a = 0
b = 0

print("Welcome to game of sticks\nYou have 21 sticks\nThe person who choose the last stick will lose")
turn = np.random.randint(1,3)

if turn == 1:
	print("Your turn first")
	while True:
		while True:
			while True:
				while True:
					try:
						print("\nYour turn")
						print("Pick 1-4 sticks")
						me = int(input("Choose 1-4 sticks:"))
						print("The number of sticks you chose = %d" %me)
					except ValueError:
						print("Invalid input, enter integer")
						continue
					break
				if me>=5:
					print("Input is out of range, enter again")
				else:
					break
			a += me
			if a >= sticks:
				print("You chose the last stick, You lose!!")
				quit()
			else:
				break

		while True:
			print("\nComputer turn")
			cmp = np.random.randint(1,5)
			print("The number of sticks Computer chose = %d" %cmp)
			a += cmp
			if a >= sticks:
				print("Computer chose the last stick, You win!!")
				quit()
			else:
				break
		
	
			
	
elif turn == 2:
	print("Computer turn first")
	while True:
		while True:
			print("\nComputer turn")
			cmp = np.random.randint(1,5)
			print("The number of sticks Computer chose = %d" %cmp)
			a += cmp
			if a >= sticks:
				print("Computer chose the last stick, You win!!")
				quit()
			else:
				break
		while True:
			while True:
				while True:
					try:
						print("\nYour turn")
						print("Pick 1-4 sticks")
						me = int(input("Choose 1-4 sticks:"))
						print("The number of sticks you chose = %d" %me)
					except ValueError:
						print("Invalid input, enter integer")
						continue
					break
				if me>=5:
					print("Input is out of range, enter again")
				else:
					break
			a += me
			if a >= sticks:
				print("You chose the last stick, You lose!!")
				quit()
			else:
				break

		
		

		
