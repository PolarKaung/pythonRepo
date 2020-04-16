import numpy as np
import random

print("Three will be 21 sticks. The one whoever takes the last stick will lose!")
stick = 21

turn = random.randint(0,1) #to take turn

if turn == 0:
    print("Its your turn")
    while True:
        print("\nYou: ")
        print("The number of sticks left : %d" %stick)
        you = int(input("Choose stick between 1 - 4 : "))
        if you >= 5 :
            print("Please choose between 1 and 4 ")
        else:
            stick  -= you
            
            if stick == 1 :
               print("Computer chooses the last stick!\nYou Win !!")
               break
               
            
            elif(21 <= stick and stick >= 1) :
                    print("\nComputer: ")
                    take = random.randint(1,4)
                    print("The computer took %d" %take)
                    stick  -= take
                    print("The number of sticks left : %d" %stick)
            elif (4 <= stick and stick >= 1) : #in order not to choose 4 when there's only 4 sticks
                print("\nComputer: ")
                take = random.randint(1,3)
                print("The computer took %d" %take)
                stick  -= take
                print("The number of sticks left : %d" %stick)
                
            elif (3<= stick and stick >= 1 ): #in order not to choose 4 when there's only 3 sticks
                print("\nComputer: ")
                take = random.randint(1,2)
                print("The computer took %d" %take)
                stick  -= take
                print("The number of sticks left : %d" %stick)
            elif (2 <= stick and stick > 1) :
                print("\nComputer: ")
                take = 1
                print("The computer took %d" %take)
                stick  -= take
                print("The number of sticks left : %d" %stick)
                print("\nYou choose the last stick! \nComputer Win !!")
                break


elif turn == 1:
    print("Its computer turn")
    while True:
        
        if(21 <=stick and stick >= 1) :
                    print("\nComputer: ")
                    take = random.randint(1,4)
                    print("The computer took %d" %take)
                    stick  -= take
                    print("The number of sticks left : %d" %stick)
        elif (4 <= stick and stick >= 1) :
            print("\nComputer: ")
            take = random.randint(1,3)
            print("The computer took %d" %take)
            stick  -= take
            print("The number of sticks left : %d" %stick)
            
        elif (3<= stick and stick >= 1 ):
            print("\nComputer: ")
            take = random.randint(1,2)
            print("The computer took %d" %take)
            stick  -= take
            print("The number of sticks left : %d" %stick)
        elif (2 <= stick and stick > 1) :
            print("\nComputer: ")
            take = 1
            print("The computer took %d" %take)
            stick  -= take
            if stick == 1:
                
                print("The number of sticks left : %d" %stick)
                print("You choose the last stick! \nComputer Win !!")
                break
            
        print("\nYou: ")
        print("The number of sticks left : %d" %stick)
        you = int(input("Choose stick between 1 - 4 : "))
        if you >= 5 :
            print("Please choose between 1 and 4 ")
        else:
            stick  -= you
            
            if stick == 1 :
               print("\nComputer chooses the last stick!\nYou Win !!")
               break
        
        
 
    


