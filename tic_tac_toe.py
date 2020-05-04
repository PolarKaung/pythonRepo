import numpy as np

board = []						

def insb():						#creating the backgroud board with empty string
	for i in range(10):	
		board.append(' ')	

def egboard():						#printing the position of board as an example
	print('\n\t' + '1' + ' | ' + '2' + ' | ' + '3')
	print('\t--+---+--')
	print('\t' + '4' + ' | ' + '5' + ' | ' + '6')
	print('\t--+---+--')
	print('\t' + '7' + ' | ' + '8' + ' | ' + '9')

def printboard(bo):					#printing the background board	
	print('\n\t' + bo[1] + ' | ' + bo[2] + ' | ' + bo[3])
	print('\t--+---+--')
	print('\t' + bo[4] + ' | ' + bo[5] + ' | ' + bo[6])
	print('\t--+---+--')
	print('\t' + bo[7] + ' | ' + bo[8] + ' | ' + bo[9])

def play(letter, key):					#insert player and computer input letter to board
    board[key] = letter
	
def free(key):						#check for free space in the board.
	if board[key] == ' ':
		return True

def win(a,l):						#check winning conditions for player and computer
	if (a[1] == l and a[2] == l and a[3] == l) or (a[4] == l and a[5] == l and a[6] == l) or (a[7] == l and a[8] == l and a[9] == l) or (a[1] == l and a[4] == l and a[7] == l) or (a[2] == l and a[5] == l and a[8] == l) or (a[3] == l and a[6] == l and a[9] == l) or (a[1] == l and a[5] == l and a[9] == l) or (a[3] == l and a[5] == l and a[7] == l):
		return True	

			
def freeplace():					#create a new list which contains the free index of board
	freepos = []	
	for i in range(len(board)):
		if free(i):
			freepos.append(i)
	freepos.remove(0)
	return freepos
	
def pickrnd(ls):					#pick random position for computer
	ran = np.random.choice(ls)
	return ran
											
def pcorner():						#to win tic-tac-toe, corners are important
	c = []						#create list for corners of the board
	for i in freeplace():
		if i in [1,3,7,9]:
			c.append(i)	
	return c

def pmid():						#create list for midedges of the board
	m = []
	for i in freeplace():
		if i in [2,4,6,8]:
			m.append(i)
	return m


def player():						#request player(user) input positions
	while True:
		try:
			put = int(input("\nEnter position you want to enter(1-9):"))
			if put > 0 and put < 10:
				if free(put):										
					play("X",put)
					break
						
				else:	
					print("\nYou cannot input in this place, it's already taken")
			else:
				print("\nPosition is out of range. Enter from 1 to 9")

		except ValueError:
			print("\nPosition is integer. You must enter number(1-9)")

def cmp():						#request computer input positions
							
	place = 0
	
	twol = ["O","X"]				#for computer
	for j in twol:               			#to check, who has a chance to win
		for i in freeplace():			#if player has a chance, computer will block it
			textb = board[:]		#if computer has a chance, it will complete it
			textb[i] = j
			if win(textb, j):
				place = i
				return place

	c = pcorner()
	if len(c) != 0:					#if no one has chance, insert in corners
		place = pickrnd(c)
		return place

	m = pmid()
	if len(m) != 0:					#if all corners are full, insert in edges
		place = pickrnd(m)
		return place

def full(board):					#to check whether the board is full or not
    if board.count(' ') > 1:
        return False
    else:
        return True


while True:				
	insb()
	print("\nWelcome to Tic Tac Toe Game!")
	print('You are "X" and Computer is "O"')
	print("Choose the position you want to insert your letter")	
	print("The example board is as follow:")
	egboard()
	printboard(board)
	turn = np.random.randint(1,3)			#randomly check, whose turn first
	
	if turn == 1:					#player play first
		print("\nYour turn first")
		try:
			while not(full(board)):
				if not(win(board, 'O')):
					player()
					printboard(board)
				else:
					print('\n"O" wins the game. Computer is the winner!')
					break
		
				if not(win(board, 'X')):
					p = cmp()
					if p == 0:
						print("\nThe Game is Tie!")
					else:
						play('O', p)
						print('\nComputer placed an "O" in position:', p)
						printboard(board)
				else:
					print('\n"X" wins the game. Nice, you are the winner!')	
					break
			
		except TypeError:
			print("\nThe Game is Tie!")
			
	
	elif turn == 2:					#computer play first
		print("\nComputer turn first")
		try:
			while not(full(board)):
				if not(win(board, 'X')):
					p = cmp()
					if p == 0:
						print("\nThe Game is Tie!")
					else:
						play('O', p)
						print('\nComputer placed an "O" in position:', p)
						printboard(board)
				else:
					print('\n"X" wins the game. Nice, you are the winner!')	
					break
					
				if not(win(board, 'O')):
					player()
					printboard(board)
				else:
					print('\n"O" wins the game. Computer is the winner!')
					break
		except TypeError:
			print("\nThe Game is Tie!")
		
	while True:					#to play again untill exit
		want = input("\nDo you want to play again? (y/n):")
		if want != 'y' and want != 'n':
			print("\nWrong Input, Try again")
		elif want == 'y':
			board.clear()			
			break
		else:	
			print("\nBye Bye!, See you soon\n")
			quit()
