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


def your(let):
    
    
    you = int(input("\nEnter the position: "))
    
    if board[you] == '-':
        board[you] = let
        display()
        
    else:
        while board[you] != '-':
            you = int(input("This place is already chosen!\nTry another: "))
            if board[you] == '-':
                board[you] = let
                display()
                break
           
def winner(board,let):
     
     return (board[1] == let and board[2] == let and board[3] == let) or \
        (board[4] == let and board[5] == let and board[6]  == let) or \
        (board[7] == let and board[8] == let and board[9]  == let) or  (board[1] == let and board[4] == let and board[7]== let) or (board[2] == let and  board[5] == let and board[8]  == let) or (board[3] == let and board[6] == let and board[9]  == let) or (board[1] == let and board[5] == let and board[9]  == let) or (board[7] == let and board[5] == let and board[3]== let)


def comp(let):
    
    move = []
    com = 0
    
    for i in range(len(board)):           #nay yar loot shr tr
        if board[i] == '-':
            move.append(i)
    move.remove(0)                          # 0 ko ma lo chin loh
    print(move)
    
    for j in "X","O":
        for i in move:
            boardcopy = board[:]           
            boardcopy[i] = j                 # test whether if player can win
            
            if winner(boardcopy,j):
                com = i
                board[com] = "0"
                display()
                print("Check")
                return board[com]
            
              
               
            
    corner = []
    for i in move:
        if i in [1,3,7,9]:
            corner.append(i)
    if len(corner) >0:
        com = random.choice(corner)
        board[com] = "O"
        display()
        print("Corner")
        return board[com]

    edge = []
    for i in move:
        if i in [2,4,6,8]:
            edge.append(i)
    if len(edge) >0:
        com = random.choice(edge)
        board[com] = "O"
        display()
        print("Edge")
        return board[com]
    
    if 5 in move:
        board[5] = "O"
        display()
        print("Middle")
        return board[5]


while board.count("-") > 1:
    
    your("X")
    print("\n")
    if winner(board,"X"):
        print("X wins the game!")
        break
    else:
        pass

    if board.count("-") == 1:
        print("Game is tie!")
        break
    
    comp("O")
    if winner(board,"O"):
        print("O wins the game!")
        break
    
        

