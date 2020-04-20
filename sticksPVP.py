print("Welcome to Game of sticks.There are 21 sticks. You can choose from 1 stick to 4sticks")

def gameOverCheck(s,p): #s is number of sticks left and p is the player number
	if(s==0 and p==1):
		print("Player One is a loser")
		exit()
	elif(s==0 and p==2):
		print("Player Two is a loser")
		exit()
	else:
		print(s,"sticks left")

def check(t): #valid move check
	while(t>s or t>4 or t<1):
		if(t>s):
			print("There is not enough sticks")
			t= int(input("Enter again: "))
		elif(t>4 or t<1):
			print("You have to select 1 to 4 sticks")
			t= int(input("Enter again: "))
	return t
#s is sticks
s = 21

#main code
while(s>0):
	p1=0
	p2=0
	p1=int(input("Player One's turn to choose sticks: "))
	p1=check(p1)
	s-=p1
	gameOverCheck(s,1)
	p2=int(input("Player Twosticks: "))
	s-=p2 
	p2=check(p2)
	gameOverCheck(s,2)

	



