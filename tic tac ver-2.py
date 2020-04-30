import random

board = []

for i in range(10):
    board.append("-")
    
def display():
    print(board[1] + " | " + board[2] + " | " + board[3] )
    print(board[4] + " | " + board[5] + " | " + board[6] )
    print(board[7] + " | " + board[8] + " | " + board[9] )
    
print("\nWelcome from the Tic Tac Toe Game!")
display()


def your():
    
    
    you = int(input("\nEnter the position: "))
    
    if board[you] == '-':
        board[you] = "X"
        display()
        
    else:
        while board[you] != '-':
            you = int(input("This place is already chosen!\nTry another: "))
            if board[you] == '-':
                board[you] = "X"
                display()
                break
           

    
    
def comp():
    
    rand = list(range(1,10))
    print("It's computer turn!")
    
    com = random.choice(rand)
    if board[com] == '-':
        board[com] = "O"
        display()
        
    else:
        while board[com] != '-':
            rand.remove(com)
            com = random.choice(rand)
        
            if board.count("-") == 1:
                print("Game is tie!")
                break
    
            if board[com] == '-':
                board[com] = "O"
                display()
                break
    
    
while board.count("-") > 1:    
    your()
    print("\n")
    
    if (board[1] == board[2] == board[3] == 'X') or \
        (board[4] == board[5] == board[6]  == 'X') or \
        (board[7] == board[8] == board[9]  == 'X') or  (board[1] == board[4] == board[7]== 'X') or (board[2] == board[5] == board[8]  == 'X') or (board[3] == board[6] == board[9]  == 'X') or (board[1] == board[5] == board[9]  == 'X') or (board[7] == board[5] == board[3]  == 'X'):
            print("You Win!")
            break
            
    elif (board[1] == board[2] == board[3] == 'O') or \
         (board[4] == board[5] == board[6]  == 'O') or \
          (board[7] == board[8] == board[9]  == 'O') or (board[1] == board[4] == board[7]  == 'O') or (board[2] == board[5] == board[8]  == 'O') or (board[3] == board[6] == board[9]  == 'O') or (board[1] == board[5] == board[9]  == 'O') or (board[7] == board[5] == board[3]  == 'O'):
            print("You Lose!")
            break
        
    if board.count("-") == 1:
        print("Game is tie!")
        break
    comp()
    if (board[1] == board[2] == board[3] == 'X') or \
        (board[4] == board[5] == board[6]  == 'X') or \
        (board[7] == board[8] == board[9]  == 'X') or  (board[1] == board[4] == board[7]== 'X') or (board[2] == board[5] == board[8]  == 'X') or (board[3] == board[6] == board[9]  == 'X') or (board[1] == board[5] == board[9]  == 'X') or (board[7] == board[5] == board[3]  == 'X'):
            print("You Win!")
            break
            
    elif (board[1] == board[2] == board[3] == 'O') or \
         (board[4] == board[5] == board[6]  == 'O') or \
          (board[7] == board[8] == board[9]  == 'O') or (board[1] == board[4] == board[7]  == 'O') or (board[2] == board[5] == board[8]  == 'O') or (board[3] == board[6] == board[9]  == 'O') or (board[1] == board[5] == board[9]  == 'O') or (board[7] == board[5] == board[3]  == 'O'):
            print("You Lose!")
            break
   
        

