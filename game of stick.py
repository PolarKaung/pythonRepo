player_turn = 1
starting_sticks = int(input("How many sticks to start with? (10-100): "))
if starting_sticks >= 10 and starting_sticks <= 100:
    print("Great! Let's play.")
    stick_counter = starting_sticks
    

while True:
    if starting_sticks >= 10 and starting_sticks <= 100:
        print()                   
        if stick_counter != 1:
            print("Turn: Player", player_turn)
            player_turn += 1
            if player_turn == 3:
                player_turn -= 2
            print("There are", stick_counter, "sticks on the table.")
            
        if stick_counter == 1:
            print("Turn: Player", player_turn)
            print("There is", stick_counter, "stick on the table.")
        take_stick = int(input("How many sticks do you want to take? (1, 2, 3 or 4): "))
    
        if take_stick < 1 or take_stick > 4:
            print("Sorry, that's not a valid number.")

        if take_stick > stick_counter:
            print("There's not that many sticks left.")

        elif take_stick >= 1 and take_stick <= 4:
            stick_counter -= take_stick
        
        
        if stick_counter <= 0:
            print()
            print("There are no sticks left on the table! Game over.")
            if player_turn == 1:
                print("Player", (player_turn + 1), "wins!")
            if player_turn == 2:
                print("Player", (player_turn - 1), "wins!")
            break

    else:

        if starting_sticks < 10:
            print("Sorry, that's too few sticks. Try again.")
            starting_sticks = int(input("How many sticks to start with? (10-100): "))
            stick_counter = starting_sticks

            if starting_sticks >= 10 and starting_sticks <= 100:
                print("Great! Let's play.")
                stick_counter = starting_sticks

        elif starting_sticks > 100:
            print("Sorry, that's too many sticks. Try again.")
            starting_sticks = int(input("How many sticks to start with? (10-100): "))
            stick_counter = starting_sticks

            if starting_sticks >= 10 and starting_sticks <= 100:
                print("Great! Let's play.")
                stick_counter = starting_sticks
    
