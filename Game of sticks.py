print("Welcome from Game of Sticks\n")
print("You can take 1-4 number of sticks at a time.\nWhoever will take the last stick will loose\n")

no_sticks = int(input("Choose the number of sticks you want to play : "))
sticks_left = no_sticks

while True:
    
    user_take = int(input("Take 1-4 sticks : "))
        
    com_take = 5 - user_take
    
    if (user_take >= 5 or user_take <= 0 ):
        print("###You should choose 1 to 4###")
        continue
    
    if (com_take == 1):
        print("You Win")
        break
    
    if (sticks_left == 1):
        print("You Lose")
        break

    print("Computer takes : ", com_take)
    total = user_take + com_take
    sticks_left -= total
    print("Sticks Left : %d \n" %sticks_left )
    
    

    
    
