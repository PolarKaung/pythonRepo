print("\nWelcome from the Game of stick\nThree will be 21 sticks. The one whoever takes the last stick will lose!\n(Haha, you will always lose)")
stick = 21
you = 0
com = 0

while True:
    if stick <=21 and stick>=4:
        print("\nThe number of stick left: %d" %stick)
        you = int(input("Choose a number between 1 & 4:"))
        if you >= 5:
            print("Please choose between 1 and 4")
        else:
            stick -= you
            if stick ==1:
                print("Computer chooses the last stick!\nYou win!")
                break
            elif(stick == 20):
                com = 4
                stick -= com
                print("\nComputer takes 4")
            elif(stick == 19):
                com = 3
                stick -= com
                print("\nComputer takes 3")
            elif(stick == 18):
                com = 2
                stick -= com
                print("\nComputer takes 2")
            elif(stick == 17):
                com = 1
                stick -= com
                print("\nComputer takes 1")
                
            elif(stick == 15):
                com = 4
                stick -= com
                print("\nComputer takes 4")
            elif(stick == 14):
                com = 3
                stick -= com
                print("\nComputer takes 3")
            elif(stick == 13):
                com = 2
                stick -= com
                print("\nComputer takes 2")
            elif(stick == 12):
                com = 1
                stick -= com
                print("\nComputer takes 1")
                
            elif(stick == 10):
                com = 4
                stick -= com
                print("\nComputer takes 4")
            elif(stick == 9):
                com = 3
                stick -= com
                print("\nComputer takes 3")
            elif(stick == 8):
                com = 2
                stick -= com
                print("\nComputer takes 2")
            elif(stick == 7):
                com = 1
                stick -= com
                print("\nComputer takes 1")
                
            elif(stick == 5):
                com = 4
                stick -= com
                print("\nComputer takes 4")
            elif(stick == 4):
                com = 3
                stick -= com
                print("\nComputer takes 3")
            elif(stick == 3):
                com = 2
                stick -= com
                print("\nComputer takes 2")
            elif(stick == 2):
                com = 1
                stick -= com
                print("\nComputer takes 1")
                print("\nThe Last Stick is for you XD\nYou Lose!")
                break
    
