import numpy as np
def play_game(initial_number):
    cur_stick = initial_number
    player = False
    while cur_stick >= 1:
        rem = input("Enter the number between 1-4 =")
        rem,state = nicheck(rem,cur_stick)
        while not state:
            rem = input("Please enter the valid number =")
            rem,state = nicheck(rem,cur_stick)
        cur_stick -= rem
        print(f"Number of stick left = {cur_stick}")
        if winorlose(cur_stick,player):
            break
        player = True
        print("Computer's Turn.")
        cur_stick -= comp_play(cur_stick)
        print(f"Number of stick left = {cur_stick}")
        if winorlose(cur_stick,player):
            break
        player = False
       
    
def nicheck(number,cur_stick):
    state = True
    checknum = 0
    try:
        checknum = int(number)
        if checknum < 1 or checknum > 4:
            state = False
            print("The number must be between 1 and 4.")
        elif checknum > cur_stick:
            state = False
            print("The remaining stick is less than the number you enter.")
    except ValueError:
        print("The number must be integer.")
        state = False
    return checknum,state


def comp_play(cur_stick):
    if cur_stick > 4:
        chosen = np.random.randint(1,5)
    elif cur_stick == 1:
        chosen = 1
    else:
        chosen = np.random.randint(1,cur_stick)
    return chosen

def winorlose(current_stick,player_or_ai):
    over = False
    if current_stick == 0 :
        if player_or_ai:
            print("Computer have drawn the last stick. You win")
        else:
            print("You have drawn the last stick. Game Over")
        over = True
    return over

#Main Program
ini_num = 21

instruct = input("""
Welcome to game of stick
To start playing, type \"play\"
To learn how to play, type \"learn\"
""").lower()


while instruct != 'learn' and instruct != 'play':
    instruct = input("Please enter the exact command :")

if instruct == 'learn':
    print("""OK, here are the rules
1. There are 21 sticks initially.
2. The user must picks the number between 1-4.
3. The chosen number of sticks will be removed.
4. Then the computer will also choose the number between 1-4.
5. The player who pick the last stick will lose.
""")

while True:
        play_game(ini_num)
        cont = input("Would you like to play again? Type 'yes' to play or anything to quit")
        if cont == 'yes':
            continue
        else:
            break

print("Thanks for playing")

