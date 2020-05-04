print("Tic-Tac-Toe")
print("Let's Start!")
pshape =[" 1 "," 2 "," 3 ",
         " 4 "," 5 "," 6 ",
         " 7 "," 8 "," 9 " ]
def p_pshape():
    print(pshape[0] + "|" + pshape[1] + "|" + pshape[2])
    print("-" * 12)
    print(pshape[3] + "|" + pshape[4] + "|" + pshape[5])
    print("-" * 12)
    print(pshape[6] + "|" + pshape[7] + "|" + pshape[8])
p_pshape()
print("The above table shows the position of numbers.")

still_playing_game = True

shape =["   ","   ","   ",
        "   ","   ","   ",
        "   ","   ","   " ]

def p_shape():
    print(shape[0] + "|" + shape[1] + "|" + shape[2])
    print("-" * 12)
    print(shape[3] + "|" + shape[4] + "|" + shape[5])
    print("-" * 12)
    print(shape[6] + "|" + shape[7] + "|" + shape[8])

winner = None

player = " X "

def play_game():
    p_shape()

    #while the game is running
    while still_playing_game:
        turn(player)
        check_game_over()

        #to alternate player's turn
        reverse_turn()

    #Deciding win or draw
    if winner == " X " or winner == " O ":
        print(winner + "win.")
    elif winner == None:
        print("Draw.")

#operation during each player    
def turn(p):

    print("Player" + p + "'s turn.")
    position = input("Enter the numbers from 1-9 to choose the position: ")

    unused_position = False
    while not unused_position:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Please choose only 1-9:")
        
        position = int(position) - 1

        if shape[position] == "   ":
            unused_position = True
        else:
            print("It had been chosen.Please try another position.")

    shape[position] = p
    p_shape()

def check_game_over():
    check_win()
    check_draw()

def check_win():
    global winner
    
    row = check_rows()
    column = check_columns()
    diagonal = check_diagonals()

    if row:
        winner = row
    elif column:
        winner = column
    elif diagonal:
        winner = diagonal
    else:
        winner = None
    return

def check_rows():

    global still_playing_game
    
    row_1 = shape[0] == shape[1] == shape[2] != "   "
    row_2 = shape[3] == shape[4] == shape[5] != "   "
    row_3 = shape[6] == shape[7] == shape[8] != "   "

    if row_1 or row_2 or row_3:
        still_playing_game = False
    if row_1:
        return shape[0]
    elif row_2:
        return shape[3]
    elif row_3:
        return shape[6]
                
    return

def check_columns():
    global still_playing_game
    
    column_1 = shape[0] == shape[3] == shape[6] != "   "
    column_2 = shape[1] == shape[4] == shape[7] != "   "
    column_3 = shape[2] == shape[5] == shape[8] != "   "

    if column_1 or column_2 or column_3:
        still_playing_game = False
    if column_1:
        return shape[0]
    elif column_2:
        return shape[1]
    elif column_3:
        return shape[2]
    return

def check_diagonals():
    global still_playing_game
    
    diagonals_1 = shape[0] == shape[4] == shape[8] != "   "
    diagonals_2 = shape[2] == shape[4] == shape[6] != "   "

    if diagonals_1 or diagonals_2:
        still_playing_game = False
        
    if diagonals_1:
        return shape[0]
    elif diagonals_2:
        return shape[2]
    return

def check_draw():
    global still_playing_game
    if "   " not in shape:
        still_playing_game = False
        
    return

def reverse_turn():
    
    global player
    
    if player == " X ":
        player = " O "
    elif player == " O ":
        player = " X "
            
    return

play_game()
