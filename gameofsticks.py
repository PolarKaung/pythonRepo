print("Game of sticks")
print("There are 21 sticks. \nYou can take 1-4 sticks at a time. \nThe one who take the last stick will lose.")

sticks = 21

while sticks != 1 and sticks >= 0:
    #print("Sticks left: " , sticks)
    user_turn = int(input("Take sticks:"))
    com_turn = (5 - user_turn)
    #print("Computer took: " , com_turn , "\n")
    if user_turn <= 0 or user_turn >= 5:
        print("Please take 1-4 sticks.")
    else:
        print("Computer took: " , com_turn , "\n")
        T = user_turn + com_turn          
        sticks -= T
    print("Sticks left: " , sticks)
    #if user_turn <= 0 or user_turn >= 5:
        #print("Please take 1-4 sticks")

print("You took the last stick, you lose")
    



    
