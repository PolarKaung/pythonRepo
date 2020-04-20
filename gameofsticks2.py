import random
print("Game of sticks")
print("There are 21 sticks. \nYou can take 1-4 sticks at a time. \nThe one who take the last stick will lose.")

sticks = 21

onestickleft_userturn = False
while True:
    print("total Sticks left: " , sticks)
    if sticks != 1 and sticks >= 0:
        user_turn = int(input("Take sticks:"))
        sticksleft1 = sticks - user_turn
        if user_turn <= 0 or user_turn >= 5:
            print("Please take 1-4 sticks.")
        else:
            comlist = [1,2,3,4]
            if sticks >= 1:
                c = random.choice(comlist)
                sticksleft2 = sticksleft1 - c
                print("Computer took: " , c , "\n")
    
            else:
                break
    #elif sticks == 0:
       # print("You Win")
    #else:
        #print("You Win")
        #break
        
    sticks = sticksleft2
    if sticksleft1 != 1 and sticksleft1 >= 0:
            print("Sticks left after user: " , sticksleft1)
    elif sticksleft1 == 1:
            print("Sticks left after user: " , sticksleft1)
            print("Congratulations! \nYou Win!")
            break
    elif sticksleft2 != 1 and sticksleft2 >= 0:
            print("Computer took: " , c , "\n")
            print("Sticks left after com: " , sticksleft2)
            sticks = sticksleft2
            break
            
    else:
        onestickleft_userturn = True
        print("You lose")
        
    
#while sticks == 1 or sticks == 0 or sticks<= 0 and onestickleft_userturn:
    #print("You Lose")
    #break
