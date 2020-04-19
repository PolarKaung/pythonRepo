print("Welcome to the Game of Sticks")
print(" Rules: There will be a number of sticks. Each player has to draw sticks(1 to 3 sticks) alternatively. The one who picks up the last stick loses.")
print(" Choose from the options:")
print("1. Play against computer")
print("2. Play against a friend")
op = int(input("Your choice: "))
sticks = int(input("Choose numbers of sticks you want to start the game from 10 to 50: "))
if sticks > 10 and sticks <=50:
    # against computer
    if op == 1:
        print("You are now playing with computer.")
        while True:
            print("Sticks left : ",sticks)
            sticks_taken = int(input("Take sticks(1-3): "))
            if sticks_taken >3 or sticks_taken <= 0:
                print("Wrong choise")
                continue
            sticks -= sticks_taken
            if sticks <1:
                print(" You took the last stick. You loose.")
                break
            if sticks >=1:
                com_take = 4 - sticks_taken
                print("Computer took: ",com_take, "\n")
            sticks -= com_take
            if sticks <= 0:
                print("Computer took the last stick. You Win!")
                break
            
    # two player_mode

        
    else:
        print("You are now playing with another player.")
        player1 = str(input("Enter your name:"))
        print("Player1 is ",player1)
        player2 = str(input("Enter your name:"))
        print("Player2 is ",player2)
        print()
        while True:
            print("Stick left:",sticks)
            print(player1,"'s turn")
            p1_take = int(input("Take sticks(1-3):"))
            while p1_take >3 or p1_take <= 0:
                print("Wrong choice")
                p1_take = int(input("Take sticks(1-3):"))
            sticks -= p1_take
            if sticks <1:
                print("You took the last stick. You loose...",player1)
                print("You Win!",player2)
                break
            print(player2,"'s turn")
            p2_take = int(input("Take sticks(1-3):"))
            while p2_take >3 or p2_take <= 0:
                print("Wrong choice")
                p2_take = int(input("Take sticks(1-3):"))
                continue
            sticks -= p2_take
            if sticks < 1:
                print("You took the last stick. You loose...",player2)
                print("You Win!",player1)
                break
        
else:
    print("Choose the number between 10 and 50 only")
    


            
               
   
        


